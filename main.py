from monte_carlo import monte1_solution
from scoring import score_answer
# from full import full_solution
from greedy import greedy_solution
from lib import read_file, write_result


def dummy_solution(teams, pizzas):
    (N2, N3, N4) = teams
    n_pizzas = [[i, pizzas[i]] for i in range(len(pizzas))]
    answer = []
    while(((N2 > 0) and (len(n_pizzas) >= 2)) or
          ((N3 > 0) and (len(n_pizzas) >= 3)) or
          ((N4 > 0) and (len(n_pizzas) >= 4))):
        team_delivery = []
        if len(n_pizzas) >= 4:
            team_delivery.append(n_pizzas[0][0])
            team_delivery.append(n_pizzas[1][0])
            team_delivery.append(n_pizzas[2][0])
            team_delivery.append(n_pizzas[3][0])
            del n_pizzas[0:4]
            N4 -= 1
        elif len(n_pizzas) >= 3:
            team_delivery.append(n_pizzas[0][0])
            team_delivery.append(n_pizzas[1][0])
            team_delivery.append(n_pizzas[2][0])
            del n_pizzas[0:3]
            N3 -= 1
        else:
            team_delivery.append(n_pizzas[0][0])
            team_delivery.append(n_pizzas[1][0])
            del n_pizzas[0:2]
            N2 -= 1
        answer.append(team_delivery)
    return answer


def solution(in_file, out_file, solution_f):
    teams, pizzas = read_file(in_file)
    answer = solution_f(teams, pizzas)
    write_result(answer, score_answer(answer, pizzas), out_file)

if __name__ == '__main__':
#    solution('a_example',                     'a_result_greedy', greedy_solution)
#    solution('b_little_bit_of_everything.in', 'b_result_greedy', greedy_solution)
#    solution('c_many_ingredients.in',         'c_result_greedy', greedy_solution)
    solution('d_many_pizzas.in', 'greedy_result/d_result_greedy', greedy_solution)
#    solution('e_many_teams.in',               'e_result_greedy', greedy_solution)
