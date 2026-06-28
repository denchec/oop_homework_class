def average_grade(grades):
    sum_grades = 0
    len_grades = 0
    for grade in grades.values():
        sum_grades += sum(grade)
        len_grades += len(grade)

    return sum_grades / len_grades
