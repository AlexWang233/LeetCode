# Write your MySQL query statement below
SELECT DISTINCT m.name 
FROM Employee e INNER JOIN Employee m 
ON m.id = e.managerId 
GROUP BY m.id HAVING COUNT(*) >= 5