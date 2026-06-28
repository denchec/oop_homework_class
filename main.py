from utils import average_grade


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecture(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in self.courses_in_progress
                and course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        average_g = average_grade(self.grades)

        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {average_g}\n'
                f'Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')

    def __lt__(self, other):
        average_g_first = average_grade(self.grades)
        average_g_second = average_grade(other.grades)

        return average_g_first < average_g_second

    def __gt__(self, other):
        average_g_first = average_grade(self.grades)
        average_g_second = average_grade(other.grades)

        return average_g_first > average_g_second

    def __eq__(self, other):
        average_g_first = average_grade(self.grades)
        average_g_second = average_grade(other.grades)

        return average_g_first == average_g_second


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        average_g = average_grade(self.grades)

        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {average_g}')

    def __lt__(self, other):
        average_g_first = average_grade(self.grades)
        average_g_second = average_grade(other.grades)

        return average_g_first < average_g_second

    def __gt__(self, other):
        average_g_first = average_grade(self.grades)
        average_g_second = average_grade(other.grades)

        return average_g_first > average_g_second

    def __eq__(self, other):
        average_g_first = average_grade(self.grades)
        average_g_second = average_grade(other.grades)

        return average_g_first == average_g_second


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) \
                and course in self.courses_attached \
                and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')
