import math
import random
import copy

MAX_DEPTH = 2

init_state = [[0, 1, 2], [2, 0, 0], [1, 0, 0]]


def run_minimax(state, player):
    state_utility = -math.inf
    action = (math.inf, -math.inf)
    for i in range(0, len(state)):
        for j in range(0, len(state[i])):
            piece_owner = state[i][j]
            if piece_owner == 0:
                next_state = copy.deepcopy(state)
                next_state[i][j] = player
                min_or_max_value = minimax(next_state, 1)
                if (min_or_max_value > state_utility):
                    state_utility = min_or_max_value
                    action = (i, j)
    return action


def minimax(state, depth):
    is_adversary_turn = depth % 2
    state_utilty = (1 if is_adversary_turn else -1) * math.inf
    if (depth == MAX_DEPTH): return calc_eval_function(state)
    print("Current state for this MiniMax:")
    print(state)
    for i in range(0, len(state)):
        for j in range(0, len(state[i])):
            piece_owner = state[i][j]
            if piece_owner == 0:
                next_state = copy.deepcopy(state)
                next_state[i][j] = is_adversary_turn + 1 # 1 for me and 2 for adversary
                min_or_max_value = minimax(next_state, depth + 1)
                if (is_adversary_turn):
                    state_utilty = min(state_utilty, min_or_max_value)
                else:
                    state_utilty = max(state_utilty, min_or_max_value)
    return state_utilty


def calc_eval_function(state):
    random_val = random.randint(0, 10)
    print("State utility reached: " + str(random_val))
    print("State for the evaluation:")
    print(state)
    return random_val


print("The best action to take is: " + str(run_minimax(init_state, 1)))