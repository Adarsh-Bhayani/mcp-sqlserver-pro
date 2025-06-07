# MSSQL MCP Server

A Model Context Protocol (MCP) server that provides comprehensive access to Microsoft SQL Server databases. This enhanced server enables Language Models to inspect database schemas, execute queries, manage database objects, and perform advanced database operations through a standardized interface.

## 🚀 Enhanced Features

### **Complete Database Schema Traversal**
- **23 comprehensive database management tools** (expanded from 5 basic operations)
- **Full database object hierarchy exploration** - tables, views, stored procedures, indexes, schemas
- **Advanced database object management** - create, modify, delete operations
- **Intelligent resource access** - all tables and views available as MCP resources

### **Core Capabilities**
- **Database Connection**: Connect to MSSQL Server instances with flexible authentication
- **Schema Inspection**: Complete database object exploration and management
- **Query Execution**: Execute SELECT, INSERT, UPDATE, DELETE, and DDL queries
- **Stored Procedure Management**: Create, modify, execute, and manage stored procedures
- **View Management**: Create, modify, delete, and describe views
- **Index Management**: Create, delete, and analyze indexes
- **Resource Access**: Browse table and view data as MCP resources
- **Security**: Read-only and write operations are properly separated and validated

## ⚠️ Important Usage Guidelines for Engineering Teams

### **Database Limitation**
**🔴 CRITICAL: Limit to ONE database per MCP server instance**

- This enhanced MCP server creates **up to 23 tools per database**
- Cursor has a **40-tool limit** across all MCP servers
- Using multiple database instances will exceed Cursor's tool limit
- For multiple databases, use separate MCP server instances in different projects

### **Tool Distribution**
- **Core Tools**: 5 (read_query, write_query, list_tables, describe_table, create_table)
- **Stored Procedures**: 6 tools (create, modify, delete, list, describe, execute, get_parameters)
- **Views**: 5 tools (create, modify, delete, list, describe)
- **Indexes**: 4 tools (create, delete, list, describe)
- **Schema Management**: 2 tools (list_schemas, list_all_objects)
- **Enhanced write_query**: Supports all database object operations

## Installation

### Prerequisites

- Python 3.10 or higher
- ODBC Driver 17 for SQL Server
- Access to an MSSQL Server instance

### Quick Setup

1. **Clone or create the project directory:**
   ```bash
   mkdir mcp-sqlserver && cd mcp-sqlserver
   ```

2. **Run the installation script:**
   ```bash
   chmod +x install.sh
   ./install.sh
   ```

3. **Configure your database connection:**
   ```bash
   cp env.example .env
   # Edit .env with your database details
   ```

### Manual Installation

1. **Create virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install ODBC Driver (macOS):**
   ```bash
   brew tap microsoft/mssql-release
   brew install msodbcsql17 mssql-tools
   ```

## Configuration

Create a `.env` file with your database configuration:

```env
MSSQL_DRIVER={ODBC Driver 17 for SQL Server}
MSSQL_SERVER=your-server-address
MSSQL_DATABASE=your-database-name
MSSQL_USER=your-username
MSSQL_PASSWORD=your-password
MSSQL_PORT=1433
TrustServerCertificate=yes
```

### Configuration Options

- `MSSQL_SERVER`: Server hostname or IP address (required)
- `MSSQL_DATABASE`: Database name to connect to (required)
- `MSSQL_USER`: Username for authentication
- `MSSQL_PASSWORD`: Password for authentication
- `MSSQL_PORT`: Port number (default: 1433)
- `MSSQL_DRIVER`: ODBC driver name (default: {ODBC Driver 17 for SQL Server})
- `TrustServerCertificate`: Trust server certificate (default: yes)
- `Trusted_Connection`: Use Windows authentication (default: no)

## Usage

### Understanding MCP Servers

MCP (Model Context Protocol) servers are designed to work with AI assistants and language models. They communicate via stdin/stdout using JSON-RPC protocol, not as traditional web services.

### Running the Server

**For AI Assistant Integration:**
```bash
python3 src/server.py
```

The server will start and wait for MCP protocol messages on stdin. This is how AI assistants like Claude Desktop or other MCP clients will communicate with it.

**For Testing and Development:**

1. **Test database connection:**
   ```bash
   python3 test_connection.py
   ```

2. **Check server status:**
   ```bash
   ./status.sh
   ```

3. **View available tables:**
   ```bash
   # The server provides tools that can be called by MCP clients
   # Direct testing requires an MCP client or testing framework
   ```

### Available Tools (23 Total)

The enhanced server provides comprehensive database management tools:

#### **Core Database Operations (5 tools)**
1. **`read_query`** - Execute SELECT queries to read data
2. **`write_query`** - Execute INSERT, UPDATE, DELETE, and DDL queries
3. **`list_tables`** - List all tables in the database
4. **`describe_table`** - Get schema information for a specific table
5. **`create_table`** - Create new tables

#### **Stored Procedure Management (6 tools)**
6. **`create_procedure`** - Create new stored procedures
7. **`modify_procedure`** - Modify existing stored procedures
8. **`delete_procedure`** - Delete stored procedures
9. **`list_procedures`** - List all stored procedures with metadata
10. **`describe_procedure`** - Get complete procedure definitions
11. **`execute_procedure`** - Execute procedures with parameters
12. **`get_procedure_parameters`** - Get detailed parameter information

#### **View Management (5 tools)**
13. **`create_view`** - Create new views
14. **`modify_view`** - Modify existing views
15. **`delete_view`** - Delete views
16. **`list_views`** - List all views in the database
17. **`describe_view`** - Get view definitions and schema

#### **Index Management (4 tools)**
18. **`create_index`** - Create new indexes
19. **`delete_index`** - Delete indexes
20. **`list_indexes`** - List all indexes (optionally by table)
21. **`describe_index`** - Get detailed index information

#### **Schema Exploration (2 tools)**
22. **`list_schemas`** - List all schemas in the database
23. **`list_all_objects`** - List all database objects organized by schema

### Available Resources

Both tables and views are exposed as MCP resources with URIs like:
- `mssql://table_name/data` - Access table data in CSV format
- `mssql://view_name/data` - Access view data in CSV format

Resources provide the first 100 rows of data in CSV format for quick data exploration.

## Integration with AI Assistants

### Claude Desktop

Add this server to your Claude Desktop configuration:

```json
{
  "mcpServers": {
    "mssql": {
      "command": "python3",
      "args": ["/path/to/mcp-sqlserver/src/server.py"],
      "cwd": "/path/to/mcp-sqlserver",
      "env": {
        "MSSQL_SERVER": "your-server",
        "MSSQL_DATABASE": "your-database",
        "MSSQL_USER": "your-username",
        "MSSQL_PASSWORD": "your-password"
      }
    }
  }
}
```

### Other MCP Clients

The server follows the standard MCP protocol and should work with any compliant MCP client.

## Development

### Project Structure

```
mcp-sqlserver/
├── src/
│   └── server.py          # Main MCP server implementation
├── tests/
│   └── test_server.py     # Unit tests
├── requirements.txt       # Python dependencies
├── .env                   # Database configuration (create from env.example)
├── env.example           # Configuration template
├── install.sh            # Installation script
├── start.sh              # Server startup script (for development)
├── stop.sh               # Server shutdown script
├── status.sh             # Server status script
└── README.md             # This file
```

### Testing

Run the test suite:
```bash
python -m pytest tests/
```

Test database connection:
```bash
python3 test_connection.py
```

### Logging

The server uses Python's logging module. Set the log level by modifying the `logging.basicConfig()` call in `src/server.py`.

## Security Considerations

- **Authentication**: Always use strong passwords and secure authentication
- **Network**: Ensure your database server is properly secured
- **Permissions**: Grant only necessary database permissions to the user account
- **SSL/TLS**: Use encrypted connections when possible
- **Query Validation**: The server validates query types and prevents unauthorized operations
- **DDL Operations**: Create/modify/delete operations for database objects are properly validated
- **Stored Procedure Execution**: Parameters are safely handled to prevent injection attacks
- **Read-First Approach**: Exploration tools are read-only by default for production safety

## Troubleshooting

### Common Issues

1. **Connection Failed**: Check your database server address, credentials, and network connectivity
2. **ODBC Driver Not Found**: Install Microsoft ODBC Driver 17 for SQL Server
3. **Permission Denied**: Ensure the database user has appropriate permissions
4. **Port Issues**: Verify the correct port number and firewall settings

### Debug Mode

Enable debug logging by setting the log level to DEBUG in `src/server.py`:

```python
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
```

### Getting Help

1. Check the server logs for detailed error messages
2. Verify your `.env` configuration
3. Test the database connection independently
4. Ensure all dependencies are installed correctly

## License

This project is open source. See the license file for details.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests. 