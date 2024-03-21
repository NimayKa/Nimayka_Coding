CREATE TABLE employees (
    first_name VARCHAR,
    last_name VARCHAR,
    salary INTEGER
);


INSERT INTO employees (first_name, last_name, salary)
VALUES 
		('John', 'Cena', 900),
		('Mike', 'Tyson', 1200),
		('Alice', 'King', 800),
		('Bob', 'THE Builder', 1500),
		('Muhammad', 'Kakashi', 1000);

SELECT 
    first_name || ' ' || last_name AS employee_name,
    salary,
    CASE 
        WHEN salary < 1000 THEN 'Underpaid'
        WHEN salary > 1000 THEN 'Well-paid'
        ELSE 'Poorly paid'
    END AS salary_category
FROM 
    employees;


SELECT 
    first_name || ' ' || last_name AS employee_name,
    salary,
    CASE 
        WHEN salary < 1000 THEN 1
        WHEN salary > 1000 THEN 2
        ELSE 3
    END AS salary_category
FROM 
    employees;
	
	

SELECT 
    CASE 
        WHEN salary < 1000 THEN 'Underpaid'
        WHEN salary = 1000 THEN 'Paid well'
        ELSE 'Poorly paid'
    END AS salary_category,
    COUNT(*) AS number_of_salaries
FROM 
    employees
GROUP BY 
    CASE 
        WHEN salary < 1000 THEN 'Underpaid'
        WHEN salary = 1000 THEN 'Paid well'
        ELSE 'Poorly paid'
    END;
	
CREATE TABLE inventory (
    product_id INT,
    product_name VARCHAR(50),
    retail_price DECIMAL(10, 2),
    wholesale_price DECIMAL(10, 2)
);


--Question 1
INSERT INTO inventory (product_id, product_name, retail_price, wholesale_price)
VALUES
    (1, 'Widget A', 10.99, 8.99),
    (2, 'Widget B', NULL, 15.99),
    (3, 'Widget C', 20.99, 18.99),
    (4, 'Widget D', 12.99, NULL);
	
SELECT 
    product_id,
    product_name,
    COALESCE(retail_price, wholesale_price) AS price_to_display
FROM 
    inventory;


--Question 2
CREATE TABLE sales (
    product_id INT,
    q1_sales DECIMAL(10, 2),
    q2_sales DECIMAL(10, 2),
    q3_sales DECIMAL(10, 2),
    q4_sales DECIMAL(10, 2)
);

INSERT INTO sales (product_id, q1_sales, q2_sales, q3_sales, q4_sales)
VALUES
    (1, 100.50, 150.75, NULL, 200.25),
    (2, 75.25, NULL, 120.00, 180.50),
    (3, 200.00, 250.00, 180.75, 300.25),
    (4, NULL, 80.50, 150.25, 90.75);

SELECT 
    product_id,
    COALESCE(q1_sales, 0) + COALESCE(q2_sales, 0) + COALESCE(q3_sales, 0) + COALESCE(q4_sales, 0) AS total_sales
FROM 
    sales;
	
--Question 3
SELECT 
    product_id,
    product_name,
    CASE 
        WHEN retail_price IS NOT NULL THEN retail_price
        ELSE wholesale_price
    END AS price_to_display
FROM 
    inventory;
	
--Question 1
SELECT film.*
FROM film
INNER JOIN inventory ON film.film_id = inventory.film_id
WHERE inventory.store_id = 2
AND film.rental_duration BETWEEN 3 AND 5;

--Question 2
SELECT c.customer_id, c.first_name
FROM Customer c
INNER JOIN (
    SELECT customer_id, COUNT(*) AS rental_count
    FROM Rental
    GROUP BY customer_id
    ORDER BY rental_count DESC
    LIMIT 1
) AS rc ON c.customer_id = rc.customer_id;

--Question 3
SELECT
    (SELECT COUNT(*) FROM Customer WHERE store_id = 1) -
    (SELECT COUNT(*) FROM Customer WHERE store_id = 2) AS customer_difference;
