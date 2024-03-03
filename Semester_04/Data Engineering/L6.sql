SELECT title, length,
       CASE
         WHEN length > 0 AND length <= 50 THEN 'Short'
         WHEN length > 50 AND length <= 120 THEN 'Medium'
         WHEN length > 120 THEN 'Long'
       END AS duration
FROM Film ORDER BY title; 

SELECT
  SUM(CASE
    WHEN rental_rate = 0.99 THEN 1
    ELSE 0
  END) AS "Economy",
  SUM(CASE
    WHEN rental_rate = 2.99 THEN 1
    ELSE 0
  END) AS "Mass",
  SUM(CASE
    WHEN rental_rate =4.99 THEN 1
    ELSE 0
  END) AS "Premium"
FROM film;

Select title, rating,
	CASE rating
		WHEN 'G' THEN 'General Audiences'
		WHEN 'PG' THEN 'Parental Guidance Suggested'
		WHEN 'PG-13' THEN 'Parents Strongly Cautioned'
		WHEN 'R' THEN 'Restricted'
		WHEN 'NC-17' THEN 'Adults Only'	
	END rating_description
FROM film ORDER BY title;

SELECT SUM(CASE rating WHEN 'G' THEN 1 ELSE 0 END) "General Audiences",
SUM(CASE rating WHEN 'PG' THEN 1 ELSE 0 END) "Parental Guidance Suggested",
SUM(CASE rating WHEN 'PG-13' THEN 1 ELSE 0 END) "Parents Strongly Cautioned",
SUM(CASE rating WHEN 'R' THEN 1 ELSE 0 END) "Restricted",
SUM(CASE rating WHEN 'NC-17' THEN 1 ELSE 0 END) "Adults Only"
FROM film;

SELECT COALESCE (1,2);

SELECT COALESCE (NULL,2,1);

SELECT COALESCE (excerpt , LEFT (CONTENT, 150))
FROM post;

CREATE TABLE items(ID serial PRIMARY KEY,product VARCHAR(100)NOT NULL,PRICE NUMERIC NOT NULL,discount NUMERIC);
INSERT INTO itemS (product, price, discount) VALUES('A',1000,10),('B',1500,20),('C',800,5),('D',500,NULL)

SELECT product,(price-discount)AS net_price FROM items;
SELECT product, (price - COALESCE(discount,0)) AS net_price FROM items

SELECT product,(price - CASE WHEN discount IS NULL THEN 0 ELSE discount END)AS net_price FROM items;