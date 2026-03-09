class Ticket:
    def __init__(self, title, ticket_price, ticket_amount, language = "geo"):
        self.title = title
        self.ticket_price = ticket_price
        self.ticket_amount = ticket_amount
        self.language = language

        def __str__(self):
            print("random movie")
        def __lt__(self, other):
            other = self.ticket_amount
            if self.ticket_amount < other:
                print(f'{self.ticket_amount} is less then {other}')
            if self.ticket_amount <= 10:
                print("u can buy this")


class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def __str__(self):
        print(self.name, self.balance)

    def deposit(self, amount):
        self.balance += amount


movie1 = Ticket("spider-man2", 30, 8)
movie2 = Ticket("harry-potter", 40, 8)
user1 = User("tazo", 100)

