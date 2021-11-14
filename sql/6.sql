WITH Battles_CTE (rn, name, date)
AS
(SELECT
 ROW_NUMBER() over(ORDER BY date, name) as rn,
 name,
 date
FROM Battles)

SELECT TOP (SELECT COUNT(*) from Battles_CTE WHERE rn%2=1)
	b.rn AS rn_1,
	b.name AS name_1,
	b.date AS date_1,
	LEAD(b.rn, (SELECT COUNT(*) from Battles_CTE WHERE rn%2=1) , null) OVER(ORDER BY b.rn) AS rn_2,
	LEAD(b.name, (SELECT COUNT(*) from Battles_CTE WHERE rn%2=1), null) OVER(ORDER BY b.rn) AS name_2,
	LEAD(b.date, (SELECT COUNT(*) from Battles_CTE WHERE rn%2=1), null) OVER(ORDER BY b.rn) AS date_2
FROM Battles_CTE AS b;