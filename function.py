class Bank:
    bankname='BANK OF INDIA'
    branchname='BARODA'
    #Create bank account
    def __init__(self, name, pan, phno, address):
        self.name=name
        self.pan=pan
        self.phno=phno
        self.address=address
        self.balance=0.0
        print(f'Mr/Ms. {self.name}, Congrats!! Your account created sucessfully')

    #Deposite Amount
    def deposit(self, amount):
        self.balance=self.balance+amount
        print(f'Hi, Mr/Ms.{self.name}, {amount} is deposited successfully')
    #Withdraw Amount
    def withdraw(self, amount):
        if self.balance>amount:
            self.balance=self.balance-amount
            print(f'Hi, Mr/Ms.{self.name}, {amount} is withdrawn  successfully')
        else:
            print('Insufficient fund in your account')
    #Balance Enquirey
    def BalanceEnq(self):
        print(f'Mr/Ms. {self.name}, your account balance is: {self.balance}')

print(f'WELCOME TO {Bank.bankname}, {Bank.branchname}')
name=input('Enter you Name:')
pan=input('Enter you Pan No:')
phno=int(input('Enter you Phno:'))
address=input('Enter you Address:')

b=Bank(name, pan, phno, address)
while True:
    option=int(input('Select any option\n1. Deposite\n2. Withdraw\n3. Balance Enq\n4. Exit\n'))
    if option==1:
        amount=float(input('Enter amount to be deposited: '))
        b.deposit(amount)
    elif option==2:
        amount=float(input('Enter amount to be Withdra: '))
        b.withdraw(amount)
    elif option==3:
        b.BalanceEnq()
    elif option==4:
        print(f'Thanks for choosing {Bank.bankname}, {Bank.branchname}')
        break
    else:
        print('Vaild input')