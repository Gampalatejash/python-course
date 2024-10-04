class bankaccount():
    def __init__(self,name,account_no,ifsc_code,balance):
        self.name=name
        self.account_no=account_no
        self.ifsc_code=ifsc_code
        self.balance=balance
    def deposit(self,amount)    :
        if amount>0:
            self.balance+=amount
            return f'dipositted amount is $ {amount} and your current balance is $ {self.balance}'
        else :
           return f'invalid amount depositted'
    def withdraw (self,amount):
        if 0<amount<=self.balance:
            self.balance-=amount
            return f'withdraw amount is $ {amount} and your current balance is $ {self.balance}'
        else:
            return f'insuffient funds or invalid entered '
    def balance_check (self) :
        return f'account holder name : {self.name}\n account no. is : {self.account_no}\n ifsc code is : {self.ifsc_code}\ncurrent balance is : {self.balance}'
bank= bankaccount  ('tejash',26928626754257,'VHSGJS',986324)

print(bank.balance_check())