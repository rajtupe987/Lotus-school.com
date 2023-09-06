# Lotus School Management System

Welcome to the Lotus School Management System, a powerful educational platform built with Django. This system helps manage students, instructors, courses, enrollments, assignments, and announcements in an educational institution.

## Features

- **Students:** Manage student information, including names, emails, and roles.
- **Instructors:** Keep track of instructors with their expertise, names, and emails.
- **Departments:** Organize departments within the institution.
- **Courses:** Create and manage courses with titles, descriptions, instructors, and departments.
- **Enrollments:** Track student enrollments in courses with enrollment dates.
- **Assignments:** Manage assignments for courses, including titles, descriptions, and due dates.
- **Announcements:** Share important announcements related to departments or courses.

## API Endpoints

To interact with the Lotus School Management System, you can use the following API endpoints:

- **Students:**
  - `GET /students`: Retrieve a list of all students.
  - `GET /students/{student_id}`: Retrieve details of a specific student.
  - `POST /students`: Create a new student.
  - `PUT /students/{student_id}`: Update details of a specific student.
  - `DELETE /students/{student_id}`: Delete a student.

- **Instructors:**
  - `GET /instructors`: Retrieve a list of all instructors.
  - `GET /instructors/{instructor_id}`: Retrieve details of a specific instructor.
  - `POST /instructors`: Create a new instructor.
  - `PUT /instructors/{instructor_id}`: Update details of a specific instructor.
  - `DELETE /instructors/{instructor_id}`: Delete an instructor.

- **Departments:**
  - `GET /departments`: Retrieve a list of all departments.
  - `GET /departments/{department_id}`: Retrieve details of a specific department.
  - `POST /departments`: Create a new department.
  - `PUT /departments/{department_id}`: Update details of a specific department.
  - `DELETE /departments/{department_id}`: Delete a department.

- **Courses:**
  - `GET /courses`: Retrieve a list of all courses.
  - `GET /courses/{course_id}`: Retrieve details of a specific course.
  - `POST /courses`: Create a new course.
  - `PUT /courses/{course_id}`: Update details of a specific course.
  - `DELETE /courses/{course_id}`: Delete a course.

- **Enrollments:**
  - `GET /enrollments`: Retrieve a list of all enrollments.
  - `GET /enrollments/{enrollment_id}`: Retrieve details of a specific enrollment.
  - `POST /enrollments`: Create a new enrollment.
  - `PUT /enrollments/{enrollment_id}`: Update details of a specific enrollment.
  - `DELETE /enrollments/{enrollment_id}`: Delete an enrollment.

- **Assignments:**
  - `GET /assignments`: Retrieve a list of all assignments.
  - `GET /assignments/{assignment_id}`: Retrieve details of a specific assignment.
  - `POST /assignments`: Create a new assignment.
  - `PUT /assignments/{assignment_id}`: Update details of a specific assignment.
  - `DELETE /assignments/{assignment_id}`: Delete an assignment.

- **Submissions:**
  - `GET /submissions`: Retrieve a list of all submissions.
  - `GET /submissions/{submission_id}`: Retrieve details of a specific submission.
  - `POST /submissions`: Create a new submission.
  - `PUT /submissions/{submission_id}`: Update details of a specific submission.
  - `DELETE /submissions/{submission_id}`: Delete a submission.

- **Announcements:**
  - `GET /announcements`: Retrieve a list of all announcements.
  - `GET /announcements/{announcement_id}`: Retrieve details of a specific announcement.
  - `POST /announcements`: Create a new announcement.
  - `PUT /announcements/{announcement_id}`: Update details of a specific announcement.
  - `DELETE /announcements/{announcement_id}`: Delete an announcement.

