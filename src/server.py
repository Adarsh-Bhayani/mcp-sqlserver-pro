"""
Simplified MSSQL MCP Server

A streamlined Model Context Protocol server that provides direct SQL query access 
to Microsoft SQL Server databases. No complex dynamic SQL generation - just simple, 
reliable query execution.
"""

import asyncio
import logging
import os
import sys
import traceback
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional, Sequence, Tuple
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
    LoggingLevel,
)
from pydantic import AnyUrl

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("simplified-mssql-mcp-server")


class SimplifiedMSSQLServer:
    """Simplified MSSQL Server with direct SQL query capabilities."""

    def __init__(self):
        self.connection_string = self._build_connection_string()
        self.server = Server("simplified-mssql-mcp-server")
        self._setup_handlers()

    def _build_connection_string(self) -> str:
        """Build MSSQL connection string from environment variables."""
        driver = os.getenv("MSSQL_DRIVER", "{ODBC Driver 18 for SQL Server}")
        server = os.getenv("MSSQL_SERVER", "localhost")
        database = os.getenv("MSSQL_DATABASE", "master")
        username = os.getenv("MSSQL_USER", "")
        password = os.getenv("MSSQL_PASSWORD", "")
        port = os.getenv("MSSQL_PORT", "1433")
        trust_cert = os.getenv("TrustServerCertificate", "yes")
        trusted_conn = os.getenv("Trusted_Connection", "no")
        auth_method = os.getenv("AUTH_METHOD", "sql")

        if not server:
            raise ValueError("MSSQL_SERVER must be set")

        # Build connection string
        conn_str = f"DRIVER={driver};SERVER={server},{port};"

        if database:
            conn_str += f"DATABASE={database};"

        # Authentication method
        if auth_method == "sql" and username and password:
            # SQL Server Authentication
            conn_str += f"UID={username};PWD={password};"
            conn_str += f"Trusted_Connection=no;"
        else:
            # Windows Authentication (default fallback)
            conn_str += f"Trusted_Connection=yes;"

        # Security settings
        conn_str += f"TrustServerCertificate={trust_cert};"

        logger.info(
            f"Connection string configured for: {auth_method} authentication to {server}"
        )
        return conn_str

    def _get_connection(self):
        """Get database connection."""
        try:
            logger.debug("Attempting database connection...")
            connection = pyodbc.connect(self.connection_string)
            logger.info("Database connection established successfully")
            return connection
        except pyodbc.Error as e:
            logger.error(f"Database connection failed: {e}")
            logger.error(
                f"Connection string (sanitized): {self._sanitize_connection_string()}"
            )
            raise
        except Exception as e:
            logger.error(f"Unexpected connection error: {e}")
            raise

    def _sanitize_connection_string(self) -> str:
        """Return connection string with password masked for logging."""
        sanitized = self.connection_string
        if "PWD=" in sanitized:
            import re

            sanitized = re.sub(r"PWD=[^;]*;", "PWD=***;", sanitized)
        return sanitized

    def _setup_handlers(self):
        """Setup MCP handlers with simple query capabilities."""

        @self.server.list_tools()
        async def list_tools() -> List[Tool]:
            """List available simplified tools."""
            return [
                Tool(
                    name="database",
                    description="Perform database operations: CREATE (tables/indexes), READ (SELECT), UPDATE (modify data), DELETE (remove data)",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "operation": {
                                "type": "string",
                                "description": "Database operation to perform",
                                "enum": ["CREATE", "READ", "UPDATE", "DELETE"],
                            },
                            "sql": {
                                "type": "string",
                                "description": "SQL query to execute",
                            },
                        },
                        "required": ["operation", "sql"],
                    },
                ),
            ]

        @self.server.call_tool()
        async def call_tool(name: str, arguments: Dict[str, Any]) -> List[TextContent]:
            """Simple tool execution for direct SQL queries."""
            try:
                logger.info(f"Executing tool: {name} with arguments: {arguments}")

                if name == "database":
                    return await self._execute_database_operation(arguments)
                else:
                    raise ValueError(f"Unknown tool: {name}")

            except Exception as e:
                logger.error(f"Error executing tool {name}: {e}")
                return [TextContent(type="text", text=f"Error: {str(e)}")]

    async def _execute_database_operation(
        self, arguments: Dict[str, Any]
    ) -> List[TextContent]:
        """Execute database CRUD operations."""
        operation = arguments.get("operation")
        sql = arguments.get("sql")

        if not sql:
            return [TextContent(type="text", text="Error: SQL query is required")]

        if not operation:
            return [
                TextContent(
                    type="text",
                    text="Error: Operation is required (CREATE, READ, UPDATE, DELETE)",
                )
            ]

        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()

                if operation == "READ":
                    # Execute SELECT queries
                    cursor.execute(sql)
                    rows = cursor.fetchall()

                    if not rows:
                        return [TextContent(type="text", text="No results returned")]

                    # Get column names
                    columns = [desc[0] for desc in cursor.description]

                    # Format results as CSV
                    result = ",".join(columns) + "\n"
                    for row in rows:
                        result += (
                            ",".join(
                                str(value) if value is not None else "" for value in row
                            )
                            + "\n"
                        )

                    return [TextContent(type="text", text=result.strip())]

                elif operation == "CREATE":
                    # Execute CREATE statements (tables, indexes, views, procedures, etc.)
                    cursor.execute(sql)
                    conn.commit()
                    return [
                        TextContent(
                            type="text",
                            text=f"✅ CREATE operation completed successfully.\n"
                            f"SQL: {sql[:100]}{'...' if len(sql) > 100 else ''}",
                        )
                    ]

                elif operation == "UPDATE":
                    # Execute UPDATE statements
                    cursor.execute(sql)
                    conn.commit()
                    return [
                        TextContent(
                            type="text",
                            text=f"✅ UPDATE operation completed successfully.\n"
                            f"Rows affected: {cursor.rowcount}\n"
                            f"SQL: {sql[:100]}{'...' if len(sql) > 100 else ''}",
                        )
                    ]

                elif operation == "DELETE":
                    # Execute DELETE statements
                    cursor.execute(sql)
                    conn.commit()
                    return [
                        TextContent(
                            type="text",
                            text=f"✅ DELETE operation completed successfully.\n"
                            f"Rows deleted: {cursor.rowcount}\n"
                            f"SQL: {sql[:100]}{'...' if len(sql) > 100 else ''}",
                        )
                    ]

                else:
                    return [
                        TextContent(
                            type="text",
                            text=f"Error: Invalid operation '{operation}'. Use CREATE, READ, UPDATE, or DELETE",
                        )
                    ]

        except Exception as e:
            return [
                TextContent(
                    type="text",
                    text=f"❌ Error executing {operation} operation: {str(e)}\n"
                    f"SQL: {sql[:100]}{'...' if len(sql) > 100 else ''}",
                )
            ]

    async def run(self):
        """Run the server using stdio transport."""
        async with stdio_server() as (read_stream, write_stream):
            logger.info("Simplified server streams established")
            await self.server.run(
                read_stream,
                write_stream,
                InitializationOptions(
                    server_name="simplified-mssql-mcp-server",
                    server_version="1.0.0",
                    capabilities=self.server.get_capabilities(
                        notification_options=NotificationOptions(),
                        experimental_capabilities={},
                    ),
                ),
            )


async def main():
    """Run the simplified MSSQL MCP server."""
    logger.info("Initializing Simplified MSSQL MCP Server...")

    server = SimplifiedMSSQLServer()
    logger.info("Simplified server initialized, starting...")

    # Run the server using stdio transport
    await server.run()


if __name__ == "__main__":
    asyncio.run(main())
