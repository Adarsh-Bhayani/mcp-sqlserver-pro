# Database Schema Traversal Capabilities

The enhanced MCP server now provides comprehensive database schema traversal capabilities, allowing you to explore and manage all major SQL Server database objects as shown in your SQL Server Management Studio tree structure.

## Complete Database Object Coverage

The MCP server now supports all the major database objects you see in SSMS:

### 📁 **Schemas**
- `list_schemas` - List all schemas in the database
- `list_all_objects` - List all objects organized by schema

### 📊 **Tables** 
- `list_tables` - List all tables in the database
- `describe_table` - Get detailed table schema information
- `create_table` - Create new tables
- Available as MCP resources for data access

### 👁️ **Views**
- `list_views` - List all views in the database
- `describe_view` - Get view definition and schema
- `create_view` - Create new views with T-SQL
- `modify_view` - Alter existing views
- `delete_view` - Drop views
- Available as MCP resources for data access

### ⚙️ **Stored Procedures**
- `list_procedures` - List all stored procedures with metadata
- `describe_procedure` - Get complete procedure definition
- `get_procedure_parameters` - Get detailed parameter information
- `create_procedure` - Create new stored procedures
- `modify_procedure` - Alter existing procedures
- `delete_procedure` - Drop procedures
- `execute_procedure` - Execute procedures with parameters

### 🔍 **Indexes**
- `list_indexes` - List all indexes (optionally filtered by table)
- `describe_index` - Get detailed index information
- `create_index` - Create new indexes
- `delete_index` - Drop indexes

## Schema Traversal Examples

### 1. Explore Database Structure
```
# Start with schemas
list_schemas

# Get all objects in a specific schema
list_all_objects(schema_name: "dbo")

# Or get all objects across all schemas
list_all_objects()
```

### 2. Table Exploration
```
# List all tables
list_tables

# Get detailed table information
describe_table(table_name: "YourTableName")

# Access table data as MCP resource
# URI: mssql://YourTableName/data
```

### 3. View Management
```
# List all views
list_views

# Get view definition
describe_view(view_name: "YourViewName")

# Create a new view
create_view(view_script: "CREATE VIEW MyView AS SELECT * FROM MyTable WHERE Active = 1")

# Access view data as MCP resource
# URI: mssql://YourViewName/data
```

### 4. Stored Procedure Operations
```
# List all procedures
list_procedures

# Get procedure definition
describe_procedure(procedure_name: "YourProcedureName")

# Get parameter details
get_procedure_parameters(procedure_name: "YourProcedureName")

# Execute procedure
execute_procedure(procedure_name: "YourProcedureName", parameters: ["param1", "param2"])
```

### 5. Index Management
```
# List all indexes
list_indexes()

# List indexes for specific table
list_indexes(table_name: "YourTableName")

# Get index details
describe_index(index_name: "IX_YourIndex", table_name: "YourTableName")

# Create new index
create_index(index_script: "CREATE INDEX IX_NewIndex ON MyTable (Column1, Column2)")
```

## Enhanced write_query Tool

The `write_query` tool now supports all database object operations:

### Tables
- `INSERT`, `UPDATE`, `DELETE` statements
- `CREATE TABLE`, `ALTER TABLE`, `DROP TABLE` statements

### Views
- `CREATE VIEW` statements
- `ALTER VIEW` statements  
- `DROP VIEW` statements

### Stored Procedures
- `CREATE PROCEDURE` statements
- `ALTER PROCEDURE` statements
- `DROP PROCEDURE` statements
- `EXEC`/`EXECUTE` statements

### Indexes
- `CREATE INDEX` statements
- `DROP INDEX` statements

## MCP Resources

Both tables and views are now available as MCP resources:

- **Tables**: `mssql://TableName/data` - Returns table data in CSV format
- **Views**: `mssql://ViewName/data` - Returns view data in CSV format

## Complete Database Object Hierarchy

The server now mirrors the complete SQL Server object hierarchy you see in SSMS:

```
Database
├── Schemas
│   ├── dbo
│   ├── custom_schema
│   └── ...
├── Tables
│   ├── Table1
│   ├── Table2
│   └── ...
├── Views
│   ├── View1
│   ├── View2
│   └── ...
├── Stored Procedures
│   ├── Procedure1
│   ├── Procedure2
│   └── ...
└── Indexes
    ├── Table1_Indexes
    ├── Table2_Indexes
    └── ...
```

## Benefits

1. **Complete Schema Visibility**: See and manage all database objects
2. **Hierarchical Navigation**: Explore objects by schema organization
3. **Comprehensive Management**: Create, modify, and delete all object types
4. **Rich Metadata**: Get detailed information about each object
5. **Resource Access**: Direct data access through MCP resources
6. **T-SQL Support**: Full T-SQL script execution for complex operations

## Use Cases

- **Database Documentation**: Generate comprehensive database documentation
- **Schema Migration**: Analyze and migrate database schemas
- **Performance Analysis**: Examine indexes and optimize queries
- **Data Access**: Query tables and views through standardized interface
- **Automation**: Automate database management tasks
- **Development**: Rapid prototyping and testing of database objects

This enhanced MCP server now provides the same level of database object visibility and management that you have in SQL Server Management Studio, but through a programmatic interface that can be used by AI assistants and other tools. 