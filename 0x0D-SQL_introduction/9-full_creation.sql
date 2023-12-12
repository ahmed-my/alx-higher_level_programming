-- Script that creates a table second_table in the database hbtn_0c_0
-- add multiple rows: id INT, name VARCHAR(256), score INT
-- if second_table already exists, script should not fail
-- create these record:
-- id = 1, name ="John", score = 10
-- id = 2, name = "Alex", score = 3
-- id = 3, name = "Bob", score = 14
-- id = 4, name = "George", score = 8
CREATE IF NOT EXISTS TABLE second_table (
    id INT AUTO_INCREMENT,
    name VARCHAR(256),
    score INT
);
INSERT INTO second_table ( name, score)
    VALUES
    ("John", 10),
    ("Alex", 3),
    ("Bob", 14),
    ("George", 8);
