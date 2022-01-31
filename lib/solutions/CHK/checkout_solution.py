from collections import defaultdict


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    basket = defaultdict(int)
    for sku in skus:
        basket[sku] += 1
    print(basket)

    

    return 10


checkout("AAABBCD")



