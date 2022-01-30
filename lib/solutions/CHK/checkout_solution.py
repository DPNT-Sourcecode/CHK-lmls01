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
