SELECT
	Person.firstName AS firstName,
	Person.lastName AS lastName,
	Address.city AS city,
	Address.state AS state
FROM Person
LEFT JOIN  Address ON Address.personId = Person.personId;