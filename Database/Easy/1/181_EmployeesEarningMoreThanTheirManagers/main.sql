SELECT
	Employee.name AS Employee
FROM Employee
LEFT OUTER JOIN  Employee AS MANAGER ON Employee.managerId = MANAGER.id
WHERE MANAGER.salary < Employee.salary;