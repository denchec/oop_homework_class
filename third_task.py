from main import Lecturer, Student, Reviewer

"""Проверяющие"""

some_reviewer = Reviewer('Some', 'Buddy')
print(some_reviewer)

"""Лекторы"""

student = Student('Алёхина', 'Ольга', 'Ж')
some_lecturer = Lecturer('Some', 'Buddy')
student.courses_in_progress += ['Python', 'Java']
some_lecturer.courses_attached += ['Python', 'Java']
student.rate_lecture(some_lecturer, 'Python', 10)
student.rate_lecture(some_lecturer, 'Java', 10)
student.rate_lecture(some_lecturer, 'Python', 10)
student.rate_lecture(some_lecturer, 'Java', 10)
student.rate_lecture(some_lecturer, 'Python', 10)
student.rate_lecture(some_lecturer, 'Java', 10)
student.rate_lecture(some_lecturer, 'Python', 10)
student.rate_lecture(some_lecturer, 'Java', 10)
student.rate_lecture(some_lecturer, 'Python', 10)
student.rate_lecture(some_lecturer, 'Java', 9)
print(some_lecturer)

"""Студенты"""

some_student = Student('Ruoy', 'Eman', 'M')
some_reviewer = Reviewer('Пётр', 'Петров')

some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['Введение в программирование']
some_reviewer.courses_attached += ['Python', 'Git']

some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Git', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Git', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Git', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Git', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Git', 9)
print(some_student)

"""Сравнение лекторов"""

student = Student('Алёхина', 'Ольга', 'Ж')
lecturer = Lecturer('Иван', 'Иванов')
some_lecturer = Lecturer('Some', 'Buddy')

student.courses_in_progress += ['Python']
lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['Python']

student.rate_lecture(lecturer, 'Python', 5)
student.rate_lecture(some_lecturer, 'Python', 10)
print(lecturer < some_lecturer)
print(lecturer > some_lecturer)
print(lecturer == some_lecturer)

"""Сравнение студентов"""

student = Student('Алёхина', 'Ольга', 'Ж')
some_student = Student('Ruoy', 'Eman', 'M')
reviewer = Reviewer('Пётр', 'Петров')

student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Python']
reviewer.courses_attached += ['Python']

reviewer.rate_hw(student, 'Python', 5)
reviewer.rate_hw(some_student, 'Python', 10)
print(student < some_student)
print(student > some_student)
print(student == some_student)
