import greeter
import insult_comic

def main():
    greet = greeter.Greeter("Wesley")
    insult = insult_comic.InsultComic("Wesley")

    greet.speak()
    insult.speak()

if __name__ == "__main__":
    main()
