# Write your MySQL query statement below
SELECT u.name, ifnull(sum(r.distance), 0) AS travelled_distance
FROM Users u
LEFT JOIN Rides r 
ON u.id = r.user_id
GROUP BY user_id
ORDER BY travelled_distance DESC, name ASC