class Course:
    def __init__(self, title, course_id, credit):
        self.title = title
        self.course_id = course_id
        self.credit = credit


class Teacher:
    def __init__(self, firstname, lastname, id):
        self.firstname = firstname
        self.lastname = lastname
        self.id = id

    def __str__(self):
        return f"{self.firstname} {self.lastname} ({self.id})"


class Major:
    def __init__(self, id, name, faculty):
        self.id = id
        self.name = name
        self.faculty = faculty

    def __str__(self):
        return f"{self.name} ({self.id})"


class Student:
    MAX_CREDITS = 25

    def __init__(self, id, firstname, lastname):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.courses = []
        self.num_course = 0
        self.total_credit = 0
        self.advisor = None
        self.major = None

    def add_course(self, course):
        if course not in self.courses and self.total_credit + course.credit <= Student.MAX_CREDITS:
            self.courses.append(course)
            self.num_course += 1
            self.total_credit += course.credit
            return True
        return False

    def drop_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
            self.num_course -= 1
            self.total_credit -= course.credit
            return True
        return False

    def set_advisor(self, advisor):
        self.advisor = advisor

    def set_major(self, major):
        self.major = major

    def __str__(self):
        courses_str = ' '.join(course.course_id for course in self.courses)
        advisor_str = str(self.advisor) if self.advisor else "None"
        major_str = str(self.major) if self.major else "None"

        return (
            f"Student ID: {self.id}\n"
            f"Name: {self.firstname} {self.lastname}\n"
            f"Major: {major_str}\n"
            f"Advisor: {advisor_str}\n"
            f"Courses: {courses_str}"
        )
