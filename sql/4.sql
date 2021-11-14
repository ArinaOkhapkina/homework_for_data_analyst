SELECT 
	classroom 
FROM Schedule
GROUP BY 
	classroom
HAVING 
	COUNT(classroom) = 
		(SELECT
			COUNT(classroom) AS c
		FROM Schedule
		GROUP BY classroom
		ORDER BY c DESC 
		LIMIT 1)
ORDER BY 
	COUNT(classroom) DESC