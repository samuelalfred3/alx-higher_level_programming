-- 5-unique_id.sql

-- Create the table if it doesn't already exist
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);

