DELETE
FROM Person
WHERE Person.id NOT IN  (
	SELECT PersonMinID FROM (
		SELECT
			Person.email,
			MIN(Person.id) AS PersonMinID
		FROM Person
		GROUP BY Person.email
	)
)

