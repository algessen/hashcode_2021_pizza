from lib import read_file, write_result

def pizza_len(pizza):
    return len(pizza[1])


def find_next_set(num_people, pizzas, start):
    next_set = []
    ingredients = set()
    pizzas[start][2] = True
    next_set.append(pizzas[start][0])
    ingredients.update(pizzas[start][1])
    remaining = num_people - 1
    while remaining > 0:
        best = -1
        best_score = len(ingredients)
        for p in range(start, len(pizzas)):
            if not(pizzas[p][2]):
                test_set = ingredients.copy()
                test_set.update(pizzas[p][1])
                if len(test_set) >= best_score:
                    best = p
                    best_score = len(test_set)
        if best == -1:
            for p in next_set:
                pizzas[p][2] = False
            return False
        next_set.append(pizzas[best][0])
        pizzas[best][2] = True
        ingredients.update(pizzas[best][1])
        remaining = remaining - 1
    return next_set


def greedy_solution(teams, pizzas_in):
    (N2, N3, N4) = teams
    pizzas = [[i, pizzas_in[i], False] for i in range(len(pizzas_in))]
    sorted_pizzas = sorted(pizzas, key=pizza_len, reverse=True)
    first_available = 0
    answer = []
    for i in range(N4):
        while sorted_pizzas[first_available][2]:
            first_available = first_available + 1
            if first_available >= len(pizzas):
                return answer
        next_set = find_next_set(4, sorted_pizzas, first_available)
        if next_set:
            answer.append(next_set)
            if i % 100 == 0:
                print("N4 ", i)

    for i in range(N3):
        while sorted_pizzas[first_available][2]:
            first_available = first_available + 1
            if first_available >= len(pizzas):
                return answer
        next_set = find_next_set(3, sorted_pizzas, first_available)
        if next_set:
            answer.append(next_set)
            if i % 100 == 0:
                print("N3 ", i)

    for i in range(N2):
        while sorted_pizzas[first_available][2]:
            first_available = first_available + 1
            if first_available >= len(pizzas):
                return answer
        next_set = find_next_set(2, sorted_pizzas, first_available)
        if next_set:
            answer.append(next_set)
            if i % 100 == 0:
                print("N2 ", i)

    return answer


if __name__ == '__main__':
    teams, pizzas = read_file("b_little_bit_of_everything.in")
    ans = greedy_solution(teams, pizzas)
    print(ans)
