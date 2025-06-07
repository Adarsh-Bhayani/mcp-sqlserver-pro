# Stored Procedure Management Examples

This document provides examples of how to use the enhanced MCP server to manage T-SQL stored procedures.

## Available Tools

The MCP server now includes the following stored procedure management tools:

1. **create_procedure** - Create a new stored procedure
2. **modify_procedure** - Modify an existing stored procedure  
3. **delete_procedure** - Delete a stored procedure
4. **list_procedures** - List all stored procedures in the database
5. **describe_procedure** - Get the definition of a stored procedure
6. **execute_procedure** - Execute a stored procedure with optional parameters
7. **get_procedure_parameters** - Get parameter information for a stored procedure

## Examples

### 1. Create a Simple Stored Procedure

```sql
CREATE PROCEDURE GetEmployeeCount
AS
BEGIN
    SELECT COUNT(*) AS TotalEmployees FROM Employees
END
```

### 2. Create a Stored Procedure with Parameters

```sql
CREATE PROCEDURE GetEmployeesByDepartment
    @DepartmentId INT,
    @MinSalary DECIMAL(10,2) = 0
AS
BEGIN
    SELECT 
        EmployeeId,
        FirstName,
        LastName,
        Salary,
        DepartmentId
    FROM Employees 
    WHERE DepartmentId = @DepartmentId 
    AND Salary >= @MinSalary
    ORDER BY LastName, FirstName
END
```

### 3. Create a Stored Procedure with Output Parameters

```sql
CREATE PROCEDURE GetDepartmentStats
    @DepartmentId INT,
    @EmployeeCount INT OUTPUT,
    @AverageSalary DECIMAL(10,2) OUTPUT
AS
BEGIN
    SELECT 
        @EmployeeCount = COUNT(*),
        @AverageSalary = AVG(Salary)
    FROM Employees 
    WHERE DepartmentId = @DepartmentId
END
```

### 4. Modify an Existing Stored Procedure

```sql
ALTER PROCEDURE GetEmployeesByDepartment
    @DepartmentId INT,
    @MinSalary DECIMAL(10,2) = 0,
    @MaxSalary DECIMAL(10,2) = 999999.99
AS
BEGIN
    SELECT 
        EmployeeId,
        FirstName,
        LastName,
        Salary,
        DepartmentId,
        HireDate
    FROM Employees 
    WHERE DepartmentId = @DepartmentId 
    AND Salary BETWEEN @MinSalary AND @MaxSalary
    ORDER BY Salary DESC, LastName, FirstName
END
```

## Usage with MCP Tools

### List All Stored Procedures
Use the `list_procedures` tool to see all stored procedures in your database.

### Get Procedure Information
Use `describe_procedure` with the procedure name to see its full definition.

### Get Parameter Details
Use `get_procedure_parameters` with the procedure name to see detailed parameter information including data types, defaults, and whether they are output parameters.

### Execute Procedures
Use `execute_procedure` with the procedure name and an optional array of parameter values.

Examples:
- Execute without parameters: `execute_procedure` with `procedure_name: "GetEmployeeCount"`
- Execute with parameters: `execute_procedure` with `procedure_name: "GetEmployeesByDepartment"` and `parameters: ["1", "50000"]`

### Delete Procedures
Use `delete_procedure` with the procedure name to remove it from the database.

## Enhanced write_query Tool

The `write_query` tool has been enhanced to support stored procedure operations:

- CREATE PROCEDURE statements
- ALTER PROCEDURE statements  
- DROP PROCEDURE statements
- EXEC/EXECUTE statements

This allows you to manage stored procedures directly through SQL commands as well as using the dedicated tools.

## Best Practices

1. **Always test procedures** after creation or modification
2. **Use parameters** to prevent SQL injection
3. **Include error handling** in complex procedures using TRY/CATCH blocks
4. **Document your procedures** with comments
5. **Use meaningful names** for procedures and parameters
6. **Consider performance** implications of complex procedures 