
# Output:
# teams (N2, N3, N4) - number of teams with 2/3/4 persons
# pizzas [[I11, ..I1i], ... [In1, ... Ini]] - numerical ingredient list
def read_file(name) -> tuple[tuple[int, int, int], list[list[int]]]:
    ingr_dict = {}
    print("Reading file", name)
    with open(name) as f:
        P, N2, N3, N4 = [int(x) for x in next(f).split()]
        pizzas: list[list[int]] = []
        for i in range(P):
            pizza: list[int] = []
            data = next(f).split()
            ingr = data[1:]
            for i in ingr:
                if (i in ingr_dict.keys()):
                    pizza.append(ingr_dict[i])
                else:
                    pizza.append(len(ingr_dict))
                    ingr_dict[i] = len(ingr_dict)
            pizzas.append(pizza)
    #    print(ingr_dict)
    print("Teams: N2: ", N2, " N3: ", N3, " N4: ", N4)
    print("Pizzas:", len(pizzas))
    print("Unique ingredients:", unique_ingredients(pizzas))
    return (N2, N3, N4), pizzas


# Converts pizza to a bitset representation
def pizza_to_bitset(pizza: list[int]):
    result = 0
    for ingredient in pizza:
        result = result | (1 << ingredient)
    return result


# Converts a bitset representation to usual pizza
def bitset_to_pizza(bitset: int):
    power = 0
    result = []
    while pow(2, power) <= bitset:
        if bitset & pow(2, power) != 0:
            result.append(power)
        power += 1
    return result


# Counts the total amount of bits set to 1 in a bitset
def bitset_count(bitset: int):
    power = 0
    result = 0
    while pow(2, power) <= bitset:
        if bitset & pow(2, power) != 0:
            result += 1
    return result


def write_result(answer: list[list[int]], score, out_file):
    #    print("Answer: %s" % answer)
    print(out_file, " solution score: %d" % score)
    with open(out_file, "w+") as f:
        f.write(str(len(answer)) + '\n')
        for delivery in answer:
            desc = str(delivery).replace('[', '').replace(']', '').replace(',', '')
            desc = str(len(delivery)) + ' ' + desc + '\n'
            f.write(desc)


def unique_ingredients(pizzas: list[list[int]]):
    ingredients: set[int] = set()
    for pizza in pizzas:
        ingredients.update(pizza)
    return len(ingredients)


if __name__ == '__main__':
    read_file('a_example')
    read_file('b_little_bit_of_everything.in')
    read_file('c_many_ingredients.in')
    read_file('d_many_pizzas.in')
    read_file('e_many_teams.in')