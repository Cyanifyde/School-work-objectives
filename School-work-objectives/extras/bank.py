class bank():
    def __init__(self, ammount: float):
        self.ammount: float = ammount

    def withdraw(self, ammount: float):
        self.ammount=(self.ammount-ammount)if(not ammount>self.ammount)else self.ammount
        print("there is £{} in your bank".format(self.ammount))


bankammount = bank(ammount = 1100)

bankammount.withdraw(ammount = int(input("please input how mich money you want to withdraw\n")))
