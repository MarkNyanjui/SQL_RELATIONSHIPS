### BRIEF SET UP

## DB Diagram Link
https://dbdiagram.io/d/Titans-Class-DB-66de9c22bc6a4b5bb59caaba


one to one -> student one - one student profile
one to many -> one student - many guardian
many to many -> many students - many units


TABLEs for the DB
students
	- id - int (auto increment) (unique)
	- name - string
	- gender - string
	- dob - string

student profile
	- id - int (auto increment) (unique)
	- admin no - integer
	- class ('names') - string

units
	- id - int (auto increment) (unique)
	- unit_name - string
	- unit_code - string (alphanumeric)

guardian
	- id - int (auto increment) (unique)
	- name - string
	- relationship - string
	- foreign key (student)

Join Table ( contains entries for 2 or more instance of other classess)
##### - Primary Key -> unique idenifier for a record in a table
##### - Foreign key-> used to create relationships by referencing to another tables primary key
##### - Composite key -> same as primary key but create a unique string based out of 2 columns



student_unit
	- id - int (auto increment) (unique)
	- foreign key (student_id)
	- foregin key (units_id)





JOINS
- Inner Join - Gets records that have matching values in one or more tables
- Left Join - Get all records from the left table and matched record from the other table
- Right Join - Get all records from the right table and matched record from the other table
- Full Join - Gets all records from either of the tables listed




