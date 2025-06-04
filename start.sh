#!/bin/bash

# MSSQL MCP Server Start Script

set -e  # Exit on any error

echo "🚀 Starting MSSQL MCP Server..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    print_error "Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Check Python version
python_version=$(python3 -c "import sys; print('.'.join(map(str, sys.version_info[:2])))")
required_version="3.8"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then
    print_error "Python $python_version is installed, but Python $required_version or higher is required."
    exit 1
fi

print_success "Python $python_version detected"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    print_warning "Virtual environment not found. Creating one..."
    python3 -m venv venv
    print_success "Virtual environment created"
fi

# Activate virtual environment
print_info "Activating virtual environment..."
source venv/bin/activate

# Check if dependencies are installed
print_info "Checking dependencies..."
if ! python -c "import pyodbc, pydantic, mcp" &> /dev/null; then
    print_warning "Dependencies not found. Installing..."
    pip install -r requirements.txt
    print_success "Dependencies installed"
fi

# Environment validation
print_info "Validating environment configuration..."

# Check if .env file exists
if [ ! -f ".env" ]; then
    print_error ".env file not found!"
    print_info "Please create a .env file based on env.example:"
    echo ""
    echo "  cp env.example .env"
    echo ""
    print_info "Then edit .env with your database configuration."
    exit 1
fi

# Load environment variables from .env file using Python to handle special characters
eval $(python3 -c "
import os
import shlex
from dotenv import load_dotenv
load_dotenv()
for key, value in os.environ.items():
    if key.startswith('MSSQL_') or key in ['TrustServerCertificate', 'Trusted_Connection']:
        # Use shlex.quote to properly escape the value
        escaped_value = shlex.quote(value)
        print(f'export {key}={escaped_value}')
")

# Validate required environment variables
validation_failed=false

validate_env_var() {
    local var_name=$1
    local var_value=${!var_name}
    
    if [ -z "$var_value" ]; then
        print_error "$var_name is not set in .env file"
        validation_failed=true
        return 1
    else
        print_success "$var_name is configured"
        return 0
    fi
}

# Check required variables
validate_env_var "MSSQL_SERVER"
validate_env_var "MSSQL_DATABASE"

# Check if authentication is properly configured
if [ -z "$MSSQL_USER" ] && [ "$Trusted_Connection" != "yes" ]; then
    print_error "Either MSSQL_USER must be set or Trusted_Connection must be 'yes'"
    validation_failed=true
fi

if [ -n "$MSSQL_USER" ] && [ -z "$MSSQL_PASSWORD" ]; then
    print_error "MSSQL_PASSWORD must be set when MSSQL_USER is provided"
    validation_failed=true
fi

if [ "$validation_failed" = true ]; then
    print_error "Environment validation failed. Please check your .env file."
    echo ""
    print_info "Required variables:"
    echo "  - MSSQL_SERVER: Your SQL Server hostname/IP"
    echo "  - MSSQL_DATABASE: Database name to connect to"
    echo "  - MSSQL_USER: Username (if not using Windows authentication)"
    echo "  - MSSQL_PASSWORD: Password (if using SQL Server authentication)"
    echo ""
    print_info "Optional variables:"
    echo "  - MSSQL_PORT: Port number (default: 1433)"
    echo "  - MSSQL_DRIVER: ODBC driver (default: {ODBC Driver 17 for SQL Server})"
    echo "  - TrustServerCertificate: yes/no (default: yes)"
    echo "  - Trusted_Connection: yes/no (default: no)"
    exit 1
fi

# Test database connection
print_info "Testing database connection..."
if python3 -c "
import os
import pyodbc
from dotenv import load_dotenv

load_dotenv()

driver = os.getenv('MSSQL_DRIVER', '{ODBC Driver 17 for SQL Server}')
server = os.getenv('MSSQL_SERVER')
database = os.getenv('MSSQL_DATABASE')
username = os.getenv('MSSQL_USER', '')
password = os.getenv('MSSQL_PASSWORD', '')
port = os.getenv('MSSQL_PORT', '1433')
trust_cert = os.getenv('TrustServerCertificate', 'yes')
trusted_conn = os.getenv('Trusted_Connection', 'no')

conn_str = f'DRIVER={driver};SERVER={server},{port};DATABASE={database};'
if username and password:
    conn_str += f'UID={username};PWD={password};'
conn_str += f'TrustServerCertificate={trust_cert};Trusted_Connection={trusted_conn};'

try:
    conn = pyodbc.connect(conn_str, timeout=10)
    cursor = conn.cursor()
    cursor.execute('SELECT 1')
    cursor.fetchone()
    conn.close()
    print('Connection successful')
except Exception as e:
    print(f'Connection failed: {e}')
    exit(1)
" 2>/dev/null; then
    print_success "Database connection test passed"
else
    print_error "Database connection test failed"
    print_info "Please check your database configuration and ensure:"
    echo "  - SQL Server is running and accessible"
    echo "  - Database exists and you have access permissions"
    echo "  - Network connectivity is available"
    echo "  - ODBC Driver 17 for SQL Server is installed"
    exit 1
fi

# Check if server is already running
if [ -f "server.pid" ]; then
    pid=$(cat server.pid)
    if ps -p $pid > /dev/null 2>&1; then
        print_warning "Server is already running (PID: $pid)"
        print_info "Use './stop.sh' to stop the server first"
        exit 1
    else
        print_warning "Stale PID file found, removing..."
        rm server.pid
    fi
fi

# Start the server
print_success "All validations passed! Starting MCP server..."
echo ""
print_info "Server will run in the background. Use './stop.sh' to stop it."
print_info "Logs will be written to server.log"
echo ""

# Start server in background and save PID
nohup python3 src/server.py > server.log 2>&1 &
server_pid=$!
echo $server_pid > server.pid

# Wait a moment and check if server started successfully
sleep 2
if ps -p $server_pid > /dev/null 2>&1; then
    print_success "MSSQL MCP Server started successfully (PID: $server_pid)"
    print_info "Server is running in the background"
    print_info "View logs with: tail -f server.log"
else
    print_error "Failed to start server. Check server.log for details."
    rm -f server.pid
    exit 1
fi 