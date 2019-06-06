class Student:
    def __init__(self, teacher, student):
        self.teacher = teacher
        self.student = student
    def speak(self):
        print("{}: Good morning, {}".format(self.student, self.teacher))
