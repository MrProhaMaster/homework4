class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __medium_mark__(self):
        summ = 0
        for i in self.grades:
            summ += sum(self.grades[i])//len(self.grades[i])
        return summ//len(self.grades)

    def __str__(self):
        b = str(self.__medium_mark__())
        return 'Имя: '+self.name+'\nФамилия: '+self.surname+'\nСредняя оценка за домашние задания: '+b+'\nКурсы в процессе изучения: '+', '.join(self.courses_in_progress)+'\nЗавершенные курсы: '+', '.join(self.finished_courses)+'\n'

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

    def __medium_mark__(self):
        summ = 0
        for i in self.lectures:
            summ += sum(self.lectures[i])//len(self.lectures[i])
        return summ//len(self.lectures)

    def __str__(self):
        b = str(self.__medium_mark__())
        return 'Имя: '+self.name+'\nФамилия '+self.surname+'\nСредняя оценка за лекции: '+b+'\n'

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

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_lecturer = Lecturer('Some', 'Person')
cool_lecturer.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

best_student.rate_L(cool_lecturer, 'Python', 10)
best_student.rate_L(cool_lecturer, 'Python', 10)
best_student.rate_L(cool_lecturer, 'Python', 10)

print(best_student.grades)
print(cool_lecturer.lectures)
print(cool_lecturer)
print(best_student)