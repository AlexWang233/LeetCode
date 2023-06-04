# Write your MySQL query statement below
SELECT class FROM courses HAVING COUNT(DISTINCT student) >= 5