from collections import defaultdict


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    # validate
    for char in skus:
        if char not in 'ABCDEF':
            return -1

    # get basket
    basket = defaultdict(int)
    for sku in skus:
        basket[sku] += 1

    # modify basket with freebies
    basket['B'] = calc_number_of_new_bs(basket)

    # calc sum
    basket_sum = 0
    for key, val in basket.items():
        if key == 'A':
            a_fives, a_five_rem = divmod(val, 5)
            basket_sum += a_fives * 200
            a_triples, a_remainder = divmod(a_five_rem, 3)
            basket_sum += a_triples * 130
            basket_sum += a_remainder * 50
        if key == 'B':
            b_doubles, b_remainder = divmod(val, 2)
            basket_sum += b_doubles * 45
            basket_sum += b_remainder * 30
        if key == 'C':
            basket_sum += val * 20
        if key == 'D':
            basket_sum += val * 15
        if key == 'E':
            basket_sum += val * 40
        if key == 'F':
            f_triples, f_remainder = divmod(val, 3)
            basket_sum += f_triples * 20
            basket_sum += f_remainder * 10

    return basket_sum


# does not modify basket
def calc_number_of_new_bs(basket):
    (number_of_free_bs, _) = divmod(basket['E'], 2)
    existing_bs = basket['B']
    new_bs = existing_bs - number_of_free_bs
    if new_bs < 0:
        return 0
    return new_bs



simple_prices = {

}
# | Item | Price | Special offers         |
# +------+-------+------------------------+
# | A    | 50    | 3A for 130, 5A for 200 |
# | B    | 30    | 2B for 45              |
# | C    | 20    |                        |
# | D    | 15    |                        |
# | E    | 40    | 2E get one B free      |
# | F    | 10    | 2F get one F free      |
# | G    | 20    |                        |
# | H    | 10    | 5H for 45, 10H for 80  |
# | I    | 35    |                        |
# | J    | 60    |                        |
# | K    | 80    | 2K for 150             |
# | L    | 90    |                        |
# | M    | 15    |                        |
# | N    | 40    | 3N get one M free      |
# | O    | 10    |                        |
# | P    | 50    | 5P for 200             |
# | Q    | 30    | 3Q for 80              |
# | R    | 50    | 3R get one Q free      |
# | S    | 30    |                        |
# | T    | 20    |                        |
# | U    | 40    | 3U get one U free      |
# | V    | 50    | 2V for 90, 3V for 130  |
# | W    | 20    |                        |
# | X    | 90    |                        |
# | Y    | 10    |                        |
# | Z    | 50    |                        |
# +------+-------+------------------------+
