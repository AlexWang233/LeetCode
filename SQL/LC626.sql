SELECT if(id % 2 > 0, if(id < (SELECT max(id) FROM seat), id + 1, id), id - 1) AS id, student
FROM seat ORDER BY id