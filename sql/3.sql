SELECT DISTINCT 
	r.*
FROM Rooms AS r
JOIN Reservations AS re
	ON r.id = re.room_id
WHERE
	WEEK(re.start_date, 1) = 12
	AND YEAR(re.start_date) = 2020;