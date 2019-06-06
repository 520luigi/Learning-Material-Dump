import classroom
import student
import teacher

def main():
    teacher1 = "Wesley"
    students1 = ["Alice", "Carol", "Eve"]
    c1 = classroom.Classroom(teacher1, students1)

    teacher2 = "Anand"
    students2 = ["Bob", "Dave"]
    c2 = classroom.Classroom(teacher2, students2)


    c1.get_info()
    c2.get_info()

    for x in students1:
        t = teacher.Teacher(teacher1, x)
        s = student.Student(teacher1, x)
        t.speak()
        s.speak()

    for y in students2:
        t = teacher.Teacher(teacher2, y)
        s = student.Student(teacher2, y)
        t.speak()
        s.speak()

if __name__ == "__main__":
    main()
