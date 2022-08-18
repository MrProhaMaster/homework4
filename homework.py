class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не студент!')
            return
        return self.__medium_mark__() < other.__medium_mark__()

    def __medium_mark__(self):
        summ = 0
        for i in self.grades:
            summ += sum(self.grades[i])//len(self.grades[i])
        return summ//len(self.grades)

    def __medium_mark_direct__(self, subject):
        return sum(self.grades[subject])//len(self.grades[subject])

    def __str__(self):
        return 'Имя: '+self.name+'\nФамилия: '+self.surname+'\nСредняя оценка за домашние задания: '+str(self.__medium_mark__())+'\nКурсы в процессе изучения: '+', '.join(self.courses_in_progress)+'\nЗавершенные курсы: '+', '.join(self.finished_courses)+'\n'

    def add_courses(self, course_name):
        self.finished_course.append(course_name)

    def rate_L(self, lecturer, lecture, grade):
        if isinstance(lecturer, Lecturer) and lecture in self.courses_in_progress and lecture in lecturer.courses_attached:
            if lecture in lecturer.lectures:
                lecturer.lectures[lecture] += [grade]
            else:
                lecturer.lectures[lecture] = [grade]
        else:
            return 'Ошибка'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        courses_attached = []
        self.lectures = {}

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не лектор!')
            return
        return self.__medium_mark__() < other.__medium_mark__()

    def __medium_mark__(self):
        summ = 0
        for i in self.lectures:
            summ += sum(self.lectures[i])//len(self.lectures[i])
        return summ//len(self.lectures)

    def __medium_mark_direct__(self, subject):
        return sum(self.lectures[subject])//len(self.lectures[subject])

    def __str__(self):
        return 'Имя: '+self.name+'\nФамилия '+self.surname+'\nСредняя оценка за лекции: '+str(self.__medium_mark__())+'\n'

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        courses_attached = []

    def __str__(self):
        return 'Имя: '+self.name+'\nФамилия: '+self.surname

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

def comparison_s(students, subject):
    summ = 0
    c = 0
    for student in students:
        if subject in student.grades:
            summ += student.__medium_mark_direct__(subject)
            c += 1
    return summ//c

def comparison_l(lecutrers, subject):
    summ = 0
    c = 0
    for lecturer in lecutrers:
        if subject in lecturer.lectures:
            summ += lecturer.__medium_mark_direct__(subject)
            c += 1
    return summ // c

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['GIT']

normal_student = Student('Ben', 'Stark', 'your_gender')
normal_student.courses_in_progress += ['Python']
normal_student.finished_courses += ['GIT']

bad_student = Student('Tony', 'Parker', 'your_gender')
bad_student.courses_in_progress += ['GIT']
bad_student.finished_courses += ['']

students = [best_student, normal_student, bad_student]

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_lecturer = Lecturer('Some', 'Person')
cool_lecturer.courses_attached += ['Python']

normal_lecturer = Lecturer('No', 'Name')
normal_lecturer.courses_attached += ['Python']

lecturers = [cool_lecturer, normal_lecturer]

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

cool_mentor.rate_hw(normal_student, 'Python', 9)
cool_mentor.rate_hw(normal_student, 'Python', 8)
cool_mentor.rate_hw(normal_student, 'Python', 7)

cool_mentor.rate_hw(bad_student, 'GIT', 6)
cool_mentor.rate_hw(bad_student, 'GIT', 4)
cool_mentor.rate_hw(bad_student, 'GIT', 5)

best_student.rate_L(cool_lecturer, 'Python', 10)
best_student.rate_L(cool_lecturer, 'Python', 10)
best_student.rate_L(cool_lecturer, 'Python', 10)

best_student.rate_L(normal_lecturer, 'Python', 7)
best_student.rate_L(normal_lecturer, 'Python', 8)
best_student.rate_L(normal_lecturer, 'Python', 6)

print(best_student.grades)
print(cool_lecturer.lectures)
print(cool_lecturer)
print(best_student)
print(cool_lecturer.__lt__(normal_lecturer))
print(comparison_s(students, 'Python'))
print(comparison_l(lecturers, 'Python'))