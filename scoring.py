# Scores a delivery for a single team
# delivery - for a single team, list integers, where integer is an index in the pizzas list
# pizzas - list of all available pizzas, list of pizzas, each pizza is a list of ingredients, each ingredient is an int
def score_delivery(delivery: list[int], pizzas: list[list[int]]):
    ingr_set = set()
    # print("Scoring delivery %s" % delivery)
    for pizza_index in delivery:
        pizza = pizzas[pizza_index]
        # print("Adding pizza %s" % pizza)
        ingr_set.update(pizza)
    # print("Final ingridients %s" % ingr_set)
    return pow(len(ingr_set), 2)


# Scores the whole answer (all deliveries for all teams)
# answer - a list of deliveries for all teams each delivery is a list of integers, where integer is an index in the
# pizzas list
# pizzas - list of all available pizzas, list of pizzas, each pizza is a list of ingredients, each ingredient is an int
def score_answer(answer: list[list[int]], pizzas: list[list[int]]):
    score = 0
    for delivery in answer:
        score += score_delivery(delivery, pizzas)
    return score
