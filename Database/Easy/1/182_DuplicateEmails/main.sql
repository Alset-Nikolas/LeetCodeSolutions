SELECT
	Person.email
FROM Person
GROUP BY Person.email
HAVING COUNT(*) > 2;