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
        if (movie.name == movie_name_ind) or (str(catalog.index(movie)) == movie_name_ind):
            return movie


def pay_movie(ticket_count, catalog):
    """
    Takes user input for a movie, checks if it's in the catalog and pay for the tickets.
    :param ticket_count:
    :param catalog:
    :return: ticket's price
    """
    print('Now pick a movie: ')
    for movie in catalog:
        print('{}. {}, Price - {}$'.format(catalog.index(movie), movie.name, movie.cost))
    input_movie = choose_movie(input(), catalog)
    if input_movie is not None:
        price = input_movie.buy_ticket(ticket_count)
        print('That will be {}$\r\nGoodbye.'.format(price))
    else:
        price = 0
        print('Sorry, that movie is not in the catalog.')
    return price


def ticket_cnt_inp():
    """
    Takes user input for amount of tickets and checks if it is valid. If it ain't valid, returns 0.
    :return: ticket count (or 0 if invalid input was given)
    """
    ticket_count = input('How many tickets would you like to purchase? ')
    try:
        ticket_count = int(ticket_count)
    except:
        print('Invalid amount of tickets')
        return 0
    else:
        if ticket_count > 0:
            return ticket_count
        else:
            print('Invalid amount of tickets.')
            return 0


def sum_stats(catalog, revenue):
    """
    Show summarize statistics of the lst purchases - Amount of tickets bought for each movie and the cinema revenue
    :param catalog:
    :param revenue:
    :return: None
    """
    for movie in catalog:
        print('{} ticket(s) were bought for {}.'.format(int(movie.cost / 2 - 1), movie.name))
    print('Overall cinema revenue: {}$'.format(revenue))


def main():
    movies_catalog = [Movie('Wonder Woman 1984'), Movie('James Bond No Time To Die'), Movie('Black Widow')]
    username = ''
    cinema_revenue = 0
    while username != 'quit':
        username = input('Welcome! What\'s your name? (type "quit" to quit) - ')
        if username != 'quit':
            ticket_count = ticket_cnt_inp()
            if ticket_count != 0:
                cinema_revenue += pay_movie(ticket_count, movies_catalog)
        else:
            sum_stats(movies_catalog, cinema_revenue)


if __name__ == '__main__':
    main()
