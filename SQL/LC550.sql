# Write your MySQL query statement below
SELECT ROUND(COUNT(p1.player_id) / COUNT(p2.player_id), 2) AS fraction
FROM (SELECT player_id, MIN(event_date) AS first_login FROM Activity GROUP BY player_id) p2
LEFT JOIN Activity p1 ON p1.player_id = p2.player_id AND p2.first_login = p1.event_date - 1