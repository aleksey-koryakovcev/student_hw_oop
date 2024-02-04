"""Логика работы с информацией о студентах
в учебном заведении в парадигме ООП"""

class Student:
    """Описание класса студентов.
    Содержит атрибуты: имя, фамилия."""
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade = float()

    def add_courses(self, course_name):
        """Добавляет курсы, которые студент уже прошел"""
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        """Выставляет оценки лекторам за лекции"""
        if isinstance(lecturer,Lecturer)\
            and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        if not self.grades:
            return 0
        grade_list = []
        for grades_list in self.grades.values():
            grade_list.extend(grades_list)
        average_grade = sum(grade_list) / max(len(grade_list), 1)
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашнее задание: {average_grade}\n' \
               f'Курсы в процессе обучения: {courses_in_progress_string}\n' \
               f'Завершенные курсы: {finished_courses_string}'

    def __lt__(self, students):
        if not isinstance(students, Student):
            return 'Некорректное сравнение'
        return self.average_grade < students.average_grade

class Mentor:
    """Родительский класс, содержит атрибуты: имя, фамилия"""
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Reviewer(Mentor):
    """Реализует возможность выставления оценки студенту за домашние задания,
    если этот проверяющий закреплен за этим студентом по данному курсу"""

    def rate_hw(self, student, course, grade):
        """Реализует выставление оценок студетам за домашние задания"""
        if isinstance(student, Student)\
            and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\n Фамилия: {self.surname}'

class Lecturer(Mentor):
    """У преподавателей есть закрепленный за ними список курсов.
    Выводит среднюю оценку за лекциюю"""
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_grade_lect = float()

    def __str__(self):
        if not self.grades:
            return 0
        grade_list = []
        for grades_list in self.grades.values():
            grade_list.extend(grades_list)
        average_grade_lect = sum(grade_list) / max(len(grade_list), 1)
        return f'Имя: {self.name}\n'\
               f'Фамилия: {self.surname}\n'\
               f'Средняя оценка за лекции: {average_grade_lect}'

    def __lt__(self, lecturers):
        if not isinstance(lecturers, Lecturer):
            return 'Некорректное сравнение'
        return self.average_grade_lect < lecturers.average_grade_lect

best_lecturer_1 = Lecturer('Иван', 'Петров')
best_lecturer_1.courses_attached += ['Python']

best_lecturer_2 = Lecturer('Петр', 'Алексеев')
best_lecturer_2.courses_attached += ['C++']

best_lecturer_3 = Lecturer('Семен', 'Зверев')
best_lecturer_3.courses_attached += ['Python']

cool_reviewer_1 = Reviewer('Павел', 'Павлов')
cool_reviewer_1.courses_attached += ['Python']
cool_reviewer_1.courses_attached += ['C++']

cool_reviewer_2 = Reviewer('Mila', 'Winter')
cool_reviewer_2.courses_attached += ['Python']
cool_reviewer_2.courses_attached += ['C++']

student_1 = Student('Ruoy', 'Eman')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Emma', 'Joys')
student_2.courses_in_progress += ['C++']
student_2.finished_courses += ['Введение в программирование']

student_3 = Student('Fillip', 'Kan')
student_3.courses_in_progress += ['Python']
student_3.finished_courses += ['Основы Python']

student_1.rate_lecturer(best_lecturer_1, 'Python', 10)
student_1.rate_lecturer(best_lecturer_1, 'Python', 8)
student_1.rate_lecturer(best_lecturer_1, 'Python', 10)

student_1.rate_lecturer(best_lecturer_2, 'С++', 8)
student_1.rate_lecturer(best_lecturer_2, 'С++', 7)
student_1.rate_lecturer(best_lecturer_2, 'С++', 9)

student_2.rate_lecturer(best_lecturer_2, 'С++', 10)
student_2.rate_lecturer(best_lecturer_2, 'С++', 8)
student_2.rate_lecturer(best_lecturer_2, 'С++', 9)

student_3.rate_lecturer(best_lecturer_3, 'Python', 9)
student_3.rate_lecturer(best_lecturer_3, 'Python', 8)
student_3.rate_lecturer(best_lecturer_3, 'Python', 6)

cool_reviewer_1.rate_hw(student_1, 'Python', 10)
cool_reviewer_1.rate_hw(student_1, 'Python', 8)
cool_reviewer_1.rate_hw(student_1, 'Python', 9)

cool_reviewer_2.rate_hw(student_2, 'С++', 5)
cool_reviewer_2.rate_hw(student_2, 'С++', 8)
cool_reviewer_2.rate_hw(student_2, 'С++', 7)

cool_reviewer_2.rate_hw(student_3, 'Python', 8)
cool_reviewer_2.rate_hw(student_3, 'Python', 7)
cool_reviewer_2.rate_hw(student_3, 'Python', 9)

list_student = [student_1, student_2, student_3]
list_lecturer = [best_lecturer_1, best_lecturer_2, best_lecturer_3]

def student_rating(list_student, course_name):
    """Подсчет средней оценки за домашние задания по всем студентам
    в рамках конкретного курса (в качестве аргументов
    принимает список студентов и название курса"""
    count_all = []
    sum_all = 0
    for student in list_student:
        if course_name in student.courses_in_progress:
            if course_name in student.grades:
                count_all.extend(student.grades[course_name])
    sum_all = sum(count_all)
    return  sum_all / max(len(count_all), 1)

def lecturer_rating(list_lecturer, course_name):
    """Подсчет средней оценки за лекции всех лекторов
    в рамках курса (в качестве аргумента принимает
    список лекторов и название курса)"""
    count_all = []
    sum_all = 0
    for lecturer in list_lecturer:
        if course_name in lecturer.courses_attached:
            if course_name in lecturer.grades:
                count_all.extend(lecturer.grades[course_name])
    sum_all = sum(count_all)
    return  sum_all / max(len(count_all), 1)

print(f'Студенты:\n\n{student_1.__str__()}\n\n{student_2.__str__()}\n\n{student_3.__str__()}')
print()
print(f'Лекторы:\n\n{best_lecturer_1.__str__()}\n'\
      f'\n{best_lecturer_2.__str__()}\n\n{best_lecturer_3.__str__()}')
print(f'Результат сравнения студентов: '
      f'{student_1.name} {student_1.surname} < {student_2.name} {student_2.surname} = \
        {student_1 > student_2}')
print(f'Результат сравнения лекторов: '
      f'{best_lecturer_1.name} {best_lecturer_1.surname} < {best_lecturer_2.name} \
        {best_lecturer_2.surname} = {best_lecturer_1 > best_lecturer_2}')
print(f"Средняя оценка для всех студентов по курсу {'C++'}: {student_rating(list_student, 'C++')}")
print(f"Средняя оценка для всех лекторов по курсу {'Python'}: \
      {lecturer_rating(list_lecturer, 'Python')}")
