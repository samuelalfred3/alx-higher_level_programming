-- 3-list_tables.sql

USE information_schema;

-- Query to select all tables in a specified database
SELECT TABLE_NAME
FROM TABLES
WHERE TABLE_SCHEMA = DATABASE();

