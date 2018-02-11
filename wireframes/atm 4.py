balance1 = 500
balance2 = 1000
request = 277
atm1 = ATM(balance1, "Smart Bank")
atm2 = ATM(balance2, "Baraka Bank")

class atm:
 def __init__(self, balance, bank_name):
        self.withdrawals_list = []
        self.bank_name = bank_name

    print "current balance 500 "

    if request > balance:
       print("Can't give you all this money !!")

    elif request < 0:
         print("More than zero plz!")

    else:
        while request > 0:

            if request >= 100:
                request -= 100
                print("give 100")

            elif request >= 50:
                request -= 50
                print("give 50")

            elif request >= 10:
                request -= 10
                print("give 10")

            elif request >= 5:
                request -= 5
                print("give 5")

            elif request < 5:
                print("give " + str(self.balance))
                request = 0

    def show_withdrawals(self):
            for withdrawal in self.withdrawals_list:
                print(withdrawal)

        return balance - request
print "current balance", balance - request
balance = withdraw(balance, 277)
balance = withdraw(balance, 30)
balance = withdraw(balance, 5)
balance = withdraw(balance, 500)
