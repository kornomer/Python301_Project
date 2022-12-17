
class Bank_Account:

    def __init__(self, initial_amount= 0):
        self.balanced = initial_amount

    def log_transaction(self, transaction):
        with open('bank_account.txt', 'a') as file:
            file.write(f"{transaction}\n")    

    def withdrawal(self, amount):
       try: 
         amount = int(amount)
       except ValueError:
         amount = 0
       if amount:
         self.balanced -= amount
         self.log_transaction(f"Withdrew {amount}")


    def deposit(self, amount):
        try:
           amount = int(amount)
        except ValueError:
            amount = 0  
        if amount:
         self.balanced += amount
         self.log_transaction(f"Deposited {amount}")
        

account = Bank_Account(0)

while True:

    operation = input("What operation do you want to make?")
    if operation in ["withdrawal", "deposit"]:
         if operation == "withdrawal":
           amount = input("How much do you want to take out?")
           account.withdrawal(amount)
         else:
            amount = input("How much do you want to put in?")
            account.deposit(amount)
    else:
        print("This is not a valid operation")
    print(f"Your Balance is: {account.balanced}")        