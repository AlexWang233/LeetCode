# Write your MySQL query statement below
SELECT p.product_name, SUM(o.unit) AS unit FROM
Products p LEFT JOIN Orders o USING(product_id)
WHERE DATE_FORMAT(order_date, '%Y-%m') = '2020-02'
GROUP BY p.product_name
HAVING SUM(o.unit) >= 100