-- SELECT * FROM Students 

-- SELECT * FROM Students JOIN StudentProfile ON Students.student_id = StudentProfile.student_id

-- SELECT Students.name, Students.gender, Students.dob, StudentProfile.admin_no, StudentProfile.class_name
-- FROM Students JOIN StudentProfile ON Students.student_id = StudentProfile.student_id

-- SELECT s.name, s.gender, s.dob, p.admin_no, p.class_name
-- FROM Students s JOIN StudentProfile p ON s.student_id = p.student_id;

-- left join  to get student, unit via studentunit knowing enrollments

-- SELECT * FROM Students
-- LEFT JOIN StudentUnits ON Students.student_id = StudentUnits.student_id
-- LEFT JOIN Units ON StudentUnits.unit_id = Units.unit_id;

SELECT s.name, u.unit_name FROM Students s
LEFT JOIN StudentUnits su ON s.student_id = su.student_id
LEFT JOIN Units u ON su.unit_id = u.unit_id;


