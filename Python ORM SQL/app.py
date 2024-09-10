import sqlite3

# establish connection
connection = sqlite3.connect('school.db')
cursor = connection.cursor() # enables to execute SQL queries


#### Classes/Tables

class Student:
    def __init__(self, name, gender, dob):
        self.name = name
        self.gender = gender
        self.dob = dob
        self.student_id = None # will update this later

    # create the table
    @classmethod
    def create_table(cls):
        sql_query = '''
            CREATE TABLE IF NOT EXISTS Students (
                student_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                name VARCHAR(100),
                gender VARCHAR(6),
                dob VARCHAR(8)
            );
        '''
        cursor.execute(sql_query) # Will run the query
        connection.commit() # will save the result in the database

    # save student
    def save(self):
        sql_query = f'''INSERT INTO Students (name, gender, dob) 
                    VALUES ('{self.name}', '{self.gender}', '{self.dob}');
                    '''
        
        cursor.execute(sql_query)
        connection.commit()
        self.student_id = cursor.lastrowid

    # update student
    def update(self, name):
        sql_query = '''UPDATE Students
                            SET name=?
                            WHERE student_id=?
                    '''
        cursor.execute(sql_query, (name, self.student_id))
        connection.commit()

    # delete student
    @classmethod
    def delete(cls, student_id):
        pass

    # get student by id
    @classmethod
    def get_student_by_id(cls, student_id):
        sql_query = 'SELECT * FROM Students WHERE student_id=?'
        cursor.execute(sql_query, (student_id,))
        data = cursor.fetchall()
        return data
    
    # update student fetched from database
    @classmethod
    def update_student_by_id(cls, name, student_id):
        sql_query = '''UPDATE Students
                            SET name=?
                            WHERE student_id=?
                    '''
        cursor.execute(sql_query, (name, student_id))
        connection.commit()

class StudentProfile:
    def __init__(self, admin_no, class_name, student_id):
        self.admin_no = admin_no
        self.class_name = class_name
        self.student_id = student_id # to will contain the id of a student
        self.profile_id = None # to be updated during saving data

    @classmethod
    def create_table(cls):
        sql_query = '''
            CREATE TABLE IF NOT EXISTS StudentProfile (
                profile_id INTEGER PRIMARY KEY AUTOINCREMENT,
                admin_no INT,
                class_name VARCHAR(100),
                student_id INT UNIQUE,

                -- one to one relationship
                FOREIGN KEY (student_id) REFERENCES Students(student_id)
            );
        '''
        cursor.execute(sql_query)
        connection.commit()

    def save(self):
        sql_query = '''
            INSERT INTO StudentProfile (admin_no, class_name, student_id)
            VALUES (?,?,?)
                    '''
        cursor.execute(sql_query, (self.admin_no, self.class_name, self.student_id))
        connection.commit()

    





################################################

# Create Tables
Student.create_table()
StudentProfile.create_table()


# Create instances
# student1 = Student('Vinitta', 'Male', '1990-01-01')
# student2 = Student('Jane Mugo', 'Female', '1985-12-31')
# student3 = Student('John Pascal', 'male', '1852-12-27')


# # Save instances to database
# student1.save()
# student2.save()
# student3.save()

# # update instance to database
# student1.update('Gavin')

###### Get Student Data from Database
# student = Student.get_student_by_id(11)
# print(student)
# Student.update_student_by_id('Khalid', 13)


#### create a student
student1 = Student('Marvin', 'Male', '1989-02-03')
######### save the student
student1.save() # will save data and update the student_id

#### Create StudentProfile instances
stud1pro = StudentProfile(4569, 'Titans', student1.student_id)
stud1pro.save()