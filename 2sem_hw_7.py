books = [
    {"title": "1984", "author": "George Orwell", "pages": 328},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "pages": 281},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "pages": 180},
    {"title": "Moby Dick", "author": "Herman Melville", "pages": 635},
    {"title": "Brave New World", "author": "Aldous Huxley", "pages": 268},
]
# Завдання 1.
# 	1.	Відсортуй книги за кількістю сторінок.
# 	2.	Виведи список назв книг (title) за допомогою map().
# 	3.	Відсортуй книги за довжиною прізвища автора, потім за назвою книги в алфавітному порядку.

def sort_by_pages(item):
    pages = item["pages"]
    return pages

def sort_by_title(item):
    title = item["title"]
    return title

def sort_by_surname_length_and_alphabet(item):
    surname = item["author"].split()[-1]
    return len(surname), item["title"]

sorted_pages = sorted(books, key=sort_by_pages)
# 	print(sorted_pages)

sorted_titles = list(map(sort_by_title, books))
# 	print(sorted_titles)

sorted_books = sorted(books, key=sort_by_surname_length_and_alphabet)
# 	print(sorted_books)
################################################################################################################

students = [
    {
        "name": "Olena",
        "age": 19,
        "grades": {
            "math": 95,
            "physics": 88,
            "literature": 78
        }
    },
    {
        "name": "Andrii",
        "age": 20,
        "grades": {
            "math": 82,
            "physics": 91,
            "literature": 85
        }
    },
    {
        "name": "Sofiia",
        "age": 18,
        "grades": {
            "math": 99,
            "physics": 84,
            "literature": 90
        }
    },
    {
        "name": "Ivan",
        "age": 21,
        "grades": {
            "math": 70,
            "physics": 73,
            "literature": 68
        }
    },
    {
        "name": "Kateryna",
        "age": 20,
        "grades": {
            "math": 88,
            "physics": 92,
            "literature": 81
        }
    }
]
# Завдання 2
# 	1.	Відсортуй студентів за оцінкою з фізики.
# 	2.	Отримай список середніх оцінок кожного студента.
# 	3.	Відсортуй студентів за середнім балом.

print("------------------------------------------------------------------------")

def sort_by_physics_grade(item):
    grades = item["grades"]["physics"]
    return grades

def sort_by_grades(item):
    math_grades = item["grades"]["math"]
    physics_grades = item["grades"]["physics"]
    literature_grades = item["grades"]["literature"]
    list = [math_grades, physics_grades, literature_grades]
    return list

def sort_by_average_grade(item):
    math_grades = item["grades"]["math"]
    physics_grades = item["grades"]["physics"]
    literature_grades = item["grades"]["literature"]
    average = round((math_grades + physics_grades + literature_grades)/3, 2)
    return average

sorted_physics_grade = sorted(students, key=sort_by_physics_grade)
# 	print(sorted_physics_grade)

sorted_grades = tuple(map(sort_by_grades, students))
# 	print(sorted_grades)

average_grade = tuple(map(sort_by_average_grade, students))
sorted_average_grade = sorted(average_grade)
# 	print(sorted_average_grade)
