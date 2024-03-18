--Question 1
SELECT *
FROM employees
WHERE department IN (
  SELECT department
  FROM departments
  WHERE division = 'Electronics'
);

--Question 2
SELECT * FROM employees WHERE region_id IN (
	SELECT region_id FROM regions WHERE country IN ('Canada', 'Asia')
	)AND salary > 130000;

--Question 3
SELECT e.first_name, e.department,
	   (SELECT MAX(salary) FROM employees AS emp2 WHERE emp2.region_id = e.region_id) - e.salary AS salary_difference, 
	   (SELECT MAX(salary)FROM employees AS emp2 WHERE emp2.region_id = e.region_id) as Max_Salary,
		e.salary as Actual_salary
FROM employees e INNER JOIN regions r ON e.region_id = r.region_id
WHERE r.country IN ('Canada', 'Asia')ORDER BY e.salary ASC;


--Question 4
SELECT * FROM employees WHERE department IN (
  SELECT department FROM departments WHERE division = 'Kids')
AND hire_date > (SELECT MAX(hire_date) FROM employees WHERE department = 'Maintenance');

--Question 5
SELECT salary FROM (
  SELECT salary, COUNT(*) AS count FROM employees GROUP BY salary) AS salary_counts
	ORDER BY count DESC LIMIT 1;