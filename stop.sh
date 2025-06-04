#!/bin/bash

# MSSQL MCP Server Stop Script

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

echo "🛑 Stopping MSSQL MCP Server..."

# Check if PID file exists
if [ ! -f "server.pid" ]; then
    print_warning "No PID file found. Server may not be running."
    
    # Check if any python processes are running the server
    server_pids=$(pgrep -f "src/server.py" 2>/dev/null || true)
    
    if [ -n "$server_pids" ]; then
        print_warning "Found running server processes. Attempting to stop them..."
        echo "$server_pids" | while read pid; do
            if [ -n "$pid" ]; then
                print_info "Stopping process $pid..."
                kill $pid 2>/dev/null || true
                
                # Wait for process to stop
                for i in {1..10}; do
                    if ! ps -p $pid > /dev/null 2>&1; then
                        print_success "Process $pid stopped"
                        break
                    fi
                    sleep 1
                done
                
                # Force kill if still running
                if ps -p $pid > /dev/null 2>&1; then
                    print_warning "Force killing process $pid..."
                    kill -9 $pid 2>/dev/null || true
                fi
            fi
        done
        print_success "All server processes stopped"
    else
        print_info "No running server processes found"
    fi
    exit 0
fi

# Read PID from file
pid=$(cat server.pid)

# Check if process is actually running
if ! ps -p $pid > /dev/null 2>&1; then
    print_warning "Process $pid is not running. Cleaning up PID file..."
    rm server.pid
    print_success "Cleanup complete"
    exit 0
fi

print_info "Stopping server process $pid..."

# Try graceful shutdown first
kill $pid 2>/dev/null

# Wait for process to stop gracefully
stopped=false
for i in {1..10}; do
    if ! ps -p $pid > /dev/null 2>&1; then
        stopped=true
        break
    fi
    print_info "Waiting for graceful shutdown... ($i/10)"
    sleep 1
done

if [ "$stopped" = false ]; then
    print_warning "Graceful shutdown failed. Force killing process..."
    kill -9 $pid 2>/dev/null || true
    
    # Wait a bit more
    sleep 2
    
    if ps -p $pid > /dev/null 2>&1; then
        print_error "Failed to stop process $pid"
        exit 1
    fi
fi

# Clean up PID file
rm server.pid

print_success "MSSQL MCP Server stopped successfully"

# Show final status
print_info "Server status: Stopped"
if [ -f "server.log" ]; then
    print_info "Logs are available in server.log"
    
    # Show last few lines of log
    echo ""
    print_info "Last few log entries:"
    tail -5 server.log 2>/dev/null || print_warning "Could not read log file"
fi 