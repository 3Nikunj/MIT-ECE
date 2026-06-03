class Operations:
    def __init__(self,ac, bal, pin): 
        self._balance = bal
        self.__pin = pin
        self.__account = ac
    
    def deposite (self, amt):
        self._balance += amt
        print("updated balance after deposite:", self._balance)

    def withdraw (self, amt):
        self._balance -= amt
        print("updated balance after withdraw:", self._balance)
    
    def get_balance (self):
        return self._balance

    def change_pin (self, new_pin):
        self.__pin = new_pin

    def diplay(self):
        print("account:", self.__account, "balance:", self._balance
        , "pin:", self.__pin)

class SBI (Operations):
    def __init__(self,ac, bal, pin):
        super().__init__(ac, bal, pin)

class Kotak (Operations):
    pass

class Axis (Operations):
    pass

class UnionBank (Operations):
    pass


print("Available Banks")
print("1.SBI")
print("2.Kotak")
print("3.Axis")
print("4.UnionBank") 

choice = int(input("Enter your Bank: "))
if choice == 1:
    ac = int(input("Enter your Account Number: "))
    bal = int(input("Enter your Balance: "))
    pin = int(input("Enter your PIN: "))
    myAccount = SBI(ac, bal, pin)
elif choice == 2:
    ac = int(input("Enter your Account Number: "))
    bal = int(input("Enter your Balance: "))
    pin = int(input("Enter your PIN: "))
    myAccount = Kotak(ac, bal, pin)
elif choice == 3:
    ac = int(input("Enter your Account Number: "))
    bal = int(input("Enter your Balance: "))
    pin = int(input("Enter your PIN: "))
    myAccount = Axis(ac, bal, pin) 
elif choice == 4:
    ac = int(input("Enter your Account Number: "))
    bal = int(input("Enter your Balance: "))
    pin = int(input("Enter your PIN: "))
    myAccount = UnionBank(ac, bal, pin)

while True:
    print("1.Deposite")
    print("2.Withdraw")
    print("3.Get Balance")
    print("4.Change PIN")
    print("5.Display")
    ops = int(input("Enter your Operation: "))
    if ops == 1: 
        deposite_amt = int(input("Enter the amount to deposite: "))
        myAccount.deposite(deposite_amt)
    else:
        break
