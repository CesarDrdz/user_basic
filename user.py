
# chaining method isn't working so we need to figuer out why! user bank account 

class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdraw (self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self, amount):
        print(f"{self.name}, balance: {self.account_balance}")
        return self
        
    # def make_transfer (self, amount)
        # self.make_transfer -= amount


user1 = User("John", "John@dojo.com")
user2 = User("Greg", "Greg@ninja.com")


# chaining method isn't working so we need to figuer out why!