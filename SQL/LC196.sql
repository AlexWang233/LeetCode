# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below
DELETE p2 FROM Person p1, Person p2
WHERE p2.email = p1.email AND p2.id > p1.id