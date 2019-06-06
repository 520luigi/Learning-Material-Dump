import animal
import cat
import dog

def main():
    print("Making An Animal")
    A = animal.Animal
    print("Making A Dog")
    D = dog.Dog
    print("Making A Cat")
    C = cat.Cat

    A.speak()
    D.speak()
    C.speak()
    A.sleep()
    D.sleep()
    C.sleep()

if __name__ == "__main__":
    main()
