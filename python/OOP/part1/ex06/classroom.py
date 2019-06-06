class Classroom:

    def __init__(self, teacher, students):
        capacity = 20
        self.capacity = capacity
        self.teacher = teacher
        self.students = students
        self.student_count = len(students)

    def get_info(self):
        print("This classroom has a standard capacity of {} and is run by {}. " \
        "It currently has {} students".format(self.capacity, self.teacher, self.student_count))
