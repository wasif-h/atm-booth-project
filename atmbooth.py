# Author : Wasif Hossain    Project : ATM BOOTH 
class Atm:

    def __init__(self):
        print("ATM BOOTH Project - Wasif Hossain")
        self.pin = input("Please Set your Pin >> ")
        self.click = 1
        self.balance = 500

    def menu(self):
        
        while True :
            self.click = int(input("""
                Press 1 : Check Balance
                Press 2 : Withdraw Balance
                Press 3 : Deposit Balance
                Press 4 : Change Pin
                Press 5 : Exit the Booth
                ------------------------------------
            """))
    
            if self.click == 1:
                self.check_balance()
            elif self.click == 2:
                self.withdraw()
            elif self.click == 3:
                self.deposit()
            elif self.click == 4:
                self.pin = input("Reset Your Pin : ")
                print("Your Pin is changed. Enjoy")
            else:
                print("Thank You Sir / Maam\nSee You Soon")
                break
                

    def pin_check(self):

        pin = input("Enter your pin : ")
        if pin == self.pin:
            return True
        else:
            return False

    def check_balance(self):
        if(self.pin_check()):
            print(f"Your Current Balance = {self.balance} BDT")
        else:
            print("Wrong Pin -- Try Again")

    def withdraw(self):
        if(self.pin_check()):
            temp = int(input("Enter Amount : "))
            self.balance -= temp
        else:
            print("Wrong Pin -- Try Again")

    def deposit(self):

        if(self.pin_check()):
            temp = int(input("Enter Amount : "))
            self.balance += temp
        else:
            print("Wrong Pin -- Try Again")
    


brac = Atm()
brac.menu()