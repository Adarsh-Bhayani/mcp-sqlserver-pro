# MSSQL MCP Server

A Model Context Protocol (MCP) server that provides access to Microsoft SQL Server databases. This server enables Language Models to inspect database schemas, execute queries, and manage data through a standardized interface.

## Features

- **Database Connection**: Connect to MSSQL Server instances with flexible authentication
- **Schema Inspection**: List tables and describe table structures
- **Query Execution**: Execute SELECT, INSERT, UPDATE, DELETE queries
- **Resource Access**: Browse table data as MCP resources
- **Security**: Read-only and write operations are separated into different tools

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

### Available Tools

The server provides these tools for MCP clients:

1. **`list_tables`** - List all tables in the database
2. **`describe_table`** - Get schema information for a specific table
3. **`read_query`** - Execute SELECT queries to read data
4. **`write_query`** - Execute INSERT, UPDATE, DELETE queries
5. **`create_table`** - Create new tables

### Available Resources

Tables are exposed as MCP resources with URIs like:
- `mssql://table_name/data` - Access table data in CSV format

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
- **Query Validation**: The server validates query types to prevent unauthorized operations

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