class Teacher:
    def __init__(self, teacher, student):
        self.teacher = teacher
        self.student = student
    def speak(self):
        print("{}: Welcome to class, {}".format(self.teacher, self.student))
