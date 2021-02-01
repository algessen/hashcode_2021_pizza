from scoring import score_answer

# Returns all possible sets of teams to send pizzas to
def teams_split(teams: tuple[int, int, int], pizzas_amount: int):
    (N2, N3, N4) = teams
    print("Splitting teams", N2, N3, N4, "pizza amount", pizzas_amount)
    for n2_i in range(0, N2 + 1):
        for n3_i in range(0, N3 + 1):
            for n4_i in range(0, N4 + 1):
                amount = n2_i * 2 + n3_i * 3 + n4_i * 4
                # print("Testing split", n2_i, n3_i, n4_i, "Required pizza amount", amount)
                if amount <= pizzas_amount:
                    yield [n2_i, n3_i, n4_i, amount]


# Returns all possible sequences of given pizzas of given length
def all_sequences(amount: int, pizzas):
    if len(pizzas) < amount:
        raise ValueError("Can't build a sequence of length", amount, "out of", len(pizzas), "pizzas")
    if amount == 0:
        return []
    for i in range(0, len(pizzas)):
        first_pizza = pizzas[i]
        if amount == 1:
            yield [first_pizza]
        else:
            rest = pizzas[:i] + pizzas[i+1:]
            for rest_seq in all_sequences(amount - 1, rest):
                yield [first_pizza] + rest_seq


def all_solutions(team_split: tuple[int, int, int, int], pizzas_amount: int):
    (N2, N3, N4, amount) = team_split
    sequences = list(all_sequences(amount, list(range(0, pizzas_amount))))
    print("Got sequences", len(sequences))
    for sequence in sequences:
        solution = []
        sequence_index = 0
        for i in range(0, N2):
            solution.append(sequence[sequence_index:sequence_index + 2])
            sequence_index += 2
        for i in range(0, N3):
            solution.append(sequence[sequence_index:sequence_index + 3])
            sequence_index += 3
        for i in range(0, N4):
            solution.append(sequence[sequence_index:sequence_index + 4])
            sequence_index += 4
        yield solution
    return


def full_solution(teams: tuple[int, int, int], pizzas_in: list[list[int]]):
    (N2, N3, N4) = teams
    best_solution = []
    best_score = 0
    for team_split in teams_split(teams, len(pizzas_in)):
        [n2_i, n3_i, n4_i, amount] = team_split
        print("Team split ", n2_i, n3_i, n4_i, amount)
        solutions = list(all_solutions(team_split, len(pizzas_in)))
        print("Got solutions:", len(solutions))
        for solution in solutions:
            # print("Possible solution", solution)
            solution_score = score_answer(solution, pizzas_in)
            # print("Score", solution_score)
            if solution_score > best_score:
                best_solution = solution
                best_score = solution_score
    return best_solution


if __name__ == '__main__':
    pizzas = [[0, 1, 2], [3, 4, 5], [6, 3, 1], [4, 3, 5], [6, 5]]
    solution = full_solution((1, 2, 1), pizzas)
    print("Full solution", solution, "score", score_answer(solution, pizzas))

