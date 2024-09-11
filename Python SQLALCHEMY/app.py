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

# create the tables in the database
Base.metadata.create_all(engine)


################################### Interact with the database

Session = sessionmaker(bind=engine)
sesh = Session()

# create a Student
# student1 = Student(name='Mark', gender='Male', dob='1978-04-23')
# student2 = Student(name='Lewis', gender='Male', dob='1990-04-23')
# student3 = Student(name='Joy', gender='Female', dob='1952-09-12')

# save the student
# sesh.add(student1)
# sesh.add_all([student1, student2, student3])
# sesh.commit()

# get all students
# all_students = sesh.query(Student).all()
# print(all_students)
filterd_students = sesh.query(Student).filter(Student.gender=='Male').all()
print(filterd_students)
sesh.close()


### auto close the session
# with Session() as sesh:
#     all your queries here

# Session = scoop_session(sessionmaker(bind=engine))