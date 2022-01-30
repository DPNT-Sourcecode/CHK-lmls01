from collections import defaultdict

simple_prices = {
    'A': 50,
    'B': 30,
    'C': 20,
    'D': 15,
    'E': 40,
    'F': 10,
    'G': 20,
    'H': 10,
    'I': 35,
    'J': 60,
    'K': 80,
    'L': 90,
    'M': 15,
    'N': 40,
    'O': 10,
    'P': 50,
    'Q': 30,
    'R': 50,
    'S': 30,
    'T': 20,
    'U': 40,
    'V': 50,
    'W': 20,
    'X': 90,
    'Y': 10,
    'Z': 50,
}

bulk_prices = {
    'A': (3, 130),
    'B': (2, 45),
    'F': (3, 20),
    'H': (5, 45),
    'K': (2, 150),
    'P': (5, 200),
    'Q': (3, 80),
    'U': (4, 120),
    'V': (2, 90),
}

double_bulk_prices = {
    'A': (5, 200),
    'H': (10, 80),
    'V': (3, 130),
}


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
    modify_basket_for_freebies(basket)

    # calc sum
    basket_total = 0

    # also modifies the basket
    basket_total += calc_basket_deal_value(basket, basket_total, double_bulk_prices)
    basket_total += calc_basket_deal_value(basket, basket_total, bulk_prices)
    basket_total += calc_basket_simple_values(basket, simple_prices, basket_total)

    return basket_total


    # for key, val in basket.items():
    #     if key == 'A':
    #         a_fives, a_five_rem = divmod(val, 5)
    #         basket_sum += a_fives * 200
    #         a_triples, a_remainder = divmod(a_five_rem, 3)
    #         basket_sum += a_triples * 130
    #         basket_sum += a_remainder * 50
    #     if key == 'B':
    #         b_doubles, b_remainder = divmod(val, 2)
    #         basket_sum += b_doubles * 45
    #         basket_sum += b_remainder * 30
    #     if key == 'C':
    #         basket_sum += val * 20
    #     if key == 'D':
    #         basket_sum += val * 15
    #     if key == 'E':
    #         basket_sum += val * 40
    #     if key == 'F':
    #         f_triples, f_remainder = divmod(val, 3)
    #         basket_sum += f_triples * 20
    #         basket_sum += f_remainder * 10

    return basket_total


# does not modify basket
def calc_number_of_new_bs(basket):
    (number_of_free_bs, _) = divmod(basket['E'], 2)
    existing_bs = basket['B']
    new_bs = existing_bs - number_of_free_bs
    if new_bs < 0:
        return 0
    return new_bs


# amends basket
def modify_basket_for_freebies(basket):
    freebies = {
        'E': (2, 'B'),
        'N': (3, 'M'),
        'R': (3, 'Q'),
    }
    for qualifying_sku, val in freebies.items():
        number_of_qualifying_skus = val[0]
        potential_reduction_sku = val[1]
        (number_of_max_free_items, _) = divmod(basket[qualifying_sku], number_of_qualifying_skus)

        existing_skus_to_be_reduced = basket[potential_reduction_sku]
        reduced_skus = existing_skus_to_be_reduced - number_of_max_free_items
        if reduced_skus < 0:
            basket[potential_reduction_sku] = 0
        basket[potential_reduction_sku] = reduced_skus


# outputs current total and reduces the number of skus in basket after calculation
def calc_basket_deal_value(basket, basket_running_total, deal_prices):
    for price_sku, bulk_tuple in deal_prices.items():
        for basket_sku, basket_count in basket:
            if basket_sku == price_sku:
                required_number_for_deal = bulk_tuple[0]
                number_of_deals, _ = divmod(basket_count, required_number_for_deal)
                basket_running_total += number_of_deals * bulk_tuple[1]
                # modifying basket
                basket[basket_sku] -= number_of_deals * required_number_for_deal
    return basket_running_total

        # if key == 'A':
            # a_fives, a_five_rem = divmod(val, 5)
            # basket_sum += a_fives * 200
            # a_triples, a_remainder = divmod(a_five_rem, 3)
            # basket_sum += a_triples * 130
            # basket_sum += a_remainder * 50

    # double_bulk_prices = {
    #     'A': (5, 200),
    #     'H': (10, 80),
    #     'V': (3, 130)
    # }


def calc_basket_simple_values(basket, simple_prices, basket_running_total):
    for key, total in basket.items():
        basket_running_total += simple_prices[key] * total
        basket[key] = 0
    return basket_running_total

