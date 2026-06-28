from main import Lecturer, Student, Reviewer

student_1 = Student('Алёхина', 'Ольга', 'Ж')
student_2 = Student('Ruoy', 'Eman', 'M')
lecturer_1 = Lecturer('Иван', 'Иванов')
lecturer_2 = Lecturer('Some', 'Buddy')
reviewer_1 = Reviewer('Пётр', 'Петров')
reviewer_2 = Reviewer('Denis', 'Chernykh')

student_1.courses_in_progress += ['Python', 'Git']
student_2.courses_in_progress += ['Python', 'Git']
lecturer_1.courses_attached += ['Python', 'Git']
lecturer_2.courses_attached += ['Python', 'Git']
reviewer_1.courses_attached += ['Python', 'Git']
reviewer_2.courses_attached += ['Python', 'Git']

reviewer_1.rate_hw(student_1, 'Python', 7)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_1, 'Python', 8)
print(reviewer_1)
reviewer_2.rate_hw(student_2, 'Python', 7)
reviewer_2.rate_hw(student_2, 'Python', 8)
reviewer_2.rate_hw(student_2, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Python', 10)
print(reviewer_2)

student_1.add_courses('Введение в программирование')
student_1.rate_lecture(lecturer_1, 'Python', 6)
print(student_1)
print(student_1 > student_2)
print(student_1 < student_2)
print(student_1 == student_2)

student_2.add_courses('Введение в программирование')
student_2.rate_lecture(lecturer_2, 'Python', 7)
print(student_2)
print(student_2 > student_1)
print(student_2 < student_1)
print(student_2 == student_1)

print(lecturer_1)
print(lecturer_1 > lecturer_2)
print(lecturer_1 < lecturer_2)
print(lecturer_1 == lecturer_2)


def average_students_grade(students: list[Student], course: str):
    grades_list = []
    for student in students:
        if not isinstance(student, Student):
            continue

        grades = student.grades.get(course, None)
        if grades is None:
            continue

        grades_list += grades

    if not grades_list:
        return 'Ошибка, у студентов нет оценок'

    return sum(grades_list) / len(grades_list)


def average_lecturers_grade(lecturers: list[Lecturer], course: str):
    grades_list = []
    for lecturer in lecturers:
        if not isinstance(lecturer, Lecturer):
            continue

        grades = lecturer.grades.get(course, None)
        if grades is None:
            continue

        grades_list += grades

    if not grades_list:
        return 'Ошибка, у лекторов нет оценок'

    return sum(grades_list) / len(grades_list)


print(average_students_grade([student_1, student_2], 'Python'))
print(average_lecturers_grade([lecturer_1, lecturer_2], 'Python'))
