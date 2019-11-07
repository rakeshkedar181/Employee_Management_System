Feature: Employee Web Application using Flask

Scenario: Display All Employees On Browser
	Given User wants to browse list of employees
	Then he should see the list with count

Scenario: Add Employee using Browser
	Given set of employees
	|empno	|name	|salary	|
	|9		|Tejas	|8500	|
	Then Employee details will be added and count will increase
	
Scenario: Delete Employee using Browser
	Given set of employees
	|empno	|
	|9		|
	Then Employee details will be deleted and count will decrease
