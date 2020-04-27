class Movie:

    def __init__(self, name):
        self.name = name
        self.cost = 2

    def buy_ticket(self, amount):
        """
        Calculates the price of all the tickets the user bought.
        Updates the cost of the ticket accordingly.
        :param amount: Number of ticket purchased
        :return: The price of all the tickets
        """
        # The total price can be reduced to a singular equation
        total_amount = amount * self.cost + 2 * sum(range(amount))
        self.cost = self.cost + 2 * amount
        return total_amount


movies_catalog = [Movie('Wonder Woman 1984'), Movie('James Bond No Time To Die'), Movie('Black Widow')]
username = ''


while username != 'quit':
    username = input('Type your name (type "quit" to quit) - ')
    chosen_movie = ''
    price = 0
    if username != 'quit':
        ticket_count = int(input('Hello {}, how many tickets would you like to purchase: '.format(username)))
        # To add - check valid input
        print('Now pick a movie: ')
        for movie in movies_catalog:
            print(movie.name + ', Price - {}$'.format(movie.cost))
        input_movie = input()
        for movie in movies_catalog:
            if movie.name == input_movie:
                chosen_movie = movie
                movie.buy_ticket(ticket_count)
        print(chosen_movie)
        print(movie.cost)