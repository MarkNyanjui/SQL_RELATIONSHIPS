--- Students
CREATE TABLE Students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name VARCHAR(100),
    gender VARCHAR(6),
    dob VARCHAR(8)
);

-- Student Profile
CREATE TABLE StudentProfile (
    profile_id INTEGER PRIMARY KEY AUTOINCREMENT,
    admin_no INT,
    class_name VARCHAR(100),
    student_id INT UNIQUE,

    -- one to one relationship
    FOREIGN KEY (student_id) REFERENCES Students(student_id)
);

-- Guardian
CREATE TABLE Guardian (
    guardian_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100),
    relationship VARCHAR(100),
    student_id INT,

    -- one to many relationship
    FOREIGN KEY (student_id) REFERENCES Students(student_id)
);

-- UNITS
CREATE TABLE Units (
    unit_id INTEGER PRIMARY KEY AUTOINCREMENT,
     VARCHAR(50),
    unit_code VARCHAR(20)
);

---- Join Table (Many to many relationship)
CREATE TABLE StudentUnits (
    su_id INTEGER PRIMARY KEY AUTOINCREMENT,

    student_id INT,
    unit_id INT,

    -- relationship
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (unit_id) REFERENCES Units(unit_id)
);