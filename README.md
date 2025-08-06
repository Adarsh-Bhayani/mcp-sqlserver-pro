# 🚀 MCP SQL Server Pro - Simplified Database Management Server

A streamlined Model Context Protocol (MCP) server that provides direct SQL query access to Microsoft SQL Server databases. This simplified version focuses on essential database operations with a clean, reliable interface for AI assistants and Language Models.

## 📋 Table of Contents

- [🌟 Key Features](#-key-features)
- [🛠️ Complete Setup Guide](#️-complete-setup-guide)
- [⚙️ Configuration](#️-configuration)
- [🔧 Available Tools](#-available-tools)
- [🎯 SQL Operation Prompt Guide](#-sql-operation-prompt-guide)
- [💡 Usage Examples](#-usage-examples)
- [🤖 AI Assistant Integration](#-ai-assistant-integration)
- [🔒 Security & Best Practices](#-security--best-practices)
- [🐛 Troubleshooting](#-troubleshooting)

## 🌟 Key Features

### **🎯 Simplified Database Management**
- **Single Powerful Tool** - One unified database tool with 4 core operations (CREATE, READ, UPDATE, DELETE)
- **Direct SQL Execution** - Execute raw SQL queries without complex abstractions
- **Streamlined Architecture** - Clean, maintainable codebase focused on essential functionality
- **Comprehensive Operations** - Full CRUD operations plus DDL (Data Definition Language) support

### **🔧 Core Capabilities**
- **Query Execution** - SELECT queries for data retrieval
- **Data Modification** - INSERT, UPDATE, DELETE operations
- **Object Creation** - CREATE tables, indexes, views, procedures, functions
- **Schema Management** - ALTER and DROP operations for database objects
- **Advanced Analytics** - Complex queries for performance monitoring and analysis

### **⚡ Technical Highlights**
- **Secure Operations** - Proper query validation and error handling
- **Efficient Processing** - Direct SQL execution without overhead
- **Flexible Authentication** - Windows Authentication or SQL Server Authentication
- **Comprehensive Error Reporting** - Detailed error messages and validation
- **Connection Management** - Automatic connection handling and cleanup

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
- **ODBC Driver 18 for SQL Server** (critical requirement)
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
   ```

### **ODBC Driver Installation**

The ODBC Driver 18 for SQL Server is **critical** for database connectivity.

#### **Windows**
1. Download from [Microsoft Download Center](https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server)
2. Run the installer as Administrator
3. Follow installation wizard

#### **macOS**
```bash
# Using Homebrew
brew tap microsoft/mssql-release
brew install msodbcsql18 mssql-tools18

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
sudo ACCEPT_EULA=Y apt-get install -y msodbcsql18 mssql-tools18
```

#### **Linux (Red Hat/CentOS)**
```bash
# Add Microsoft repository
sudo curl -o /etc/yum.repos.d/msprod.repo https://packages.microsoft.com/config/rhel/8/prod.repo

# Install driver
sudo ACCEPT_EULA=Y yum install -y msodbcsql18 mssql-tools18
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
   AUTH_METHOD=sql
   
   # Method 2: Windows Authentication
   AUTH_METHOD=windows
   # (leave MSSQL_USER and MSSQL_PASSWORD empty)
   
   # Optional Settings
MSSQL_PORT=1433
   MSSQL_DRIVER={ODBC Driver 18 for SQL Server}
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
AUTH_METHOD=sql
TrustServerCertificate=yes
```

#### **Remote SQL Server with Windows Auth**
```env
MSSQL_SERVER=sql-server.company.com
MSSQL_DATABASE=ProductionDB
MSSQL_PORT=1433
AUTH_METHOD=windows
TrustServerCertificate=yes
```

#### **Azure SQL Database**
```env
MSSQL_SERVER=your-server.database.windows.net
MSSQL_DATABASE=your-database
MSSQL_USER=your-username@your-server
MSSQL_PASSWORD=your-password
MSSQL_PORT=1433
AUTH_METHOD=sql
TrustServerCertificate=yes
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
driver = os.getenv('MSSQL_DRIVER', '{ODBC Driver 18 for SQL Server}')
server = os.getenv('MSSQL_SERVER')
database = os.getenv('MSSQL_DATABASE')
username = os.getenv('MSSQL_USER', '')
password = os.getenv('MSSQL_PASSWORD', '')
port = os.getenv('MSSQL_PORT', '1433')
trust_cert = os.getenv('TrustServerCertificate', 'yes')
auth_method = os.getenv('AUTH_METHOD', 'sql')

conn_str = f'DRIVER={driver};SERVER={server},{port};DATABASE={database};'
if auth_method == 'sql' and username and password:
    conn_str += f'UID={username};PWD={password};Trusted_Connection=no;'
else:
    conn_str += f'Trusted_Connection=yes;'
conn_str += f'TrustServerCertificate={trust_cert};'

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

## 🔧 Available Tools

MCP SQL Server Pro provides **1 powerful database tool with 4 core operations**:

### **📊 Database Tool**
**Execute all SQL operations with comprehensive CRUD support**

| Operation | Description | Use Cases |
|-----------|-------------|-----------|
| `CREATE` | Execute CREATE statements | Tables, indexes, views, procedures, functions, schemas |
| `READ` | Execute SELECT queries | Data retrieval, analysis, reporting |
| `UPDATE` | Execute UPDATE/INSERT statements | Data modification, bulk operations |
| `DELETE` | Execute DELETE statements | Data removal, cleanup operations |

**Tool Schema:**
```json
{
  "name": "database",
  "description": "Perform database operations: CREATE (tables/indexes), READ (SELECT), UPDATE (modify data), DELETE (remove data)",
  "inputSchema": {
    "type": "object",
    "properties": {
      "operation": {
        "type": "string",
        "description": "Database operation to perform",
        "enum": ["CREATE", "READ", "UPDATE", "DELETE"]
      },
      "sql": {
        "type": "string",
        "description": "SQL query to execute"
      }
    },
    "required": ["operation", "sql"]
  }
}
```

## 🎯 SQL Operation Prompt Guide

This section provides comprehensive prompts and examples for all SQL operations you can perform with the MCP SQL Server Pro.

### **📖 READ Operations (SELECT Queries)**

#### **Basic Data Retrieval**
```
Please show me all customers from the database.
```
*Translates to:*
```json
{
  "tool": "database",
  "parameters": {
    "operation": "READ",
    "sql": "SELECT * FROM Customers"
  }
}
```

#### **Filtered Data Queries**
```
Show me all orders from the last 30 days with customer information.
```
*Translates to:*
```json
{
  "tool": "database",
  "parameters": {
    "operation": "READ",
    "sql": "SELECT o.OrderID, o.OrderDate, c.CustomerName, o.TotalAmount FROM Orders o JOIN Customers c ON o.CustomerID = c.CustomerID WHERE o.OrderDate >= DATEADD(DAY, -30, GETDATE())"
  }
}
```

#### **Aggregation and Analytics**
```
Give me sales summary by month for the current year.
```
*Translates to:*
```json
{
  "tool": "database",
  "parameters": {
    "operation": "READ",
    "sql": "SELECT YEAR(OrderDate) as Year, MONTH(OrderDate) as Month, COUNT(*) as OrderCount, SUM(TotalAmount) as TotalSales FROM Orders WHERE YEAR(OrderDate) = YEAR(GETDATE()) GROUP BY YEAR(OrderDate), MONTH(OrderDate) ORDER BY Month"
  }
}
```

#### **Performance Analysis Queries**
```
Show me the most fragmented indexes in the database.
```
*Translates to:*
```json
{
  "tool": "database",
  "parameters": {
    "operation": "READ",
    "sql": "SELECT OBJECT_SCHEMA_NAME(ips.object_id) AS SchemaName, OBJECT_NAME(ips.object_id) AS TableName, i.name AS IndexName, ips.avg_fragmentation_in_percent FROM sys.dm_db_index_physical_stats(DB_ID(), NULL, NULL, NULL, 'LIMITED') ips INNER JOIN sys.indexes i ON ips.object_id = i.object_id AND ips.index_id = i.index_id WHERE ips.avg_fragmentation_in_percent > 10 ORDER BY ips.avg_fragmentation_in_percent DESC"
  }
}
```

#### **System Information Queries**
```
Show me database size and file information.
```
*Translates to:*
```json
{
  "tool": "database",
  "parameters": {
    "operation": "READ",
    "sql": "SELECT name AS FileName, size * 8.0 / 1024 AS SizeMB, CASE WHEN max_size = -1 THEN 'Unlimited' ELSE CAST(max_size * 8.0 / 1024 AS VARCHAR(20)) + ' MB' END AS MaxSize FROM sys.master_files WHERE database_id = DB_ID()"
  }
}
```

### **✏️ UPDATE Operations (INSERT/UPDATE Queries)**

#### **Insert New Records**
```
Add a new customer named 'John Doe' from New York, USA.
```
*Translates to:*
```json
{
  "tool": "database",
  "parameters": {
    "operation": "UPDATE",
    "sql": "INSERT INTO Customers (CustomerName, City, Country) VALUES ('John Doe', 'New York', 'USA')"
  }
}
```

#### **Update Existing Records**
```
Update the email address for customer ID 123 to 'newemail@example.com'.
```
*Translates to:*
```json
{
  "tool": "database",
  "parameters": {
    "operation": "UPDATE",
    "sql": "UPDATE Customers SET Email = 'newemail@example.com' WHERE CustomerID = 123"
  }
}
```

#### **Bulk Data Operations**
```
Update all product prices by increasing them by 5%.
```
*Translates to:*
```json
{
  "tool": "database",
  "parameters": {
    "operation": "UPDATE",
    "sql": "UPDATE Products SET Price = Price * 1.05"
  }
}
```

#### **Complex Insert with Joins**
```
Insert order details for all products in category 'Electronics' for customer ID 456.
```
*Translates to:*
```json
{
  "tool": "database",
  "parameters": {
    "operation": "UPDATE",
    "sql": "INSERT INTO OrderDetails (OrderID, ProductID, Quantity, UnitPrice) SELECT 1001, ProductID, 1, Price FROM Products WHERE Category = 'Electronics'"
  }
}
```

### **🗑️ DELETE Operations**

#### **Delete Specific Records**
```
Delete the customer with ID 789.
```
*Translates to:*
```json
{
  "tool": "database",
  "parameters": {
    "operation": "DELETE",
    "sql": "DELETE FROM Customers WHERE CustomerID = 789"
  }
}
```

#### **Conditional Deletion**
```
Delete all orders older than 2 years.
```
*Translates to:*
```json
{
  "tool": "database",
  "parameters": {
    "operation": "DELETE",
    "sql": "DELETE FROM Orders WHERE OrderDate < DATEADD(YEAR, -2, GETDATE())"
  }
}
```

#### **Cascade Deletion with Cleanup**
```
Delete all order details for cancelled orders.
```
*Translates to:*
```json
{
  "tool": "database",
  "parameters": {
    "operation": "DELETE",
    "sql": "DELETE od FROM OrderDetails od INNER JOIN Orders o ON od.OrderID = o.OrderID WHERE o.Status = 'Cancelled'"
  }
}
```

### **🏗️ CREATE Operations (DDL Statements)**

#### **Create Tables**
```
Create a new table called 'ProductReviews' with columns for ReviewID, ProductID, CustomerID, Rating, and Comment.
```
*Translates to:*
```json
{
  "tool": "database",
  "parameters": {
    "operation": "CREATE",
    "sql": "CREATE TABLE ProductReviews (ReviewID INT IDENTITY(1,1) PRIMARY KEY, ProductID INT NOT NULL, CustomerID INT NOT NULL, Rating INT CHECK (Rating >= 1 AND Rating <= 5), Comment NVARCHAR(1000), ReviewDate DATETIME DEFAULT GETDATE(), FOREIGN KEY (ProductID) REFERENCES Products(ProductID), FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID))"
  }
}
```

#### **Create Indexes**
```
Create an index on the Orders table for OrderDate and CustomerID columns.
```
*Translates to:*
```json
{
  "tool": "database",
  "parameters": {
    "operation": "CREATE",
    "sql": "CREATE INDEX IX_Orders_OrderDate_CustomerID ON Orders (OrderDate, CustomerID)"
  }
}
```

#### **Create Views**
```
Create a view that shows customer order summary with total orders and total spent.
```
*Translates to:*
```json
{
  "tool": "database",
  "parameters": {
    "operation": "CREATE",
    "sql": "CREATE VIEW vw_CustomerOrderSummary AS SELECT c.CustomerID, c.CustomerName, COUNT(o.OrderID) as TotalOrders, SUM(o.TotalAmount) as TotalSpent, MAX(o.OrderDate) as LastOrderDate FROM Customers c LEFT JOIN Orders o ON c.CustomerID = o.CustomerID GROUP BY c.CustomerID, c.CustomerName"
  }
}
```

#### **Create Stored Procedures**
```
Create a stored procedure to get customer orders within a date range.
```
*Translates to:*
```json
{
  "tool": "database",
  "parameters": {
    "operation": "CREATE",
    "sql": "CREATE PROCEDURE GetCustomerOrdersByDateRange @CustomerID INT, @StartDate DATE, @EndDate DATE AS BEGIN SELECT o.OrderID, o.OrderDate, o.TotalAmount, o.Status FROM Orders o WHERE o.CustomerID = @CustomerID AND o.OrderDate BETWEEN @StartDate AND @EndDate ORDER BY o.OrderDate DESC END"
  }
}
```

#### **Create Functions**
```
Create a function to calculate the total order amount including tax.
```
*Translates to:*
```json
{
  "tool": "database",
  "parameters": {
    "operation": "CREATE",
    "sql": "CREATE FUNCTION dbo.CalculateOrderTotalWithTax(@OrderID INT, @TaxRate DECIMAL(5,4)) RETURNS DECIMAL(10,2) AS BEGIN DECLARE @Total DECIMAL(10,2) SELECT @Total = SUM(Quantity * UnitPrice) FROM OrderDetails WHERE OrderID = @OrderID RETURN @Total * (1 + @TaxRate) END"
  }
}
```

### **🔧 Advanced Operations**

#### **Database Maintenance**
```
Rebuild all fragmented indexes with fragmentation over 30%.
```
*Translates to:*
```json
{
  "tool": "database",
  "parameters": {
    "operation": "CREATE",
    "sql": "DECLARE @sql NVARCHAR(1000) DECLARE index_cursor CURSOR FOR SELECT 'ALTER INDEX [' + i.name + '] ON [' + OBJECT_SCHEMA_NAME(ips.object_id) + '].[' + OBJECT_NAME(ips.object_id) + '] REBUILD' FROM sys.dm_db_index_physical_stats(DB_ID(), NULL, NULL, NULL, 'LIMITED') ips INNER JOIN sys.indexes i ON ips.object_id = i.object_id AND ips.index_id = i.index_id WHERE ips.avg_fragmentation_in_percent > 30 OPEN index_cursor FETCH NEXT FROM index_cursor INTO @sql WHILE @@FETCH_STATUS = 0 BEGIN EXEC sp_executesql @sql FETCH NEXT FROM index_cursor INTO @sql END CLOSE index_cursor DEALLOCATE index_cursor"
  }
}
```

#### **Performance Monitoring**
```
Show me the top 10 slowest queries in the system.
```
*Translates to:*
```json
{
  "tool": "database",
  "parameters": {
    "operation": "READ",
    "sql": "SELECT TOP 10 qs.total_elapsed_time / qs.execution_count / 1000.0 AS avg_elapsed_time_ms, qs.execution_count, SUBSTRING(st.text, (qs.statement_start_offset/2)+1, ((CASE qs.statement_end_offset WHEN -1 THEN DATALENGTH(st.text) ELSE qs.statement_end_offset END - qs.statement_start_offset)/2) + 1) AS query_text FROM sys.dm_exec_query_stats qs CROSS APPLY sys.dm_exec_sql_text(qs.sql_handle) st ORDER BY avg_elapsed_time_ms DESC"
  }
}
```

#### **Security Analysis**
```
Show me all user permissions in the current database.
```
*Translates to:*
```json
{
  "tool": "database",
  "parameters": {
    "operation": "READ",
    "sql": "SELECT p.state_desc, p.permission_name, s.name AS principal_name, o.name AS object_name FROM sys.database_permissions p LEFT JOIN sys.objects o ON p.major_id = o.object_id LEFT JOIN sys.database_principals s ON p.grantee_principal_id = s.principal_id WHERE s.name IS NOT NULL ORDER BY s.name, p.permission_name"
  }
}
```

### **💡 Prompt Tips for Better Results**

#### **Be Specific About Your Needs**
- ❌ "Show me some data"
- ✅ "Show me the top 10 customers by total order value in 2024"

#### **Specify Data Ranges**
- ❌ "Show recent orders"
- ✅ "Show orders from the last 7 days"

#### **Include Business Context**
- ❌ "Update the table"
- ✅ "Update product prices for items in the Electronics category, increasing by 10%"

#### **Request Specific Columns**
- ❌ "Get customer info"
- ✅ "Get customer name, email, and total orders for customers who placed orders in the last month"

#### **Use Clear Filtering Criteria**
- ❌ "Delete old data"
- ✅ "Delete log entries older than 90 days from the audit table"

## 💡 Usage Examples

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
  "tool": "database",
  "parameters": {
    "operation": "READ",
    "sql": "SELECT TOP 10 * FROM Customers ORDER BY CustomerID"
  }
}
```

#### **Insert Data**
```json
{
  "tool": "database",
  "parameters": {
    "operation": "UPDATE",
    "sql": "INSERT INTO Customers (CustomerName, City, Country) VALUES ('New Customer', 'New York', 'USA')"
  }
}
```

#### **Create Database Objects**
```json
{
  "tool": "database",
  "parameters": {
    "operation": "CREATE",
    "sql": "CREATE TABLE TestTable (ID INT IDENTITY(1,1) PRIMARY KEY, Name NVARCHAR(100) NOT NULL, CreatedDate DATETIME DEFAULT GETDATE())"
  }
}
```

### **🗃️ Advanced Operations**

#### **Complex Analytics Query**
```json
{
  "tool": "database",
  "parameters": {
    "operation": "READ",
    "sql": "WITH MonthlySales AS (SELECT YEAR(OrderDate) as Year, MONTH(OrderDate) as Month, SUM(TotalAmount) as Sales FROM Orders GROUP BY YEAR(OrderDate), MONTH(OrderDate)) SELECT Year, Month, Sales, LAG(Sales) OVER (ORDER BY Year, Month) as PreviousMonth, Sales - LAG(Sales) OVER (ORDER BY Year, Month) as Growth FROM MonthlySales ORDER BY Year, Month"
  }
}
```

#### **Database Maintenance**
```json
{
  "tool": "database",
  "parameters": {
    "operation": "CREATE",
    "sql": "UPDATE STATISTICS Customers WITH FULLSCAN"
  }
}
```

#### **Performance Analysis**
```json
{
  "tool": "database",
  "parameters": {
    "operation": "READ",
    "sql": "SELECT wait_type, wait_time_ms, waiting_tasks_count, signal_wait_time_ms FROM sys.dm_os_wait_stats WHERE wait_time_ms > 0 ORDER BY wait_time_ms DESC"
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
        "AUTH_METHOD": "sql",
        "TrustServerCertificate": "yes"
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
    "mssql": {
      "command": "python",
      "args": ["C:\\Users\\YourUsername\\Desktop\\mcp-sqlserver-pro\\src\\server.py"],
      "cwd": "C:\\Users\\YourUsername\\Desktop\\mcp-sqlserver-pro",
      "env": {
        "MSSQL_SERVER": "SF-CPU-505",
        "MSSQL_DATABASE": "Contoso",
        "MSSQL_USER": "sa",
        "MSSQL_PASSWORD": "YourPassword"
      }
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
   Can you analyze the database performance and show me any fragmented indexes?
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
AUTH_METHOD=sql
TrustServerCertificate=no  # Use valid certificates in production
```

### **🚫 Built-in Security Features**

The server includes comprehensive security measures:

- **Query Type Validation**: Only allows appropriate queries for each operation type
- **SQL Injection Prevention**: Uses parameterized queries and input validation
- **Connection Security**: Secure connection string handling and timeout management
- **Error Handling**: Prevents sensitive information leakage in error messages
- **Input Sanitization**: Validates all input parameters before execution

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
# ['ODBC Driver 18 for SQL Server', ...]
```

**If ODBC driver is missing:**
- **Windows**: Download and install from Microsoft
- **macOS**: `brew install msodbcsql18`
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
2. **Use index analysis queries**
3. **Monitor wait statistics**
4. **Analyze blocking sessions**

### **🔍 Debugging Steps**

#### **1. Basic Connectivity Test**
```python
import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

# Test basic connection
try:
    conn_str = f"DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={os.getenv('MSSQL_SERVER')};DATABASE={os.getenv('MSSQL_DATABASE')};UID={os.getenv('MSSQL_USER')};PWD={os.getenv('MSSQL_PASSWORD')}"
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
# INFO - Simplified server initialized, starting...
# INFO - Simplified server streams established
```

#### **3. Tool Availability Test**
After connecting through Claude Desktop:
```
Please test the database tool by showing me the current database version.
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
INFO - Simplified server initialized, starting...  # Normal startup
ERROR - Database connection failed                 # Connection issue
DEBUG - Executing tool: database                   # Tool execution
ERROR - Error executing tool database              # Tool error
```

---

## 📋 Summary

MCP SQL Server Pro provides streamlined database management capabilities through **1 powerful database tool with 4 core operations** (CREATE, READ, UPDATE, DELETE), making it the most straightforward and reliable MCP server for Microsoft SQL Server integration.

### **Key Benefits**
- ✅ **Simplified Architecture** - One tool, four operations, maximum clarity
- ✅ **Direct SQL Execution** - No abstractions, just pure SQL power
- ✅ **Complete Database Management** - All CRUD and DDL operations supported
- ✅ **Professional Security** - Built-in validation and security measures
- ✅ **Easy Setup** - Comprehensive installation guide for any platform
- ✅ **AI Integration** - Seamless integration with Claude Desktop and other MCP clients

### **🆕 What's New in This Simplified Version**
- **Streamlined Architecture** - Reduced complexity while maintaining full functionality
- **Direct SQL Access** - Execute any SQL query directly without tool abstractions
- **Better Error Handling** - Comprehensive error reporting and validation
- **Improved Security** - Enhanced input validation and connection security
- **Cleaner Codebase** - Maintainable, readable code structure

### **Quick Start Checklist**
- [ ] Install Python 3.8+
- [ ] Install ODBC Driver 18 for SQL Server
- [ ] Clone/download project files
- [ ] Run installation script or manual setup
- [ ] Configure .env file with database details
- [ ] Test database connection
- [ ] Configure Claude Desktop
- [ ] Start using the powerful database tool with direct SQL access!

**Ready to get started?** Follow the installation guide above and unlock the full power of your SQL Server database with enhanced AI assistance! 🚀

## 📚 Additional Resources

### **SQL Reference Guides**
- [Microsoft SQL Server Documentation](https://docs.microsoft.com/en-us/sql/sql-server/)
- [T-SQL Reference](https://docs.microsoft.com/en-us/sql/t-sql/)
- [SQL Server Performance Tuning](https://docs.microsoft.com/en-us/sql/relational-databases/performance/)

### **MCP Protocol**
- [Model Context Protocol Specification](https://modelcontextprotocol.io/)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)

### **Community & Support**
- Report issues on GitHub
- Join the MCP community discussions
- Contribute to the project development

---

*Last updated: August 2025*