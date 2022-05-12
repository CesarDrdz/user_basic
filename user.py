class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdraw (self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"{self.name}, balance: {self.account_balance}")
user1 = User("John", "John@dojo.com")
user2 = User("Greg", "Greg@ninja.com")
