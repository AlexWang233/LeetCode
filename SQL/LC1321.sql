# Write your MySQL query statement below
SELECT c1.visited_on, SUM(c2.day_sum) AS amount, ROUND(AVG(c2.day_sum), 2) AS average_amount FROM
(SELECT visited_on, SUM(amount) AS day_sum FROM Customer GROUP BY visited_on) c1 CROSS JOIN
(SELECT visited_on, SUM(amount) AS day_sum FROM Customer GROUP BY visited_on) c2
WHERE DATEDIFF(c1.visited_on, c2.visited_on) BETWEEN 0 AND 6
GROUP BY c1.visited_on HAVING COUNT(c2.visited_on) = 7