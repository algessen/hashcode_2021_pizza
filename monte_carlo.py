from random import randrange
from scoring import score_answer

def monte1_iteration(teams, pizzas_in):
    (N2, N3, N4) = teams
    pizzas = [i for i in range(len(pizzas_in))]

    answer = []
    while(((N2 > 0) and (len(pizzas) >= 2)) or
          ((N3 > 0) and (len(pizzas) >= 3)) or
          ((N4 > 0) and (len(pizzas) >= 4))):
        total = 2*N2 + 3*N3 + 4*N4
        r = randrange(total)
        if (r < 4*N4 and len(pizzas) >= 4):
            team_size = 4
            N4 -= 1
        elif (r < 4*N4 + 3*N3 and len(pizzas) >= 3):
            team_size = 3
            N3 -= 1
        else:
            team_size = 2
            N2 -= 1
 #       print("Creating a pizza for team of %d" % team_size)
        delivery = []
        for i in range(team_size):
            pizza = randrange(len(pizzas))
            delivery.append(pizzas[pizza])
            del pizzas[pizza]
  #      print("Generated delivery", delivery)
  #      print("Remaining pizzas", pizzas, ", remaining teams %d %d %d" % (N2, N3, N4))
        answer.append(delivery)
    score = score_answer(answer, pizzas_in)
  #  print(score, answer)
    return score, answer

def monte1_solution(teams, pizzas_in):
    ITER = 1000
    score_max = 0
    asnwer_max = [[]]
    for i in range(ITER):
        score, answer = monte1_iteration(teams, pizzas_in)
        if (score > score_max):
            score_max = score
            answer_max = answer
        print("Iteration %d" % i, end='\r')
    return answer_max

if __name__ == '__main__':
    monte1_solution((1, 2, 1), [[0, 1, 2], [3, 4, 5], [6, 3, 1], [4, 3, 5], [6, 5]])