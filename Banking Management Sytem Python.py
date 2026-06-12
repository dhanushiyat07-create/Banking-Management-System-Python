from datetime import datetime

class Account:
    
    def __init__(self):
        self.name=input("Enter Account Holder name:")
        self.acc_no=int(input("Enter the Account number:"))
        self.balance=float(input("Enter Initial Balance:"))
        self.pin_no=int(input("Enter PIN number:"))
        self.history=[]
        self.is_locked=False
        self.wrong_attempts=0
        self.Max_attempts=3
        print("New Account Created")
        
#----------------------------------------------------------------------------------------
#check pin
#----------------------------------------------------------------------------------------
        
    def check_pin(self):
         if self.is_locked:
             print("Account locked")
             return False
         pin=int(input("Enter pin:"))
         if pin==self.pin_no:
            self.wrong_attempts=0
            return True
         else:
            self.wrong_attempts+=1
            print(f"wrong PIN!{3-self.wrong_attempts}tries left")
            if self.wrong_attempts>=3:
                self.is_locked=True
                print("Locked! 3 wrong tries!")
            return False
        
#----------------------------------------------------------------------------------------
#deposit
#----------------------------------------------------------------------------------------
            
    def deposit(self):
        amount=float(input("Enter amount to deposit:"))
        if not self.check_pin():
            return
        old_balance=self.balance
        self.balance+=amount
        now=datetime.now()
        self.history.append(f"{now.strftime('%d-%m-%y %H:%M:%S')}|"f"deposit={amount}|old balance={old_balance}|\n====Total Balance={self.balance}=====") 
        print("Accepted")
        print("deposited successully")
        print("Current balance:",self.balance)

#----------------------------------------------------------------------------------------
#withdraw
#----------------------------------------------------------------------------------------
            
    def withdraw(self):
        amount=float(input("Enter amount to withdraw:"))
        if not self.check_pin():
             return
        if amount>self.balance:
            print("Insufficient Balance")
        else:
            old_balance=self.balance
            self.balance-=amount
            now=datetime.now()
            self.history.append(f"{now.strftime('%d-%m-%y %H:%M:%S')}|"f"withdraw={amount}|old balance={old_balance}|\n====Total Balance={self.balance}=====")
            print("Accepted")
            print("withdrawal successfully")
            print("Current balance:",self.balance)

#----------------------------------------------------------------------------------------
#deposit
#----------------------------------------------------------------------------------------
            
    def enquiry(self):
        if not self.check_pin():
            return
        print("Accepted")
        print("Account Holder Name:",self.name)
        print("Account number:",self.acc_no)
        print("Current balance:",self.balance) 

#----------------------------------------------------------------------------------------
#Transaction_history
#----------------------------------------------------------------------------------------
    def show_history(self):
        if not self.check_pin():
            return
        print("Accepted")
        print("-"*30)
        print("** Transaction history **")
        print("-"*30)
        for i in self.history:
             print(i)
    def change_pin(self):
        old_pin=int(input("Enter Old PIN:"))
        if old_pin==self.pin_no:
            new_pin=int(input("Enter New PIN:"))
            confirm_pin=int(input("Confirm new PIN:"))
            if new_pin==confirm_pin:
                self.pin_no=new_pin
                print("PIN changed successfully")
            else:
                print("PIN does not match")
        else:
            print("Incorrect OLD PIN")
                
amount=Account()

#----------------------------------------------------------------------------------------
#Main program
#----------------------------------------------------------------------------------------

while True:
    print("**========BANK MENU========**")
    print("1.deposit")
    print("2.withdraw")
    print("3.Balance")
    print("4.View Transactions")
    print("5.Change PIN")
    print("6.Exit")
    choice=input("Enter choice:") 
    if choice=="1":
        amount.deposit()
    elif choice=="2":
        amount.withdraw()
    elif choice=="3":
        amount.enquiry()
    elif choice=="4":
        amount.show_history()
    elif choice=="5":
        amount.change_pin()
    elif choice=="6":
        print("Thank you for using bank system")
        break
    else:
        print("Invalid choice")


