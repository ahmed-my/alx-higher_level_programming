-- Script that creates the table force_name on my MySQL server
-- id INT
-- name VARCHAR(256) can't be null
-- if the table force_name already exists, script should not fail
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
