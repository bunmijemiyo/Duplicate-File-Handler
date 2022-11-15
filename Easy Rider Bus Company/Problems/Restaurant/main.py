import itertools

dishes = itertools.product(main_courses, desserts, drinks)
prices = itertools.product(price_main_courses, price_desserts, price_drinks)
for d, p in zip(dishes, prices):
    if sum(p) <= 30:
        print(*d, sum(p))