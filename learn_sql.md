# What is database
A database is a collection of data that is organized in a manner that facilitates ease of access, as well as efficient management and updating.

A database is made up of tables that store relevant information.

For example, you would use a database, if you were to create a website like YouTube, which contains a lot of information like videos, usernames, passwords, comments.

# Database Tables
A table stores and displays data in a structured format consisting of columns and rows that are similar to those seen in Excel spreadsheets.

Databases often contain multiple tables, each designed for a specific purpose. For example, imagine creating a database table of names and telephone numbers.

First, we would set up columns with the titles FirstName, LastName and TelephoneNumber.

Each table includes its own set of fields, based on the data it will store.

# SQL Tables
A single database can house hundreds of tables, each playing its own unique role in the database schema.

SQL tables are comprised of table rows and columns. Table columns are responsible for storing many different types of data, including numbers, texts, dates, and even files.

The CREATE TABLE statement is used to create a new table.

-CREATE TABLE table_name
(
column_name1 data_type(size),
column_name2 data_type(size),
column_name3 data_type(size),
....
columnN data_type(size)
);

- The column_names specify the names of the columns we want to create.
- The data_type parameter specifies what type of data the column can hold. For example, use int for whole numbers.
- The size parameter specifies the maximum length of the table's column.

# DATA Types
Data types specify the type of data for a particular column.

If a column called "LastName" is going to hold names, then that particular column should have a "varchar" (variable-length character) data type.
The most common data types:
Numeric
INT -A normal-sized integer that can be signed or unsigned.
FLOAT(M,D) - A floating-point number that cannot be unsigned. You can optionally define the display length (M) and the number of decimals (D).
DOUBLE(M,D) - A double precision floating-point number that cannot be unsigned. You can optionally define the display length (M) and the number of decimals (D).

Date and Time
DATE - A date in YYYY-MM-DD format.
DATETIME - A date and time combination in YYYY-MM-DD HH:MM:SS format.
TIMESTAMP - A timestamp, calculated from midnight, January 1, 1970
TIME - Stores the time in HH:MM:SS format.

String Type
CHAR(M) - Fixed-length character string. Size is specified in parenthesis. Max 255 bytes.
VARCHAR(M) - Variable-length character string. Max size is specified in parenthesis.
BLOB - "Binary Large Objects" and are used to store large amounts of binary data, such as images or other types of files.
TEXT - Large amount of text data.

# Primary Keys
A primary key is a field in the table that uniquely identifies the table records.

The primary key's main features:
- It must contain a unique value for each row.
- It cannot contain NULL values.

For example, our table contains a record for each name in a phone book. The unique ID number would be a good choice for a primary key in the table, as there is always the chance for more than one person to have the same name.

# SQL Constraints
SQL constraints are used to specify rules for table data.

The following are commonly used SQL constraints:
NOT NULL - Indicates that a column cannot contain any NULL value.
UNIQUE - Does not allow to insert a duplicate value in a column. The UNIQUE constraint maintains the uniqueness of a column in a table. More than one UNIQUE column can be used in a table.
PRIMARY KEY - Enforces the table to accept unique data for a specific column and this constraint create a unique index for accessing the table faster.
CHECK - Determines whether the value is valid or not from a logical expression.
DEFAULT - While inserting data into a table, if no value is supplied to a column, then the column gets the value set as DEFAULT.

For example, the following means that the name column disallows NULL values.

# What is SQL
Once you understand what a database is, understanding SQL is easy. SQL stands for Structured Query Language.

SQL is used to access and manipulate a database.
MySQL is a program that understands SQL.

SQL can:
- insert, update, or delete records in a database.
- create new databases, tables, stored procedures and views.
- retrieve data from a database, etc.

# Basic SQL Commands

## SHOW DATABASES
The SQL SHOW statement displays information contained in the database and its tables. This helpful tool lets you keep track of your database contents and remind yourself about the structure of your tables.
For example, the SHOW DATABASES command lists the databases managed by the server.

## SHOW TABLES
The SHOW TABLES command is used to display all of the tables in the currently selected MySQL database.

## SHOW COLUMNS FROM tbl_name
SHOW COLUMNS displays information about the columns in a given table.
SHOW COLUMNS displays the following values for each table column:

Field: column name
Type: column data type
Key: indicates whether the column is indexed
Default: default value assigned to the column
Extra: may contain any additional information that is available about a given column

## SELECT 
- SELECt * FROM tbl_name
- SELECt column_name1, column_name2 FROM tbl_name

The SELECT statement is used to select data from a database.
The result is stored in a result table, which is called the result-set.

A query may retrieve information from selected columns or from all columns in the table.

## DISTINCT Keyword 
- SELECT DISTINCT column_name1 FROM tbl_name

In situations in which you have multiple duplicate records in a table, it might make more sense to return only unique records, instead of fetching the duplicates.

The SQL DISTINCT keyword is used in conjunction with SELECT to eliminate all duplicate records and return only unique ones.

## LIMIT and OFFSET Keyword 
- SELECT column_name1, column_name2 from tble_name LIMIT no_of_records
- SELECT column_name1, column_name2 from tble_name OFFSET no_of_position LIMIT no_of_records

By default, all results that satisfy the conditions specified in the SQL statement are returned. However, sometimes we need to retrieve just a subset of records. In MySQL, this is accomplished by using the LIMIT keyword.

## FUlly Qualifies names
In SQL, you can provide the table name prior to the column name, by separating them with a dot.
The following statements are equivalent:
1. SELECT City FROM customers;
2. SELECT customers.City FROM customers;

## ORDER BY 
- SELECT * FROM tbl_name ORDER BY column_name
- SELECT * FROM tbl_name ORDER BY column_name1, column_name2

ORDER BY is used with SELECT to sort the returned data. 
By default, the ORDER BY keyword sorts the results in ascending order

ORDER BY can sort retrieved data by multiple columns. When using ORDER BY with more than one column, separate the list of columns to follow ORDER BY with commas.

The ORDER BY command starts ordering in the same sequence as the columns. It will order by the first column listed, then by the second, and so on.

The DESC keyword sorts results in descending order.
Similarly, ASC sorts the results in ascending order.

## WHERE STATEMENT
- SELECT * FROM tble_name WHERE condition

The WHERE clause is used to extract only those records that fulfill a specified criterion.
Comparison Operators and Logical Operators are used in the WHERE clause to filter the data to be selected.

The following comparison operators can be used in the WHERE clause: =, !=, >, <, >=, <=, BETWEEN

The BETWEEN operator selects values within a range. The first value must be lower bound and the second value, the upper bound.

When working with text columns, surround any text that appears in the statement with single quotation marks (').

- SELECT Column_name(s) FROM tbl_name WHERE column_name BETWEEN value1 AND value2

### Logical Operators
Logical operators can be used to combine two Boolean values and return a result of true, false, or null.
The following operators can be used: AND, OR, IN, NOT

When retrieving data using a SELECT statement, use logical operators in the WHERE clause to combine multiple conditions.

#### IN/NOT IN Operator
- SELECT * FROM tbl_name WHERE column_name IN (value1, value2, value3)
- SELECT * FROM tbl_name WHERE column_name NOT IN (value1, value2, value3)

The IN operator is used when you want to compare a column with more than one value.

## CONCAT function
concatenate two column , separating them with a comma
- SELECT CONCAT(column1, ', ', column2) FROM tbl_name

The CONCAT function is used to concatenate two or more text values and returns the concatenating string.

## AS Keyword
- SELECT column_name as new_column_name

A concatenation results in a new column. The default column name will be the CONCAT function.
You can assign a custom name to the resulting column using the AS keyword:

## UPPER/LOWER function
The UPPER function converts all letters in the specified string to uppercase.
The LOWER function converts the string to lowercase.

## SQRT/AVG function
The SQRT function returns the square root of given value in the argument. Similarly, the AVG function returns the average value of a numeric column:

## SUM function
The SUM function is used to calculate the sum for a column's values.

## MIN function
The MIN function is used to return the minimum value of an expression in a SELECT statement.


## Subqueries
A subquery is a query within another query.

##  The Like Operator
The LIKE keyword is useful when specifying a search condition within your WHERE clause.

SQL pattern matching enables you to use "_" to match any single character and "%" to match an arbitrary number of characters (including zero characters).

For example, to select employees whose FirstNames begin with the letter A, you would use the following query:
- SELECT * FROM employees WHERE FirstName LIKE 'A%'

## Joining Tables
One of the most beneficial features of SQL is the ability to combine data from two or more tables.

In SQL, "joining tables" means combining data from two or more tables. A table join creates a temporary table showing the data from the joined tables.

Each table contains "ID" and "Name" columns, so in order to select the correct ID and Name, fully qualified names are used.

Custom names can be used for tables as well. You can shorten the join statements by giving the tables "nicknames":
- SELECT tbl1.column_name1, tbl1.column_name2, tbl2.column_name1 FROM tbl_name1 AS tbl1, tbl_name2 AS tbl2 WHERE tbl1.column_name = tbl2.column_name

### Types of Join
The following are the types of JOIN that can be used in MySQL:
- INNER JOIN
- LEFT JOIN
- RIGHT JOIN

#### INNER JOIN
INNER JOIN is equivalent to JOIN. It returns rows when there is a match between the tables
- SELECT column_name(s) FROM tbl1 INNER JOIN tbl2 ON tbl1.column_name = tbl2.column_name

Only the records matching the join condition are returned.

#### LEFT JOIN
The LEFT JOIN returns all rows from the left table, even if there are no matches in the right table.

This means that if there are no matches for the ON clause in the table on the right, the join will still return the rows from the first table in the result.

- SELECT tbl1.column1, tbl2.column2, ... FROM tbl1 LEFT OUTER JOIN tbl2 ON tbl1.column_name = tbl2.column_name
The OUTER keyword is optional, and can be omitted.

#### RIGHT JOIN
The RIGHT JOIN returns all rows from the right table, even if there are no matches in the left table.

- SELECT tbl1.column1, tbl2.column2, ... FROM tbl1 RIGHT OUTER JOIN tbl2 ON tbl1.column_name = tbl2.column_name

### UNION
Occasionally, you might need to combine data from multiple tables into one comprehensive dataset. This may be for tables with similar data within the same database or maybe there is a need to combine similar data across databases or even across servers.

To accomplish this, use the UNION and UNION ALL operators.

UNION combines multiple datasets into a single dataset, and removes any existing duplicates.
UNION ALL combines multiple datasets into one dataset, but does not remove duplicate rows.

The UNION operator is used to combine the result-sets of two or more SELECT statements.

All SELECT statements within the UNION must have the same number of columns. The columns must also have the same data types. Also, the columns in each SELECT statement must be in the same order.

- SELECT column_name(s) FROM tbl1 UNION SELECT column_name(s) FROM tbl2

### UNION ALL
UNION ALL selects all rows from each table and combines them into a single table.

- SELECT column_name(s) FROM tbl1 UNION ALL SELECT column_name(s) FROM tbl2


## INSERT INTO Statement
SQL tables store data in rows, one row after another. The INSERT INTO statement is used to add new rows of data to a table in the database.

- INSERT INTO tbl_name VALUES('value1', 'value2', ....)
- INSERT INTO tbl_name ('column1', 'column2', ...) VALUES('value1', 'value2', ....)

## UPDATE
The UPDATE statement allows us to alter data in the table
You specify the column and its new value in a comma-separated list after the SET keyword.

-UPDATE table_name SET column1=value1, column2=value2 WHERE condition

If you omit the WHERE clause, all records in the table will be updated!

## DELETE FROM
The DELETE statement is used to remove data from your table. DELETE queries work much like UPDATE queries.

- DELETE FROM tbl_name WHERE condition
If you omit the WHERE clause, all records in the table will be deleted!
The DELETE statement removes the data from the table permanently.



## ALTER TABLE
The ALTER TABLE command is used to add, delete, or modify columns in an existing table.
You would also use the ALTER TABLE command to add and drop various constraints on an existing table.

### adding
ALTER TABLE tbl_name ADD column_name datatype

### dropping
ALTER TABLE tbl_name DROP COLUMN column_name

To delete the entire table, use the DROP TABLE command: 
- DROP TABLE tbl_name;

### renaming
The ALTER TABLE command is also used to rename columns:
- ALTER TABLE tbl_name RENAME column_name to new_column_name

You can rename the entire table using the RENAME command:
- RENAME TABLE tbl_name to new_table_name

## Views
In SQL, a VIEW is a virtual table that is based on the result-set of an SQL statement.

A view contains rows and columns, just like a real table. The fields in a view are fields from one or more real tables in the database.

Views allow us to:
- Structure data in a way that users or classes of users find natural or intuitive.
- Restrict access to the data in such a way that a user can see and (sometimes) modify exactly what they need and no more.
- Summarize data from various tables and use it to generate reports.

- CREATE VIEW view_name AS SELECT column(s) FROM tbl_name WHERE condition;
- CREATE VIEW OR REPLACE view_name AS SELECT column(s) FROM tbl_name WHERE condition;
















# Syntax Rule
### Multiple Queries
SQL allows to run multiple queries or commands at the same time.
Remember to end each SQL statement with a semicolon to indicate that the statement is complete and ready to be interpreted.

### Case Sensitivity
SQL is case insensitive. But tt is common practice to write all SQL commands in upper-case.

### White spaces and multiple lines
A single SQL statement can be placed on one or more text lines. In addition, multiple SQL statements can be combined on a single text line.

White spaces and multiple lines are ignored in SQL.
For example, the following query is absolutely correct. However, it is recommended to avoid unnecessary white spaces and lines.
