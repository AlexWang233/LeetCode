# Write your MySQL query statement below
# Select name of employees who
SELECT d.name AS Department, e1.name AS Employee, e1.salary AS Salary 
FROM Employee e1 INNER JOIN Department d ON e1.DepartmentId = d.Id
# Have < 3 people in the department have higher salary than them
WHERE (SELECT COUNT(DISTINCT(e2.Salary)) FROM Employee e2
WHERE e2.Salary > e1.Salary AND e1.DepartmentId = e2.DepartmentId) < 3