SELECT
	COALESCE ((SELECT SUM(out) FROM Outcome_o WHERE date > s.dt1 and date <= s.dt2), 0) AS qty,
	s.dt1,
	s.dt2
FROM
(
	SELECT
		*
	FROM 
	(
		SELECT 
			date AS dt1,
			LEAD(date) OVER(ORDER BY date) AS dt2
		FROM (SELECT DISTINCT date FROM Income_o) AS s
	) AS s
	WHERE s.dt2 IS NOT NULL
) AS s;