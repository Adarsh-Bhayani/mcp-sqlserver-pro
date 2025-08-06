# 🚀 MCP SQL Server Pro - Comprehensive Database Management Server

A powerful Model Context Protocol (MCP) server that provides complete access to Microsoft SQL Server databases. This professional-grade server enables AI assistants and Language Models to perform comprehensive database operations, schema exploration, and advanced database management through a standardized MCP interface.

## 📋 Table of Contents

- [🌟 Key Features](#-key-features)
- [🛠️ Complete Setup Guide](#️-complete-setup-guide)
- [⚙️ Configuration](#️-configuration)
- [🔧 Available Tools](#-available-tools-complete-list)
- [🎯 Usage Examples](#-usage-examples)
- [🤖 AI Assistant Integration](#-ai-assistant-integration)
- [🔒 Security & Best Practices](#-security--best-practices)
- [🐛 Troubleshooting](#-troubleshooting)

## 🌟 Key Features

### **🎯 Comprehensive Database Management**
- **9 Powerful Tools with 41 Actions** - Streamlined tools with multiple actions for complete database operations
- **Schema Exploration** - Full database hierarchy traversal (tables, views, procedures, functions, indexes)
- **Advanced Analytics** - Enhanced performance monitoring, deadlock analysis, and optimization tools
- **Resource Access** - All tables and views accessible as MCP resources
- **Large Content Support** - Handles large stored procedures and complex database objects

### **🔧 Core Capabilities**
- **Query Execution** - SELECT, INSERT, UPDATE, DELETE with proper validation
- **Object Management** - Create, modify, delete tables, views, procedures, functions, indexes
- **Performance Analysis** - Missing indexes, unused indexes, blocking sessions, wait statistics
- **Schema Operations** - Complete schema management and organization
- **Function Management** - User-defined functions (scalar, table-valued, inline)
- **Advanced Monitoring** - Deadlock graphs, performance metrics, system health

### **⚡ Technical Highlights**
- **Secure Operations** - Proper query validation and SQL injection prevention
- **Efficient Processing** - Optimized for large database objects and complex operations
- **Flexible Authentication** - Windows Authentication or SQL Server Authentication
- **Resource Streaming** - Efficient handling of large data sets and complex objects
- **Error Handling** - Comprehensive error reporting and validation
- **Enhanced Performance Monitoring** - New capabilities for connection stats, slow queries, and failed logins

### **🆕 New Enhanced Features**
- **Advanced Performance Analytics** - Monitor slow queries, connection statistics, and failed login attempts
- **Buffer Pool Memory Monitoring** - Track memory usage, cache hit ratios, and page life expectancy
- **Historical Blocking Analysis** - Track previous blocking sessions with configurable time ranges
- **Index Fragmentation Analysis** - Identify fragmented indexes with customizable thresholds
- **Comprehensive Database Statistics** - Get detailed performance metrics and query statistics
- **Streamlined Tool Architecture** - 9 powerful tools with 40+ actions for better organization

## 🛠️ Complete Setup Guide

### **Prerequisites**

Before installing MCP SQL Server Pro, ensure you have the following:

#### **1. Python Requirements**
- **Python 3.8 or higher** (Python 3.10+ recommended)
- **pip** (Python package installer)

#### **2. Database Requirements**
- **Microsoft SQL Server** (2016 or later)
- **Database access permissions** (read/write as needed)
- **Network connectivity** to SQL Server instance

#### **3. System Requirements**
- **ODBC Driver 17 for SQL Server** (critical requirement)
- **Operating System**: Windows, macOS, or Linux

### **Step-by-Step Installation**

#### **Option 1: Automated Installation (Recommended)**

1. **Download/Clone the Project**
   ```bash
   # Clone from repository
   git clone https://github.com/your-repo/mcp-sqlserver-pro.git
   cd mcp-sqlserver-pro
   
   # Or create directory and download files
   mkdir mcp-sqlserver-pro
   cd mcp-sqlserver-pro
   # Download all project files to this directory
   ```

2. **Run Automated Installation**
   ```bash
   # Make installation script executable (Linux/macOS)
   chmod +x install.sh
   
   # Run installation
   ./install.sh
   ```

   **For Windows (PowerShell):**
   ```powershell
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   .\venv\Scripts\Activate.ps1
   
   # Install dependencies
   pip install -r requirements.txt
   ```

#### **Option 2: Manual Installation**

1. **Create Project Directory**
   ```bash
   mkdir mcp-sqlserver-pro
   cd mcp-sqlserver-pro
   ```

2. **Create Virtual Environment**
   ```bash
   # Create virtual environment
   python3 -m venv venv
   
   # Activate virtual environment
   # Linux/macOS:
   source venv/bin/activate
   
   # Windows:
   venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   # Upgrade pip first
   pip install --upgrade pip
   
   # Install required packages
   pip install pyodbc>=4.0.39
   pip install pydantic>=2.0.0
   pip install python-dotenv>=1.0.1
   pip install mcp>=1.2.0
   pip install anyio>=4.5.0
   pip install asyncio-mqtt>=0.16.2
   pip install pytest>=7.0.0
   pip install pytest-asyncio>=0.21.0
   ```

### **ODBC Driver Installation**

The ODBC Driver 17 for SQL Server is **critical** for database connectivity.

#### **Windows**
1. Download from [Microsoft Download Center](https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server)
2. Run the installer as Administrator
3. Follow installation wizard

#### **macOS**
   ```bash
# Using Homebrew
   brew tap microsoft/mssql-release
   brew install msodbcsql17 mssql-tools

# Alternative: Download from Microsoft
# Visit: https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/install-microsoft-odbc-driver-sql-server-macos
```

#### **Linux (Ubuntu/Debian)**
```bash
# Add Microsoft repository
curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list | sudo tee /etc/apt/sources.list.d/msprod.list

# Update and install
sudo apt-get update
sudo ACCEPT_EULA=Y apt-get install -y msodbcsql17 mssql-tools
```

#### **Linux (Red Hat/CentOS)**
```bash
# Add Microsoft repository
sudo curl -o /etc/yum.repos.d/msprod.repo https://packages.microsoft.com/config/rhel/8/prod.repo

# Install driver
sudo ACCEPT_EULA=Y yum install -y msodbcsql17 mssql-tools
```

### **Verification**

After installation, verify everything is working:

```bash
# Check Python version
python --version

# Check if virtual environment is active
which python

# Check ODBC driver installation
python -c "import pyodbc; print(pyodbc.drivers())"

# Test basic imports
python -c "import pyodbc, pydantic, mcp; print('All dependencies imported successfully')"
```

## ⚙️ Configuration

### **Environment Setup**

1. **Create Configuration File**
```bash
   # Copy example configuration
   cp env.example .env
   
   # Edit with your database details
   nano .env  # or use your preferred editor
   ```

2. **Configuration Options**
```env
   # Required Settings
   MSSQL_SERVER=your-server-hostname-or-ip
MSSQL_DATABASE=your-database-name
   
   # Authentication (choose one method)
   # Method 1: SQL Server Authentication
MSSQL_USER=your-username
MSSQL_PASSWORD=your-password
   Trusted_Connection=no
   
   # Method 2: Windows Authentication
   Trusted_Connection=yes
   # (leave MSSQL_USER and MSSQL_PASSWORD empty)
   
   # Optional Settings
MSSQL_PORT=1433
   MSSQL_DRIVER={ODBC Driver 17 for SQL Server}
TrustServerCertificate=yes
```

### **Configuration Examples**

#### **Local SQL Server Instance**
```env
MSSQL_SERVER=localhost
MSSQL_DATABASE=MyDatabase
MSSQL_USER=sa
MSSQL_PASSWORD=YourStrongPassword123!
MSSQL_PORT=1433
TrustServerCertificate=yes
Trusted_Connection=no
```

#### **Remote SQL Server with Windows Auth**
```env
MSSQL_SERVER=sql-server.company.com
MSSQL_DATABASE=ProductionDB
MSSQL_PORT=1433
TrustServerCertificate=yes
Trusted_Connection=yes
```

#### **Azure SQL Database**
```env
MSSQL_SERVER=your-server.database.windows.net
MSSQL_DATABASE=your-database
MSSQL_USER=your-username@your-server
MSSQL_PASSWORD=your-password
MSSQL_PORT=1433
TrustServerCertificate=yes
Trusted_Connection=no
```

### **Testing Configuration**

Test your database connection before using the MCP server:

```bash
# Activate virtual environment
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate     # Windows

# Test connection
python3 -c "
import os
import pyodbc
from dotenv import load_dotenv

load_dotenv()

# Build connection string
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
    cursor.execute('SELECT @@VERSION')
    version = cursor.fetchone()
    print(f'✅ Connection successful!')
    print(f'📊 SQL Server Version: {version[0][:50]}...')
    conn.close()
except Exception as e:
    print(f'❌ Connection failed: {e}')
"
```

## 🔧 Available Tools (Complete List)

MCP SQL Server Pro provides **9 powerful tools with 41 actions** organized into functional categories:

### **📊 1. Query Tool**
**Execute SQL queries with read/write actions**

| Action | Description | Parameters |
|--------|-------------|------------|
| `read` | Execute SELECT queries to read data | `sql` (string) - SELECT SQL query to execute |
| `write` | Execute INSERT, UPDATE, DELETE queries | `sql` (string) - SQL query to execute |

**Usage:**
```json
{
  "tool": "query",
  "parameters": {
    "action": "read",
    "sql": "SELECT TOP 10 * FROM Customers"
  }
}
```

### **🗃️ 2. Table Tool**
**Manage database tables with comprehensive operations**

| Action | Description | Parameters |
|--------|-------------|------------|
| `list` | List all tables in the database | None |
| `describe` | Get detailed table schema information | `table_name` (string) |
| `create` | Create new tables with DDL | `sql` (string) - CREATE TABLE statement |

**Usage:**
```json
{
  "tool": "table",
  "parameters": {
    "action": "describe",
    "table_name": "Customers"
  }
}
```

### **📋 3. Procedure Tool**
**Complete stored procedure management**

| Action | Description | Parameters |
|--------|-------------|------------|
| `list` | List all stored procedures with metadata | None |
| `describe` | Get complete procedure definitions | `procedure_name` (string) |
| `create` | Create new stored procedures | `procedure_script` (string) |
| `execute` | Execute procedures with parameters | `procedure_name` (string), `parameters` (array) |
| `modify` | Modify existing stored procedures | `procedure_script` (string) |
| `delete` | Delete stored procedures | `procedure_name` (string) |
| `get_parameters` | Get detailed parameter information | `procedure_name` (string) |

### **🔧 4. Function Tool**
**User-defined function management**

| Action | Description | Parameters |
|--------|-------------|------------|
| `list` | List all user-defined functions | None |
| `describe` | Get function definitions | `function_name` (string) |
| `create` | Create new functions | `function_script` (string) |
| `execute` | Execute scalar functions | `function_name` (string), `parameters` (array) |
| `modify` | Modify existing functions | `function_script` (string) |
| `delete` | Delete functions | `function_name` (string) |

### **👁️ 5. View Tool**
**Database view management**

| Action | Description | Parameters |
|--------|-------------|------------|
| `list` | List all views in the database | None |
| `describe` | Get view definitions and schema | `view_name` (string) |
| `create` | Create new views | `view_script` (string) |
| `modify` | Modify existing views | `view_script` (string) |
| `delete` | Delete views | `view_name` (string) |

### **🗂️ 6. Index Tool**
**Index management and operations**

| Action | Description | Parameters |
|--------|-------------|------------|
| `list` | List all indexes (optionally by table) | `table_name` (optional string) |
| `describe` | Get detailed index information | `index_name` (string), `table_name` (string) |
| `create` | Create new indexes | `index_script` (string) |
| `delete` | Delete indexes | `index_name` (string), `table_name` (string) |

### **📁 7. Schema Tool**
**Database schema and metadata management**

| Action | Description | Parameters |
|--------|-------------|------------|
| `list_schemas` | List all schemas in the database | None |
| `list_objects` | List all database objects by schema | `schema_name` (optional string) |
| `table_size` | Get row count and disk space usage | `table_name` (string) |

### **🔍 8. Index Analysis Tool**
**Advanced index analysis and optimization**

| Action | Description | Parameters |
|--------|-------------|------------|
| `unused` | Find unused indexes for optimization | None |
| `missing_recommendations` | Get missing index suggestions | None |
| `fragmented` | Find fragmented indexes | `fragmentation_threshold` (number, default: 10) |

### **📈 9. Performance Tool**
**Comprehensive performance monitoring and analysis**

| Action | Description | Parameters |
|--------|-------------|------------|
| `top_waits` | Get top wait types by wait time | None |
| `connection_stats` | Get database connection statistics | None |
| `blocking_sessions` | Get current blocking session details | None |
| `deadlock_graph` | Get recent deadlock graph XML | None |
| `previous_blocking` | Get historical blocking sessions | `hours_back` (number), `min_duration_seconds` (number) |
| `database_stats` | Get comprehensive database performance stats | `include_query_stats` (boolean), `top_queries_count` (number) |
| `slow_queries` | Get slow-performing queries | `min_elapsed_ms` (number), `top_n` (integer) |
| `failed_logins` | Get failed login attempts | `time_period_minutes` (integer) |
| `buffer_pool_stats` | Get buffer pool memory usage and cache hit ratios | None |

### **📋 MCP Resources**

All tables and views are automatically exposed as MCP resources:
- **URI Format**: `mssql://table_name/data` or `mssql://view_name/data`
- **Format**: CSV with first 100 rows
- **Access**: Direct resource access for quick data exploration

## 🎯 Usage Examples

### **🚀 Starting the Server**

```bash
# Activate virtual environment
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate     # Windows

# Start MCP server
python src/server.py
```

The server communicates via stdin/stdout using JSON-RPC protocol for MCP clients.

### **📊 Basic Database Operations**

#### **Query Data**
```json
{
  "tool": "query",
  "parameters": {
    "action": "read",
    "sql": "SELECT TOP 10 * FROM Customers ORDER BY CustomerID"
  }
}
```

#### **Insert Data**
```json
{
  "tool": "query",
  "parameters": {
    "action": "write",
    "sql": "INSERT INTO Customers (CustomerName, City, Country) VALUES ('New Customer', 'New York', 'USA')"
  }
}
```

#### **Explore Database Structure**
```json
{
  "tool": "table",
  "parameters": {
    "action": "list"
  }
}

{
  "tool": "table",
  "parameters": {
    "action": "describe",
    "table_name": "Customers"
  }
}
```

### **🗃️ Advanced Object Management**

#### **Create a Comprehensive Stored Procedure**
```json
{
  "tool": "procedure",
  "parameters": {
    "action": "create",
    "procedure_script": "CREATE PROCEDURE GetCustomerOrders\n    @CustomerID INT,\n    @StartDate DATE = NULL,\n    @EndDate DATE = NULL\nAS\nBEGIN\n    SELECT \n        o.OrderID,\n        o.OrderDate,\n        od.ProductID,\n        p.ProductName,\n        od.Quantity,\n        od.UnitPrice,\n        (od.Quantity * od.UnitPrice) AS LineTotal\n    FROM Orders o\n    INNER JOIN OrderDetails od ON o.OrderID = od.OrderID\n    INNER JOIN Products p ON od.ProductID = p.ProductID\n    WHERE o.CustomerID = @CustomerID\n    AND (@StartDate IS NULL OR o.OrderDate >= @StartDate)\n    AND (@EndDate IS NULL OR o.OrderDate <= @EndDate)\n    ORDER BY o.OrderDate DESC, od.ProductID\nEND"
  }
}
```

#### **Create a User-Defined Function**
```json
{
  "tool": "function",
  "parameters": {
    "action": "create",
    "function_script": "CREATE FUNCTION dbo.CalculateOrderTotal(@OrderID INT)\nRETURNS DECIMAL(10,2)\nAS\nBEGIN\n    DECLARE @Total DECIMAL(10,2)\n    \n    SELECT @Total = SUM(Quantity * UnitPrice)\n    FROM OrderDetails\n    WHERE OrderID = @OrderID\n    \n    RETURN ISNULL(@Total, 0)\nEND"
  }
}
```

#### **Advanced Performance Analysis**
```json
{
  "tool": "index_analysis",
  "parameters": {
    "action": "missing_recommendations"
  }
}

{
  "tool": "index_analysis",
  "parameters": {
    "action": "unused"
  }
}

{
  "tool": "performance",
  "parameters": {
    "action": "top_waits"
  }
}

{
  "tool": "performance",
  "parameters": {
    "action": "slow_queries",
    "min_elapsed_ms": 1000,
    "top_n": 10
  }
}
```

### **🔍 New Performance Monitoring Examples**

#### **Monitor Database Connection Statistics**
```json
{
  "tool": "performance",
  "parameters": {
    "action": "connection_stats"
  }
}
```

#### **Analyze Historical Blocking Sessions**
```json
{
  "tool": "performance",
  "parameters": {
    "action": "previous_blocking",
    "hours_back": 24,
    "min_duration_seconds": 5
  }
}
```

#### **Get Comprehensive Database Performance Stats**
```json
{
  "tool": "performance",
  "parameters": {
    "action": "database_stats",
    "include_query_stats": true,
    "top_queries_count": 10
  }
}
```

#### **Monitor Failed Login Attempts**
```json
{
  "tool": "performance",
  "parameters": {
    "action": "failed_logins",
    "time_period_minutes": 120
  }
}
```

#### **Find Fragmented Indexes**
```json
{
  "tool": "index_analysis",
  "parameters": {
    "action": "fragmented",
    "fragmentation_threshold": 15
  }
}
```

#### **Buffer Pool Memory Analysis**
```json
{
  "tool": "performance",
  "parameters": {
    "action": "buffer_pool_stats"
  }
}
```

#### **Schema Management Examples**
```json
{
  "tool": "schema",
  "parameters": {
    "action": "list_schemas"
  }
}

{
  "tool": "schema",
  "parameters": {
    "action": "table_size",
    "table_name": "Orders"
  }
}
```

## 🤖 AI Assistant Integration

### **Claude Desktop Configuration**

Add MCP SQL Server Pro to your Claude Desktop configuration:

#### **Method 1: Environment Variables in Config**
```json
{
  "mcpServers": {
    "mssql-pro": {
      "command": "python",
      "args": ["/absolute/path/to/mcp-sqlserver-pro/src/server.py"],
      "cwd": "/absolute/path/to/mcp-sqlserver-pro",
      "env": {
        "MSSQL_SERVER": "your-server-hostname",
        "MSSQL_DATABASE": "your-database-name",
        "MSSQL_USER": "your-username",
        "MSSQL_PASSWORD": "your-password",
        "MSSQL_PORT": "1433",
        "TrustServerCertificate": "yes",
        "Trusted_Connection": "no"
      }
    }
  }
}
```

#### **Method 2: Using .env File (Recommended)**
```json
{
  "mcpServers": {
    "mssql-pro": {
      "command": "python",
      "args": ["/absolute/path/to/mcp-sqlserver-pro/src/server.py"],
      "cwd": "/absolute/path/to/mcp-sqlserver-pro"
    }
  }
}
```

### **Windows Configuration Example**
```json
{
  "mcpServers": {
    "mssql-pro": {
      "command": "C:\\Users\\YourUsername\\mcp-sqlserver-pro\\venv\\Scripts\\python.exe",
      "args": ["C:\\Users\\YourUsername\\mcp-sqlserver-pro\\src\\server.py"],
      "cwd": "C:\\Users\\YourUsername\\mcp-sqlserver-pro"
    }
  }
}
```

### **macOS/Linux Configuration Example**
```json
{
  "mcpServers": {
    "mssql-pro": {
      "command": "/Users/yourusername/mcp-sqlserver-pro/venv/bin/python",
      "args": ["/Users/yourusername/mcp-sqlserver-pro/src/server.py"],
      "cwd": "/Users/yourusername/mcp-sqlserver-pro"
    }
  }
}
```

### **Testing Integration**

After configuring Claude Desktop:

1. **Restart Claude Desktop**
2. **Start a new conversation**
3. **Test basic functionality**:
   ```
   Can you show me all the tables in my database?
   ```
4. **Test advanced features**:
   ```
   Can you analyze the performance of my database and suggest missing indexes?
   ```

## 🔒 Security & Best Practices

### **🛡️ Database Security**

#### **Authentication Best Practices**
- **Use strong passwords** (minimum 12 characters, mixed case, numbers, symbols)
- **Prefer Windows Authentication** when possible for integrated security
- **Use dedicated service accounts** with minimal required permissions
- **Enable SSL/TLS encryption** for remote connections

#### **Permission Management**
```sql
-- Create dedicated user for MCP server
CREATE LOGIN mcp_service WITH PASSWORD = 'YourStrongPassword123!';
CREATE USER mcp_service FOR LOGIN mcp_service;

-- Grant minimal required permissions
GRANT SELECT, INSERT, UPDATE, DELETE ON SCHEMA::dbo TO mcp_service;
GRANT CREATE TABLE, CREATE PROCEDURE, CREATE FUNCTION, CREATE VIEW TO mcp_service;
GRANT ALTER ON SCHEMA::dbo TO mcp_service;

-- For read-only scenarios
GRANT SELECT ON SCHEMA::dbo TO mcp_service;
GRANT VIEW DEFINITION ON SCHEMA::dbo TO mcp_service;
```

### **🔐 Configuration Security**

#### **Environment File Protection**
```bash
# Set restrictive permissions on .env file
chmod 600 .env  # Linux/macOS
# Windows: Use file properties to restrict access
```

#### **Secure Configuration Example**
```env
# Use environment-specific configurations
MSSQL_SERVER=prod-sql.internal.company.com
MSSQL_DATABASE=ProductionDB
MSSQL_USER=mcp_service
MSSQL_PASSWORD=ComplexPassword123!@#
TrustServerCertificate=no  # Use valid certificates in production
Trusted_Connection=no
```

### **🚫 Built-in Security Features**

The server includes comprehensive security measures:

- **Query Type Validation**: Only allows appropriate queries for each tool
- **SQL Injection Prevention**: Uses parameterized queries where possible
- **DDL Operation Validation**: Validates CREATE, ALTER, DROP statements
- **Input Sanitization**: Cleans and validates all input parameters
- **Connection Security**: Secure connection string handling
- **Error Handling**: Prevents sensitive information leakage in error messages

## 🐛 Troubleshooting

### **🔧 Common Installation Issues**

#### **Python Version Problems**
```bash
# Check Python version
python --version
python3 --version

# Install specific Python version if needed
# Windows: Download from python.org
# macOS: brew install python@3.11
# Linux: sudo apt install python3.11
```

#### **ODBC Driver Issues**
```bash
# Check installed drivers
python -c "import pyodbc; print(pyodbc.drivers())"

# Expected output should include:
# ['ODBC Driver 17 for SQL Server', ...]
```

**If ODBC driver is missing:**
- **Windows**: Download and install from Microsoft
- **macOS**: `brew install msodbcsql17`
- **Linux**: Follow Microsoft's installation guide for your distribution

#### **Virtual Environment Problems**
```bash
# Recreate virtual environment
rm -rf venv
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# or venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### **🔌 Connection Issues**

#### **Connection Timeout**
```
Error: Connection timeout
```

**Solutions:**
1. **Check server address and port**
2. **Verify firewall settings**
3. **Test with SQL Server Management Studio**
4. **Check SQL Server is running**

#### **Authentication Failed**
```
Error: Login failed for user
```

**Solutions:**
1. **Verify credentials in .env file**
2. **Check SQL Server authentication mode**
3. **Ensure user exists and has permissions**
4. **Test connection with SQL tools**

#### **Database Not Found**
```
Error: Cannot open database requested by the login
```

**Solutions:**
1. **Verify database name spelling**
2. **Check database exists**
3. **Ensure user has access to database**
4. **Check database is online**

### **🚀 Performance Issues**

#### **Slow Query Performance**
```bash
# Enable debug logging
# Edit src/server.py and change:
logging.basicConfig(level=logging.DEBUG)
```

**Analysis Steps:**
1. **Check query execution plans**
2. **Use `get_missing_index_recommendations`**
3. **Monitor with `get_top_waits`**
4. **Analyze with `get_blocking_sessions`**

### **🔍 Debugging Steps**

#### **1. Basic Connectivity Test**
```python
import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

# Test basic connection
try:
    conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={os.getenv('MSSQL_SERVER')};DATABASE={os.getenv('MSSQL_DATABASE')};UID={os.getenv('MSSQL_USER')};PWD={os.getenv('MSSQL_PASSWORD')}"
    conn = pyodbc.connect(conn_str)
    print("✅ Connection successful")
    conn.close()
except Exception as e:
    print(f"❌ Connection failed: {e}")
```

#### **2. MCP Server Test**
```bash
# Test server startup
python src/server.py

# Should show:
# INFO - Starting MCP server...
# INFO - Server streams established
```

#### **3. Tool Availability Test**
After connecting through Claude Desktop:
```
Please list all available tools and test the list_tables tool.
```

### **📞 Getting Help**

#### **Log Analysis**
```bash
# Check server logs
tail -f server.log

# Check system logs
# Windows: Event Viewer
# Linux: journalctl -f
# macOS: Console app
```

#### **Common Log Messages**
```
INFO - Starting MCP server...          # Normal startup
ERROR - Failed to connect to database  # Connection issue
DEBUG - Executing query: SELECT...     # Query execution
ERROR - Tool execution failed          # Tool error
```

---

## 📋 Summary

MCP SQL Server Pro provides comprehensive database management capabilities through **9 powerful tools with 41 actions**, making it the most complete and well-organized MCP server for Microsoft SQL Server integration. The new streamlined architecture provides better organization while maintaining all the functionality you need for professional database operations.

### **Key Benefits**
- ✅ **Streamlined Architecture** - 9 organized tools with 41 actions for better usability
- ✅ **Enhanced Performance Monitoring** - New advanced analytics and monitoring capabilities
- ✅ **Complete Database Management** - All major database operations covered
- ✅ **Professional Security** - Built-in validation and security measures
- ✅ **Easy Setup** - Comprehensive installation guide for any PC
- ✅ **AI Integration** - Seamless integration with Claude Desktop and other MCP clients

### **🆕 What's New in This Version**
- **Consolidated Tools** - Streamlined from 35+ individual tools to 9 organized tools with actions
- **Enhanced Performance Analytics** - New monitoring capabilities for connections, slow queries, and failed logins
- **Historical Analysis** - Track previous blocking sessions and performance trends
- **Index Fragmentation Analysis** - Advanced index optimization with customizable thresholds
- **Better Organization** - Action-based approach for cleaner tool usage

### **Quick Start Checklist**
- [ ] Install Python 3.8+
- [ ] Install ODBC Driver 17 for SQL Server
- [ ] Clone/download project files
- [ ] Run installation script or manual setup
- [ ] Configure .env file with database details
- [ ] Test database connection
- [ ] Configure Claude Desktop
- [ ] Start using 9 powerful database tools with 41 actions!

**Ready to get started?** Follow the installation guide above and unlock the full power of your SQL Server database with enhanced AI assistance! 🚀