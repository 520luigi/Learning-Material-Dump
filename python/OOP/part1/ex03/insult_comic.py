class InsultComic:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("I'd say it's good to see you {}, but I'd be lying...".format(self.name))
