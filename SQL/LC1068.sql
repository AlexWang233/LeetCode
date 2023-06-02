# Write your MySQL query statement below
SELECT DISTINCT P.product_name, S.year, S.price
FROM Sales S INNER JOIN Product P
ON P.product_id = s.product_id