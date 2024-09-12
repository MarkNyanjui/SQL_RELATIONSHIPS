from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base() # basic class for creating models (tables)

class Student(Base):
    __tablename__ = 'students'

    student_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    gender = Column(String(6))
    dob = Column(String(8))
    

    ## Relationships
    profile = relationship('StudentProfile', back_populates='student')

    def __repr__(self):
        return f'Student name="{self.name}"'


class StudentProfile(Base):
    __tablename__ = 'profile'

    profile_id = Column(Integer, primary_key=True, autoincrement=True)
    admin_no = Column(Integer)
    class_name = Column(String(100))
    student_id = Column(Integer, ForeignKey('students.student_id'), unique=True)

    ## relationship
    student = relationship('Student', back_populates='profile')

## More models down here


# Connect to the database
engine = create_engine('sqlite:///school.db')

################################################################
## Start of CLI

## Option Functions 

def add_student():
    student_name = input('Student Name: ')
    student_gender = input('Gender: ')
    student_dob = input('Date of Birth (DD-MM-YYYY): ')

    # validations
    if student_gender not in ['Male', 'Female']:
        print('Invalid Gender. Please choose either Male or Female.')
        

    # create instance of student
    student1 = Student(name=student_name, gender=student_gender, dob=student_dob)

    # save the student
    with Session() as sesh:
        sesh.add(student1)
        sesh.commit()

        print(f"Student {student_name} Added Successfully")

### End Option Function


if __name__ == '__main__':
    # create tables in Database
    # Base.metadata.create_all(engine)

    # create a session
    Session = sessionmaker(bind=engine)
   
    help = '''
    0 - Exit the Program
    1 - Add a new Student
    2 - List all Students
    3 - Update a Student
    '''
    while True:
        print('-'*50)
        print(help)
        userInput = int(input('Select an Option:'))
        
        if userInput == '0':
            print('Thank You, Bye , See you Again Later!')
            exit()
        elif userInput == '1':
            add_student()
        elif userInput == '2':
            print('Selected Option is 2')
        elif userInput == '3':
            print('Selected Option is 3')
        else:
            print('Invalid Option, Must be String')