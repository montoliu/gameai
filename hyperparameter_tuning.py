from games.asmacag import AsmacagGameParameters, AsmacagForwardModel, AsmacagGame
from heuristics import SimpleHeuristic
from utils import GameEvaluatorOE, Ntbea
import random


if __name__ == '__main__':
    # random.seed(6)
    # ASMACAG parameters
    parameters = AsmacagGameParameters()
    forward_model = AsmacagForwardModel()
    game = AsmacagGame(parameters, forward_model)

    asmacag_evaluator = GameEvaluatorOE(game, SimpleHeuristic())

    c_value = 0.5
    n_neighbours = 10
    mutation_rate = 0.5
    n_initializations = 10
    param_population_size = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
    param_mutation_rate = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    param_survival_rate = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    params = [param_population_size, param_mutation_rate, param_survival_rate]
    n_games = 4
    budget = 1
    rounds = 100

    ntbea = Ntbea(params, asmacag_evaluator, c_value, n_neighbours, mutation_rate, n_initializations)
    best_params = ntbea.run(n_games, budget, rounds)

    print("Best parameters: " + str(best_params))
    print("Population size: " + str(param_population_size[best_params[0]]))
    print("Mutation rate: " + str(param_mutation_rate[best_params[1]]))
    print("Survival rate: " + str(param_survival_rate[best_params[2]]))
