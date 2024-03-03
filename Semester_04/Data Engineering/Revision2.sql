CREATE TABLE customer(customer_id serial PRIMARY KEY,
					  country VARCHAR(100)NOT NULL,
					  city VARCHAR(100)NOT NULL);
					  
INSERT INTO customer (customer_id, country, city)
VALUES (1, 'Brunei', 'Seria'),
       (2, 'Malaysia', 'Putrajaya'),
       (3, 'Singapore', 'Punggol'),
       (4, 'Brunei', 'Bangar'),
       (5, 'Malaysia', 'Kuching'),
       (6, 'Singapore', 'Yishun'),
       (7, 'Brunei', 'Mentiri'),
       (8, 'Malaysia', 'Malacca'),
       (9, 'Singapore', 'Geylang'),
       (10, 'Brunei', 'Gadong');
	   
SELECT * FROM customer;

SELECT city FROM customer;

SELECT distinct(country) FROM customer;

SELECT * FROM customer WHERE country = 'Brunei';

SELECT * FROM customer WHERE country = 'Singapore' AND city ='Yishun';

SELECT * FROM customer WHERE country = 'Malaysia' OR city = 'Seria';

CREATE TABLE staff(staff_id serial PRIMARY KEY,
					  first_name VARCHAR(20)NOT NULL,
					  last_name VARCHAR(20)NOT NULL,
					  department VARCHAR(20)NOT NULL,
					  salary INT NOT NULL,
					 job_role VARCHAR(20)NOT NULL);
					 
INSERT INTO staff (staff_id, first_name, last_name, department, salary, job_role)
VALUES (1, 'Jame', 'Joe', 'Marketing', 25000, 'Clerk'),
       (2, 'Angelina', 'Jamie', 'Admin', 25000, 'Clerk'),
       (3, 'Will', 'Smack', 'Finance', 25050, 'Clerk'),
       (4, 'Ed', 'Shewalk', 'Marketing', 37030, 'Officer'),
       (5, 'Elon', 'Mask', 'Admin', 38050, 'Officer'),
       (6, 'Robert', 'Upney Jr', 'Marketing', 38000, 'Officer'),
       (7, 'Cristiano', 'Rivaldo', 'Admin', 22000, 'Clerk'),
       (8, 'Kanye', 'South', 'Finance', 45000, 'Manager'),
       (9, 'Tom', 'Fly', 'Marketing', 43500, 'Manager'),
       (10, 'Clint', 'Westwood', 'Admin', 50000, 'Manager');

SELECT first_name AS "First Name", last_name AS "Last Name"
FROM staff;

SELECT first_name, last_name,
       LENGTH(CONCAT(first_name, ' ', last_name)) AS full_name_length
FROM staff;

SELECT CONCAT(first_name, ' ', last_name) AS full_name
FROM staff;
