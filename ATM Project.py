class atm:
    def __init__(self):
        self.pin = 1396
        self.balance = 1000
        
        self.menu()
        
    def menu(self):
        user_input=input("""
        Hello, how would you like to proceed?
        1.Enter 1 to change pin
        2.Enter 2 to deposit
        3.Enter 3 to withdraw
        4.Enter 4 to check balance
        5.Enter 5 to exit
        """)
        if(user_input=='1'):
            self.change_pin()
        elif(user_input=='2'):
            self.deposit()
        elif(user_input=='3'):
            self.withdraw()
        elif(user_input=='4'):
            self.check_balance()
        else:
            self.exit()
        
    def change_pin(self):
        temp=int(input("Enter your previous pin :"))
        if(self.pin==temp):
          pin=input("Enter new pin :")
          self.pin=pin
          print("Pin set sucessfully")
        else:
            print("""You Entered Wrong Pin
            
            """)
            self.change_pin()
          
    def deposit(self):
        temp=int(input("Enter your pin :"))
        if(self.pin==temp):
            balance=int(input("Enter amount to be deposited : "))
            print("Amount deposited sucessfully!")
            self.balance+=balance
            print("Remaining balance :",self.balance)
        else:
            print("""You Entered Wrong Pin
            
            """)
            self.deposit()
            
    def withdraw(self):
        temp=int(input("Enter your pin :"))
        if(self.pin==temp):
          withdraw=int(input("Enter amount to be withdrawn : "))
          if(self.balance>=withdraw):
              print("Amount withdrawn sucessfully!")
              self.balance =self.balance-withdraw
              print("Remaining balance :",self.balance)
          else:
              print("Sorry Not Sufficient Balance!")
        else:
            print("""You Entered Wrong Pin
            
            """)
            self.withdraw()
            
    def check_balance(self):
        temp=int(input("Enter your pin :"))
        if(self.pin==temp):
            print("Your Account Balance is :",self.balance)
        else:
            print("""You Entered Wrong Pin
            
            """)
            self.check_balance()
            
    def exit(self):
        print("""
        Thank You For Using Our Service
        Please Visit Again!!
        """)
    
obj=atm()
