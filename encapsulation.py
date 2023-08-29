# Public Members (Default):
# Public members are accessible from anywhere, both inside and outside the class.
# They are not prefixed with any underscore.
class MyClass:
    def __init__(self):
        self.public_var = 10  # Public variable

    def public_method(self):
        return "This is a public method"
    
# Protected Members (_prefix):
# Protected members should not be accessed directly from outside the class, 
# but Python does not enforce this. Instead, it uses a naming convention with a single 
# underscore prefix (e.g., _variable or _method) to indicate that a member should be treated 
# as protected.

class MyClass:
    def __init__(self):
        self._protected_var = 20  # Protected variable

    def _protected_method(self):
        return "This is a protected method"
myclass = MyClass()
print(myclass._protected_method())

# Private Members (__prefix):
# Private members should not be accessed from outside the class, and Python provides 
# some level of name mangling to make it harder to access these members. 
# Private members are indicated by a double underscore prefix (e.g., __variable or __method).
class MyClass:
    def __init__(self):
        self.__private_var = 30  # Private variable

    def __private_method(self):
        return "This is a private method"
myclass = MyClass()
# print(myclass.__private_method()) Can't access __private_method



class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

class HDFCBank(BankAccount):
    def __init__(self, account_number,balance):
        super().__init__(account_number,balance)
        self._account_number = account_number

account = BankAccount("123456", 1000)
account.deposit(500)
account.withdraw(200)
print("Account balance:", account.get_balance())
hdfc =HDFCBank("123456",1000)
print(hdfc.get_balance())
