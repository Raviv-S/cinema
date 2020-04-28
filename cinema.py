class Movie:

    def __init__(self, name):
        self.name = name
        self.cost = 2

    def buy_ticket(self, amount):
        """
        Calculates the price of all the tickets the user bought and updates the cost of the ticket accordingly.
        :param amount: Number of ticket purchased
        :return: The price of all the tickets
        """
        # The total price here reduced to a singular equation
        total_amount = amount * self.cost + 2 * sum(range(amount))
        self.cost = self.cost + 2 * amount
        return total_amount


def main():
    movies_catalog = [Movie('Wonder Woman 1984'), Movie('James Bond No Time To Die'), Movie('Black Widow')]
    username = ''
    cinema_revenue = 0
    while username != 'quit':
        username = input('Welcome! What\'s your name? (type "quit" to quit) - ')
        if username != 'quit':
            ticket_count = input('Hello {}, How many tickets would you like to purchase: '.format(username))
            # Checks for valid ticket input
            try:
                ticket_count = int(ticket_count)
            except:
                print('Invalid amount of tickets')
            else:
                if ticket_count > 0:
                    print('Now pick a movie: ')
                    for movie in movies_catalog:
                        print(movie.name + ', Price - {}$'.format(movie.cost))
                    input_movie = input().lower()
                    # Checks which movie was chosen and calculates it's price
                    if input_movie in [movie.name.lower() for movie in movies_catalog]:
                        for movie in movies_catalog:
                            if movie.name.lower() == input_movie:
                                price = movie.buy_ticket(ticket_count)
                                cinema_revenue += price
                        print('That will be {}$\r\nGoodbye.'.format(price))
                    else:
                        print('Sorry, {} is not in the catalog.'.format(input_movie))

                else:
                    print('Invalid amount of tickets')


if __name__ == '__main__':
    main()