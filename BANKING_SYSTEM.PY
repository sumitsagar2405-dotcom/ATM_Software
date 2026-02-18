class Banking:
    counter=1
    def __init__(self):
        self.__balance=0
        self.__pin=''
        self.cid=0
        self.cid=Banking.counter
        Banking.counter=Banking.counter + 1
        self.menu()

    def menu(self):
        op=input("""Hi, your welcome in xyz bank
        1. press 1 for your bank balance
        2. press 2 for balance check
        3. press 3 for pin change
        4. press 4 for widraw
        5. press 5 for deposite
        6. pres 6 to creat a pin
        6. press anything else for exit
        """)

        
        if op=='2':
            self.check_balance()
        elif op=='3':
            self.pin_change()
        elif op=='4':
            self.widraw()
        elif op=='5':
            self.deposit()
        elif op=='1':
            self.balance_add()
        elif op=='6':
            self.creat()
        else:
            exit
    

    def check_balance(self):
        print("your current balance :", self.__balance)
        self.menu()


    def pin_change(self):
        old_pin=input("enter old pin :")
        if old_pin==self.__pin:
            pin=input("emter new pin")
            self.__pin=pin
            print("pin changed sucessfully")
        else:
            print('worng pin! try again')
        self.menu()


    def widraw(self):
        pin_now=(input("enter pin"))
        if self.__pin==pin_now:
            amount=int(input("emter the amount you want to widrawl :"))
            if amount<=self.__balance:
                self.__balance=self.__balance-amount
                print('widrawl sucessfully')
                print("your current amount :",self.__balance)
            else:
                print('not enough amount!')
        else:
            print('worng pin! try agian')
        self.menu()


    def deposit(self):
        amount=int(input("enter the amount : "))
        self.__balance=self.__balance+amount
        print('widrawl succesfull')
        print("your curent amount : ",self.__balance)
        self.menu()


    def balance_add(self):
        pin=input("enter your pin ")
        if pin==self.__pin:
            amount=int(input("entr your balance a:"))
            self.__balance=amount
        else:
            print('worng pin')
        self.menu()


    def creat(self):
        pin_pin=input("enter your pin :")
        again_pin=input('enter pin again to varify :')
        if pin_pin==again_pin:
            self.__pin=again_pin
            print('pin created sucessfully')
        else:
            print("try again")
        self.menu()

