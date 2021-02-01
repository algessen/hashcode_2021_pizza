from scoring import score_answer
from full import full_solution
from greedy import greedy_solution
from lib import *
from random import *


def split_solution(teams, pizzas_in):
#    pizzas = [(i, pizzas_in[i], False) for i in range(len(pizzas_in))]
#    sorted_pizzas = sorted(pizzas, key=len)
    N = [0, 0, 0, 0, 0]
    N[2], N[3], N[4] = teams
    SUB_SIZE = 10000
    length = len(pizzas_in)
    pizzas = [(i, pizzas_in[i]) for i in range(len(pizzas_in))]
    solution = list()
    while length > 0:
        small_list = list()
        pizza_dict = dict()
        for i in range(min(SUB_SIZE, length)):
            pizza = pizzas.pop(randrange(len(pizzas)))
            small_list.append(pizza[1])
            pizza_dict[i] = pizza[0]
        length -= SUB_SIZE
        temp_solution = greedy_solution((N[2], N[3], N[4]), small_list)
        for delivery in temp_solution:
            for i in range(len(delivery)):
                delivery[i] = pizza_dict[delivery[i]]
                N[len(delivery)] -= 1
            solution.append(delivery)
    return solution


if __name__ == '__main__':
    #in_name = 'b_little_bit_of_everything.in'
    #in_name = 'c_many_ingredients.in'
    in_name = 'e_many_teams.in'
    teams, pizzas = read_file(in_name)
    answer = split_solution(teams, pizzas)
    write_result(answer, score_answer(answer, pizzas), 'e_result_split')
