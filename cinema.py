class Movie:

    def __init__(self, name, index):
        self.name = name
        self.index = index
        self.cost = 2

    def buy_ticket(self, amount):
        """
        Calculates the price of all the tickets the user bought and updates the cost of the ticket accordingly.
        :param amount: Number of ticket purchased
        :return: The price of all the tickets
        """
        # The total price here reduced to a singular equation
        total_amount = amount * self.cost + 2 * sum(range(amount))
        self.cost += 2 * amount
        return total_amount


def choose_movie(movie_name_ind, catalog):
    """
    Returns the movie object instances according the movie name or index.
    :param catalog: Movie object list
    :param movie_name_ind: Movie name or index (not case sensitive)
    :return: Movie object
    """
    for movie in catalog:
        if (movie.name == movie_name_ind) | (movie.index == movie_name_ind):
            return movie
    # To the reviewer - The same can be done with filter but it's less readable and a bit messier.
    # return list(filter(lambda movie: (movie.name.lower() == movie_name_ind.lower()) | (movie.index == movie_name_ind),
    #                   catalog))[0]


def main():
    movies_catalog = [Movie('Wonder Woman 1984', '0'), Movie('James Bond No Time To Die', '1'),
                      Movie('Black Widow', '2')]
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
                        print('{}. {}, Price - {}$'.format(movie.index, movie.name, movie.cost))
                    input_movie = choose_movie(input(), movies_catalog)
                    if input_movie is not None:
                        price = input_movie.buy_ticket(ticket_count)
                        cinema_revenue += price
                        print('That will be {}$\r\nGoodbye.'.format(price))
                    else:
                        print('Sorry, that movie is not in the catalog.')
                else:
                    print('Invalid amount of tickets.')
        else:
            for movie in movies_catalog:
                print('{} ticket(s) were bought for {}.'.format(int(movie.cost / 2 - 1), movie.name))
            print('Overall cinema revenue: {}$'.format(cinema_revenue))


if __name__ == '__main__':
    main()
