SELECT AVG(rental_rate) FROM Film;

SELECT film,title,rental_rate FROM film WHERE rental_rate => 2.98

SELECT film,title,rental_rate FROM film WHERE rental_rate => (SELECT AVG(rental_rate) FROM Film);

SELECT inventory.film_id FROM rental INNER JOIN inventory ON inventory.inventory_id = rental.inventory_id 
WHERE return_date BETWEEN '2005-05-29' AND '2005-05-30';

SELECT  film_id , title FROM film WHERE film_id IN 
(SELECT inventory.film_id FROM rental INNER JOIN inventory ON inventory.inventory_id = rental.inventory_id 
WHERE return_date BETWEEN '2005-05-29' AND '2005-05-30');
 
SELECT first_name, last_name FROM customer 
WHERE EXISTS (SELECT 1 FROM payment WHERE payment.customer_id = customer.customer_id);

SELECT title FROM film 
WHERE length >= ANY (SELECT MAX(length) FROM film INNER JOIN film_category USING(film_id) GROUP BY category_id);

SELECT title,category_id FROM film INNER JOIN film_category USING (film_id) 
WHERE category_id = ANY (SELECT category_id FROM category WHERE NAME = 'Action' OR NAME = 'Drama')

SELECT title,category_id FROM film INNER JOIN film_category USING (film_id) 
WHERE category_id IN (SELECT category_id FROM category WHERE NAME = 'Action' OR NAME = 'Drama')

SELECT film_id,title,length FROM film
WHERE length>ALL(SELECT ROUND(AVG (length),2)FROM film GROUP BY rating)ORDER BY length;
