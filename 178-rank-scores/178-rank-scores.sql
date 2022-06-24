# Write your MySQL query statement below
# select score,DENSE_RANK() OVER(ORDER BY SCORE) AS RANK FROM Scores;
SELECT score,
DENSE_RANK() OVER(ORDER BY score DESC) AS "rank"
FROM Scores;
