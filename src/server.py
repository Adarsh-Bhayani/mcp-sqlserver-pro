#!/usr/bin/env python3
"""
MSSQL MCP Server

A Model Context Protocol server that provides access to Microsoft SQL Server databases.
Enables Language Models to inspect table schemas and execute SQL queries.
"""

import asyncio
import logging
import os
import sys
import traceback
from typing import Any, Dict, List, Optional, Sequence
from urllib.parse import urlparse

import pyodbc
from dotenv import load_dotenv
from mcp.server import Server, NotificationOptions
from mcp.server.models import InitializationOptions
from mcp.server.stdio import stdio_server
from mcp.types import (
    Resource,
    Tool,
    TextContent,
    ImageContent,
    EmbeddedResource,
    LoggingLevel
)
from pydantic import AnyUrl

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("mssql-mcp-server")

class MSSQLServer:
    def __init__(self):
        self.connection_string = self._build_connection_string()
        self.server = Server("mssql-mcp-server")
        self._setup_handlers()

    def _build_connection_string(self) -> str:
        """Build MSSQL connection string from environment variables."""
        driver = os.getenv("MSSQL_DRIVER", "{ODBC Driver 17 for SQL Server}")
        server = os.getenv("MSSQL_SERVER", "localhost")
        database = os.getenv("MSSQL_DATABASE", "")
        username = os.getenv("MSSQL_USER", "")
        password = os.getenv("MSSQL_PASSWORD", "")
        port = os.getenv("MSSQL_PORT", "1433")
        trust_cert = os.getenv("TrustServerCertificate", "yes")
        trusted_conn = os.getenv("Trusted_Connection", "no")

        if not all([server, database]):
            raise ValueError("MSSQL_SERVER and MSSQL_DATABASE must be set")

        conn_str = f"DRIVER={driver};SERVER={server},{port};DATABASE={database};"
        
        if username and password:
            conn_str += f"UID={username};PWD={password};"
        
        conn_str += f"TrustServerCertificate={trust_cert};Trusted_Connection={trusted_conn};"
        
        return conn_str

    def _get_connection(self):
        """Get database connection."""
        try:
            return pyodbc.connect(self.connection_string)
        except Exception as e:
            logger.error(f"Failed to connect to database: {e}")
            raise

    def _setup_handlers(self):
        """Set up MCP handlers."""
        
        @self.server.list_resources()
        async def list_resources() -> List[Resource]:
            """List all available database tables as resources."""
            try:
                with self._get_connection() as conn:
                    cursor = conn.cursor()
                    cursor.execute("""
                        SELECT TABLE_NAME 
                        FROM INFORMATION_SCHEMA.TABLES 
                        WHERE TABLE_TYPE = 'BASE TABLE'
                        ORDER BY TABLE_NAME
                    """)
                    tables = cursor.fetchall()
                    
                    resources = []
                    for table in tables:
                        table_name = table[0]
                        resources.append(Resource(
                            uri=AnyUrl(f"mssql://{table_name}/data"),
                            name=f"Table: {table_name}",
                            description=f"Data from {table_name} table",
                            mimeType="text/csv"
                        ))
                    
                    return resources
            except Exception as e:
                logger.error(f"Error listing resources: {e}")
                return []

        @self.server.read_resource()
        async def read_resource(uri: AnyUrl) -> str:
            """Read data from a specific table."""
            try:
                # Parse the URI to get table name
                parsed = urlparse(str(uri))
                if parsed.scheme != "mssql":
                    raise ValueError("Invalid URI scheme")
                
                table_name = parsed.netloc
                if not table_name:
                    raise ValueError("Table name not specified in URI")

                with self._get_connection() as conn:
                    cursor = conn.cursor()
                    # Get first 100 rows
                    cursor.execute(f"SELECT TOP 100 * FROM [{table_name}]")
                    rows = cursor.fetchall()
                    
                    if not rows:
                        return "No data found"
                    
                    # Get column names
                    columns = [desc[0] for desc in cursor.description]
                    
                    # Format as CSV
                    csv_data = ",".join(columns) + "\n"
                    for row in rows:
                        csv_data += ",".join(str(cell) if cell is not None else "" for cell in row) + "\n"
                    
                    return csv_data
                    
            except Exception as e:
                logger.error(f"Error reading resource {uri}: {e}")
                return f"Error: {str(e)}"

        @self.server.list_tools()
        async def list_tools() -> List[Tool]:
            """List available tools."""
            return [
                Tool(
                    name="read_query",
                    description="Execute a SELECT query to read data from the database",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "SELECT SQL query to execute"
                            }
                        },
                        "required": ["query"]
                    }
                ),
                Tool(
                    name="write_query",
                    description="Execute an INSERT, UPDATE, or DELETE query",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "SQL query to execute (INSERT, UPDATE, DELETE)"
                            }
                        },
                        "required": ["query"]
                    }
                ),
                Tool(
                    name="list_tables",
                    description="List all tables in the database",
                    inputSchema={
                        "type": "object",
                        "properties": {}
                    }
                ),
                Tool(
                    name="describe_table",
                    description="Get schema information for a specific table",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "table_name": {
                                "type": "string",
                                "description": "Name of the table to describe"
                            }
                        },
                        "required": ["table_name"]
                    }
                ),
                Tool(
                    name="create_table",
                    description="Create a new table in the database",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "CREATE TABLE SQL statement"
                            }
                        },
                        "required": ["query"]
                    }
                )
            ]

        @self.server.call_tool()
        async def call_tool(name: str, arguments: Dict[str, Any]) -> List[TextContent]:
            """Execute tool calls."""
            try:
                if name == "read_query":
                    return await self._execute_read_query(arguments["query"])
                elif name == "write_query":
                    return await self._execute_write_query(arguments["query"])
                elif name == "list_tables":
                    return await self._list_tables()
                elif name == "describe_table":
                    return await self._describe_table(arguments["table_name"])
                elif name == "create_table":
                    return await self._create_table(arguments["query"])
                else:
                    raise ValueError(f"Unknown tool: {name}")
            except Exception as e:
                logger.error(f"Error executing tool {name}: {e}")
                return [TextContent(type="text", text=f"Error: {str(e)}")]

    async def _execute_read_query(self, query: str) -> List[TextContent]:
        """Execute a SELECT query."""
        if not query.strip().upper().startswith("SELECT"):
            raise ValueError("Only SELECT queries are allowed for read_query")
        
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            
            if not rows:
                return [TextContent(type="text", text="No results found")]
            
            # Get column names
            columns = [desc[0] for desc in cursor.description]
            
            # Format as CSV
            csv_data = ",".join(columns) + "\n"
            for row in rows:
                csv_data += ",".join(str(cell) if cell is not None else "" for cell in row) + "\n"
            
            return [TextContent(type="text", text=csv_data)]

    async def _execute_write_query(self, query: str) -> List[TextContent]:
        """Execute an INSERT, UPDATE, or DELETE query."""
        query_upper = query.strip().upper()
        if not any(query_upper.startswith(cmd) for cmd in ["INSERT", "UPDATE", "DELETE"]):
            raise ValueError("Only INSERT, UPDATE, and DELETE queries are allowed for write_query")
        
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            affected_rows = cursor.rowcount
            conn.commit()
            
            return [TextContent(type="text", text=f"Query executed successfully. {affected_rows} rows affected.")]

    async def _list_tables(self) -> List[TextContent]:
        """List all tables in the database."""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT TABLE_NAME, TABLE_TYPE
                FROM INFORMATION_SCHEMA.TABLES 
                WHERE TABLE_TYPE = 'BASE TABLE'
                ORDER BY TABLE_NAME
            """)
            tables = cursor.fetchall()
            
            if not tables:
                return [TextContent(type="text", text="No tables found")]
            
            result = "Tables in database:\n"
            for table in tables:
                result += f"- {table[0]} ({table[1]})\n"
            
            return [TextContent(type="text", text=result)]

    async def _describe_table(self, table_name: str) -> List[TextContent]:
        """Get schema information for a table."""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT 
                    COLUMN_NAME,
                    DATA_TYPE,
                    IS_NULLABLE,
                    COLUMN_DEFAULT,
                    CHARACTER_MAXIMUM_LENGTH
                FROM INFORMATION_SCHEMA.COLUMNS 
                WHERE TABLE_NAME = ?
                ORDER BY ORDINAL_POSITION
            """, table_name)
            columns = cursor.fetchall()
            
            if not columns:
                return [TextContent(type="text", text=f"Table '{table_name}' not found")]
            
            result = f"Schema for table '{table_name}':\n"
            result += "Column Name | Data Type | Nullable | Default | Max Length\n"
            result += "-" * 60 + "\n"
            
            for col in columns:
                max_len = str(col[4]) if col[4] else "N/A"
                result += f"{col[0]} | {col[1]} | {col[2]} | {col[3] or 'NULL'} | {max_len}\n"
            
            return [TextContent(type="text", text=result)]

    async def _create_table(self, query: str) -> List[TextContent]:
        """Create a new table."""
        if not query.strip().upper().startswith("CREATE TABLE"):
            raise ValueError("Only CREATE TABLE statements are allowed")
        
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            
            return [TextContent(type="text", text="Table created successfully")]

    async def run(self):
        """Run the MCP server."""
        try:
            logger.info("Starting MCP server...")
            async with stdio_server() as (read_stream, write_stream):
                logger.info("Server streams established")
                await self.server.run(
                    read_stream,
                    write_stream,
                    InitializationOptions(
                        server_name="mssql-mcp-server",
                        server_version="1.0.0",
                        capabilities=self.server.get_capabilities(
                            notification_options=NotificationOptions(),
                            experimental_capabilities=None,
                        ),
                    ),
                )
        except Exception as e:
            logger.error(f"Error in server run: {e}")
            logger.error(f"Traceback: {traceback.format_exc()}")
            raise

async def main():
    """Main entry point."""
    try:
        logger.info("Initializing MSSQL MCP Server...")
        server = MSSQLServer()
        logger.info("Server initialized, starting...")
        await server.run()
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
    except Exception as e:
        logger.error(f"Server error: {e}")
        logger.error(f"Full traceback: {traceback.format_exc()}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main()) 