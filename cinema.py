class Movie:

    cost = 2

    def __init__(self, name):
        self.name = name

    def buy_ticket(self):
        self.cost += 2
