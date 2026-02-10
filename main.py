class Bank:
    def __init__(self,name, balance):
        self.balance = balance
        self.name = name
        self.history = []
    def deposit(self):
        depo = int(input("How much do you want to deposit? "))
        if depo >= 0:
            self.balance += depo        
            self.history.append(f"Deposit {depo}")
            print(f"Deposit Successful, Current balance is {self.balance}")
    def withdraw(self):
        width = int(input("How much do you want to withdraw? "))
        if self.balance >= width:
            self.balance -= width
            self.history.append(f'Withdraw {width}')
            print(f"Successfull Withdrawal you current balance is {self.balance}")
        elif self.balance < width:
            print("Cannnot withdraw due to insuficient balance !")
    def view_history(self):
        print(f'ACCOUNT HISTORY of {self.name}\n{self.history}')



customer = Bank("Necolie",1000)
while True:
    
    print(f"Hello {customer.name}, Balance : {customer.balance}")
    print("Choose an option\n 1. Deposit | 2.Withdraw | 3.Check History | 4.Exit")
    choice = int(input("Choose an option (1-4) :"))

    if choice == 1:
        customer.deposit()
        print()
    elif choice == 2:
        customer.withdraw()
        print()
    elif choice == 3:
        customer.view_history()
        print()
    elif choice == 4:
        print()
        print ("BYE")
        break
    else:
        print("Invalid option")