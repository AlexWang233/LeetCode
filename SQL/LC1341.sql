# Write your MySQL query statement below
(SELECT u.name AS results FROM
Users u LEFT JOIN MovieRating mr ON u.user_id = mr.user_id
GROUP BY u.name
ORDER BY COUNT(mr.movie_id) desc, u.name LIMIT 1)
UNION ALL
(SELECT m.title AS results FROM 
MovieRating mr LEFT JOIN Movies m ON m.movie_id = mr.movie_id
WHERE DATE_FORMAT(mr.created_at, '%Y-%m') = "2020-02"
GROUP BY m.title
ORDER BY AVG(mr.rating) desc, m.title LIMIT 1)