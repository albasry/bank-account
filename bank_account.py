from datetime import datetime


class BankAccount:  # Parent Class
    _bank_name = 'Al-basri Bank'     # Class Attribute & Access Modifier '_Protected'
    __balance = 0.0000      # Class Attribute & Access Modifier '_ _Private'

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_balance(self):    # Getter
        return self.__balance

    def set_balance(self, edit_balance):    # Setter
        self.__balance = edit_balance

    def checking(self):
        print(f'\n Net Available Balance: {self.get_balance():,.2f} $ \n')

    def depositing(self):
        amount = float(input('\n Enter amount to be Deposited: '))
        now = datetime.now().strftime('%d %B %Y, %I:%M %p')
        today = datetime.today().strftime('%A')
        if amount > 0:
            net_balance = self.get_balance() + amount
            self.set_balance(net_balance)
            print(f'\n Amount Deposited: {amount:,.2f} $ \n\n at {today} {now} \n')
        else:
            print('Invalid input!')

    def set_withdraw(self):
        amount = float(input('\n Enter amount to be Withdrawn: '))
        now = datetime.now().strftime('%d %B %Y, %I:%M %p')
        today = datetime.today().strftime('%A')
        if self.get_balance() >= amount > 0:
            net_balance = self.get_balance() - amount
            self.set_balance(net_balance)
            print(f'\n Amount Withdrawn: {amount:,.2f} $ \n\n {today} {now} \n')
        else:
            print('\n Insufficient balance on account! \n')


class CreateAccount(BankAccount):   # Child Class
    def welcoming(self):
        print(f'\n===== Welcome to {self._bank_name} =====\n')
        print(f'Good Day. {self.name} {self.surname}\n')
        print(f'Your balance is: {self.get_balance():,.2f} $\n')


first_name = input('\nEnter your first name: ')
last_name = input('\nEnter your last name: ')
account_created = CreateAccount(name=first_name, surname=last_name)
account_created.welcoming()

while True:
    decision = input('Enter from the options (Check, Deposit, Withdraw or Exit): ').lower()
    try:
        if decision == 'check':
            account_created.checking()
        elif decision == 'deposit':
            account_created.depositing()
        elif decision == 'withdraw':
            account_created.set_withdraw()
        elif decision == 'exit':
            break
        else:
            raise ValueError
    except ValueError:
        print('Invalid input!')
