import building
import campus

def main():
    b1 = building.Building("Math Building", 25)
    b2 = building.Building("Science Building", 17)

    b1.get_info()
    b2.get_info()

    #this is pretty cool, so I can create an empty list with [], and append it with
    #other objects as a parameter!! WHAHAHAHA
    c = campus.Campus([], 0, 0)
    c.get_info() #wanted to see output of campus with nothing in it 
    c.add_building(b1)
    c.add_building(b2)
    c.get_info()

if __name__ == "__main__":
    main()
