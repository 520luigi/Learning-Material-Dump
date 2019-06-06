#put your imports here
import first_class


#I wonder if this is just too much calling?? like is there a simpler version to doing this?
#not sure if the importing method is right...maybe try out different importing methods
#well at the very least, I think I am getting better at using python mains...
def main():
    #put your code here
    hello = first_class.FirstClass("First!")
    print(hello.message)

if __name__ == "__main__":
    main()
