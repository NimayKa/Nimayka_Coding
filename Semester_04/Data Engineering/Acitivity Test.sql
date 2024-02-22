--Question 1
SELECT * FROM address;
--Question 2
SELECT address,address2 FROM address;
--Question 3
SELECT DISTINCT district FROM address;
--Question 4
SELECT * FROM address WHERE district = 'England';
--Question 5
CREATE TABLE departments (
  department_id INTEGER PRIMARY KEY,
  department_name VARCHAR(100) NOT NULL,
  division VARCHAR(100) NOT NULL,
  manager_id INTEGER,
  location VARCHAR(100) NOT NULL
);

INSERT INTO departments (department_id, department_name, division, manager_id, location)
VALUES (1, 'Music', 'Entertainment', 1001, 'New York'),
       (2, 'Finance', 'Finance', 1002, 'Chicago'),
       (3, 'Human Resources', 'Administration', 1003, 'Los Angeles'),
       (4, 'Research and Development', 'Technology', 1004, 'San Francisco'),
       (5, 'Customer Service', 'Operations', 1005, 'Dallas'),
       (6, 'Music', 'Entertainment', 1006, 'Miami'),
       (7, 'Legal', 'Administration', 1007, 'Washington D.C.'),
       (8, 'Music', 'Entertainment', 1008, 'Seattle'),
       (9, 'Production', 'Operations', 1009, 'Houston'),
       (10, 'Information Technology', 'Technology', 1010, 'Boston');
--Question 6   
SELECT * FROM departments WHERE division ='Entertainment' AND department_name = 'Music';
--Question 7
SELECT * FROM departments WHERE division ='Finance' OR division = 'Administration' AND department_name = 'Finance' OR department_name ='Human Resources';
--Question 8
SELECT title FROM film WHERE title LIKE '%di' or title LIKE '%do';
--Question 9
SELECT title,rating FROM film WHERE rating = 'PG' or rating = 'PG-13';
--Question 10
SELECT title,length FROM film WHERE length >= 100;
--Question 11
SELECT title,description FROM film WHERE description LIKE '%Man%' or description LIKE '%Woman%';
--Question 12
SELECT title, description,LENGTH(title) AS title_length, LENGTH(description) AS description_length, LENGTH(title) + LENGTH(description) AS total_length FROM film;
--Question 13
SELECT title, description,CONCAT(title, ' - ', description) AS full_synopsis FROM film;
