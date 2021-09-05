class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.Gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def student_grades(self):
        avarage_grades = []
        for key in self.grades:
            avarage_grades += self.grades[key]
        avarage_grade = sum(avarage_grades)/len(avarage_grades)
        return avarage_grade


    def __lt__(self, other):
        return  self.student_grades() < other.student_grades()

    def __le__(self,other):
        return  self.student_grades() <= other.student_grades()

    def __gt__(self,other):
        return  self.student_grades() > other.student_grades()

    def __ge__(self,other):
        return  self.student_grades() >= other.student_grades()


    def get_fineshed_courses(self):
        courses = ""
        for key in self.finished_courses:
            if courses == "":
                courses += key
            else:
                courses += "," + key
        return courses


    def courses(self):
        courses = ""
        for key in self.grades:
            if courses == "":
                courses += key
            else:
                courses += "," + key
        return courses


    def rate_lection(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.lect_grades:
                lecturer.lect_grades[course] += [grade]
            else:
                lecturer.lect_grades[course] = [grade]
        else:
            return 'Ошибка'


    def __str__(self):
        some_student = f' Name : {self.name} \n Surname : {self.surname} \n Avarage grade per Homework: {self.student_grades()} \n Courses in process: {self.courses()} \n Finnished courses: {self.get_fineshed_courses()}'
        return some_student


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__ (self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.lect_grades = {}


    def lector_grades(self):
        avarage_grades = []
        for key in self.lect_grades:
            avarage_grades += self.lect_grades[key]
        avarage_grade = sum(avarage_grades)/len(avarage_grades)
        return avarage_grade


    def __lt__(self, other):
        return self.lector_grades() < other.lector_grades()

    def __le__(self, other):
        return self.lector_grades() <= other.lector_grades()

    def __gt__(self, other):
        return self.lector_grades() > other.lector_grades()

    def __ge__(self, other):
        return self.lector_grades() >= other.lector_grades()


    def __str__(self):
        some_lecturer = f' Name : {self.name} \n Surname : {self.surname} \n Avarage grade per lection: {self.lector_grades()}'
        return some_lecturer


class Reviewer(Mentor):
    def reviewer_info(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


    def __str__(self):
        some_reviewer = f' Name : {self.name} \n Surname : {self.surname}'
        return some_reviewer

some_lecturer1 = Lecturer('Some', 'Buddy')
some_lecturer2 = Lecturer('Some', 'Buddy')

best_student1 = Student('Ruoy', 'Eman', 'your_gender')
best_student2 = Student('Ruoy', 'Eman', 'your_gender')

best_student1.courses_in_progress += ['Python', 'Git']
best_student2.courses_in_progress += ['Python', 'Git']



cool_mentor = Reviewer("Some", "Buddy")
cool_mentor.courses_attached += ['Python']

some_lecturer1.courses_attached += ['Python']
some_lecturer2.courses_attached += ['Python']

cool_mentor.rate_hw(best_student1, 'Python', 9)
cool_mentor.rate_hw(best_student2, 'Python', 10)


best_student1.rate_lection(some_lecturer1, 'Python', 10)
best_student1.finished_courses += ['Programing for beginners']
best_student1.rate_lection(some_lecturer2, 'Python', 10)


best_student2.rate_lection(some_lecturer1, 'Python', 9)
best_student2.finished_courses += ['Programing for beginners']
best_student2.rate_lection(some_lecturer2, 'Python', 7)


print(best_student1)
print()
print(best_student2)
print()
print(some_lecturer2)
print()
print(some_lecturer1)
print()
print(cool_mentor)
print()
print()
print(some_lecturer1 > some_lecturer2)
print(best_student1 > best_student2)