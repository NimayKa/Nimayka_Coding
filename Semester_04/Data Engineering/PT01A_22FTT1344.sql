--Awangku Muhammad Yamin Bin Pengiran Ibnu
--22FTT1344
--DDAS02
-- Question 1

-- Q1A)
SELECT 2225/108*312 AS Result;

-- Q1B)
CREATE TABLE company (company_id INT PRIMARY KEY, company_name VARCHAR(255), company_activity VARCHAR(255),no_of_staff INT,no_of_branches INT);

-- Q1C)
INSERT INTO company (company_id,company_name,company_activity,no_of_staff,no_of_branches) VALUES
(1,'ABC Corp','Technology',50,3),
(2,'XYZ Ltd','Finance',30,2),
(3,'Acme Inc','Manufacturing',100,5),
(4,'Global Solutions','Consulting',80,4),
(5,'Smith Enterprises','Food & Beverage',25,1),
(6,'Johnson & Sons','Construction',60,3),
(7,'Sunrise Foods','Food & Beverage',75,2),
(8,'Peak Performance','Fitness',20,1),
(9,'BlueSky Restaurant','Food & Beverage',45,2),
(10,'Green Earth Co','Enviromental Services',40,3);

-- Q1D)
SELECT * FROM company LIMIT(8);

-- Q1E)
SELECT company_name,no_of_staff,no_of_staff*800 as Salary FROM company;

-- Q1F)
SELECT SUM(CASE WHEN company_name ~ '[0-9]' THEN 1 ELSE 0 END) AS contains_numbers FROM company;
-- Explaination
-- CASE WHEN...THEN...ELSE...END: This conditional expression checks each row in the company_name column.
-- WHEN company_name ~ '[0-9]': If the company name contains any number ([0-9] is a regular expression for digits), it evaluates to 1.
-- ELSE 0: Otherwise, it evaluates to 0.
-- SUM(...): This function adds up the results of the CASE expression for all rows in the company_name column.
-- > 0: This condition checks if the sum is greater than zero.
-- AS contains_numbers: Naming new column.

-- Question 2
-- Q2A)
SELECT UPPER(company_name) as company_name,company_activity FROM company WHERE company_activity ='Food & Beverage';

-- Q2B)
SELECT SUBSTRING(company_name,1,5) FROM company ORDER BY company_name ASC;

-- Q2C)
SELECT * FROM company WHERE no_of_staff > 60 ORDER BY no_of_staff DESC;

-- Q2D)
SELECT MAX(no_of_staff)AS Max_no_staff, MIN(no_of_staff) AS Min_no_of_Staff FROM company;

-- Q2E)
SELECT COUNT(*) AS num_companies FROM company WHERE company_activity = 'Food & Beverage';

-- Q2F)
SELECT DISTINCT * FROM company WHERE (no_of_branches >= 3 AND company_activity != 'Construction') OR company_id IN (1, 3);

-- Explaination
-- SELECT DISTINCT *: This selects all columns from the company table while removing duplicate rows.
-- (no_of_branches >= 3 AND company_activity != 'Construction'):filtering for companies with at least 3 branches and excluding those in construction.
-- OR company_id IN (1, 3): This condition directly checks if the company_id is in the list (1, 3), regardless of other criteria. The IN operator is used for efficient comparisons with multiple values.