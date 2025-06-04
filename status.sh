#!/bin/bash

# MSSQL MCP Server Status Script

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

echo "📊 MSSQL MCP Server Status"
echo "=========================="

# Check if PID file exists
if [ ! -f "server.pid" ]; then
    print_warning "No PID file found"
    
    # Check if any python processes are running the server
    server_pids=$(pgrep -f "src/server.py" 2>/dev/null || true)
    
    if [ -n "$server_pids" ]; then
        print_warning "Server processes found running without PID file:"
        echo "$server_pids" | while read pid; do
            if [ -n "$pid" ]; then
                echo "  PID: $pid"
            fi
        done
        print_info "Consider running './stop.sh' to clean up"
    else
        print_error "Server is not running"
    fi
    exit 1
fi

# Read PID from file
pid=$(cat server.pid)

# Check if process is actually running
if ! ps -p $pid > /dev/null 2>&1; then
    print_error "Server is not running (stale PID file)"
    print_info "PID file contains: $pid"
    print_info "Run './stop.sh' to clean up or './start.sh' to restart"
    exit 1
fi

# Server is running
print_success "Server is running"
echo "  PID: $pid"

# Get process information
if command -v ps &> /dev/null; then
    process_info=$(ps -p $pid -o pid,ppid,etime,pcpu,pmem,cmd --no-headers 2>/dev/null || true)
    if [ -n "$process_info" ]; then
        echo "  Process Info:"
        echo "    $process_info"
    fi
fi

# Check log file
if [ -f "server.log" ]; then
    log_size=$(wc -c < server.log 2>/dev/null || echo "unknown")
    log_lines=$(wc -l < server.log 2>/dev/null || echo "unknown")
    print_info "Log file: server.log ($log_lines lines, $log_size bytes)"
    
    # Show last few lines of log
    echo ""
    print_info "Recent log entries:"
    tail -10 server.log 2>/dev/null | sed 's/^/    /' || print_warning "Could not read log file"
else
    print_warning "No log file found"
fi

# Check environment configuration
echo ""
print_info "Environment Configuration:"
if [ -f ".env" ]; then
    print_success ".env file exists"
    
    # Check key variables (without showing sensitive data)
    if grep -q "MSSQL_SERVER=" .env 2>/dev/null; then
        server_value=$(grep "MSSQL_SERVER=" .env | cut -d'=' -f2 | sed 's/^[[:space:]]*//' | sed 's/[[:space:]]*$//')
        if [ -n "$server_value" ]; then
            print_success "MSSQL_SERVER is configured"
        else
            print_warning "MSSQL_SERVER is empty"
        fi
    else
        print_warning "MSSQL_SERVER not found in .env"
    fi
    
    if grep -q "MSSQL_DATABASE=" .env 2>/dev/null; then
        db_value=$(grep "MSSQL_DATABASE=" .env | cut -d'=' -f2 | sed 's/^[[:space:]]*//' | sed 's/[[:space:]]*$//')
        if [ -n "$db_value" ]; then
            print_success "MSSQL_DATABASE is configured"
        else
            print_warning "MSSQL_DATABASE is empty"
        fi
    else
        print_warning "MSSQL_DATABASE not found in .env"
    fi
    
    if grep -q "MSSQL_USER=" .env 2>/dev/null; then
        print_success "MSSQL_USER is configured"
    else
        print_info "MSSQL_USER not configured (may be using Windows auth)"
    fi
else
    print_error ".env file not found"
fi

# Check virtual environment
echo ""
print_info "Virtual Environment:"
if [ -d "venv" ]; then
    print_success "Virtual environment exists"
    if [ -n "$VIRTUAL_ENV" ]; then
        print_success "Virtual environment is activated"
    else
        print_info "Virtual environment is not activated in current shell"
    fi
else
    print_warning "Virtual environment not found"
fi

echo ""
print_info "Control Commands:"
echo "  Start:  ./start.sh"
echo "  Stop:   ./stop.sh"
echo "  Status: ./status.sh"
echo "  Logs:   tail -f server.log" 