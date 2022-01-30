from collections import defaultdict


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    # validate
    for char in skus:
        if char not in 'ABCD':
            return -1

    # get basket
    basket = defaultdict(int)
    for sku in skus:
        basket[sku] += 1
    print(basket)

    # calc sum
    basket_sum = 0
    for key, val in basket.items():
        if key == 'A':
            a_triples, a_remainder = divmod(val, 3)
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

    return basket_sum






