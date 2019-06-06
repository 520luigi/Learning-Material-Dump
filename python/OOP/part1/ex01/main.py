import cellphone

#don't put () around a class if there are no inputs, else you create 1 extra input of nothing...
#example: if i had myphone = cellphone.Cellphone(), then I couldn't call myphone.call(), etc
def main():
    myphone = cellphone.Cellphone
    myphone.call()
    myphone.text()
    myphone.drop()

if __name__ == "__main__":
    main()
