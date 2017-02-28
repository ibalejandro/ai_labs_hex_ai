import math
import copy
import label
import time

INCR_VALUE = 96
INCR_VALUE_2 = 110
INCR_VALUE_3 = 114

init_state = \
[[2, 1, 2, 1, 1, 2, 2, 1, 2, 1, 0],
[1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 0],
[1, 1, 2, 1, 1, 2, 1, 2, 1, 2, 0],
[1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 0],
[1, 1, 2, 1, 1, 2, 1, 2, 1, 2, 0],
[1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 0],
[1, 1, 2, 1, 1, 2, 1, 2, 1, 2, 0],
[1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1],
[1, 1, 2, 1, 1, 2, 1, 2, 1, 2, 2],
[1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2],
[1, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1]]

max_depth = 2
is_max_depth_odd = 0
current_player = -1
count_turn = 114

def update_max_depth():
    global max_depth, is_max_depth_odd
    max_depth += 3
    is_max_depth_odd = max_depth % 2

def run_minimax(state, player):
    global count_turn, current_player
    if count_turn == INCR_VALUE_3:
        update_max_depth()
    current_player = player
    state_utility = -math.inf
    action = (math.inf, -math.inf)
    for i in range(0, len(state)):
        for j in range(0, len(state[i])):
            piece_owner = state[i][j]
            if piece_owner == 0:
                next_state = copy.deepcopy(state)
                next_state[i][j] = player
                min_or_max_value = minimax(i, j, next_state, 1)
                if min_or_max_value > state_utility:
                    state_utility = min_or_max_value
                    action = (i, j)
    count_turn += 2
    return action


def minimax(row, column, state, depth):
    is_adversary_turn = depth % 2
    state_utilty = (1 if is_adversary_turn else -1) * math.inf
    if depth == max_depth: return calc_eval_function(row, column, state)
    #print("Current state for this MiniMax:")
    #print(state)
    for i in range(0, len(state)):
        for j in range(0, len(state[i])):
            piece_owner = state[i][j]
            if piece_owner == 0:
                next_state = copy.deepcopy(state)
                next_state[i][j] = is_adversary_turn + 1 # 1 for me and 2 for adversary
                min_or_max_value = minimax(i, j, next_state, depth + 1)
                if is_adversary_turn:
                    state_utilty = min(state_utilty, min_or_max_value)
                else:
                    state_utilty = max(state_utilty, min_or_max_value)
    return state_utilty


def calc_eval_function(i, j, state):
    eval_function_result = calc_border_distance(i, j, state) + get_appropriate_adj_blank_fields(i, j, state)
    #print("State utility reached: " + str(eval_function_result))
    #print("State for the evaluation:")
    #print(state)
    return eval_function_result


def calc_border_distance(i, j, state):
    if current_player == label.P1:
        if is_max_depth_odd:
            max_or_min_distance = min(j, label.BOARD_SIZE - j - 1)
        else:
            max_or_min_distance = max(j, label.BOARD_SIZE - j - 1)
    else:
        if is_max_depth_odd:
            max_or_min_distance = min(i, label.BOARD_SIZE - i - 1)
        else:
            max_or_min_distance = max(i, label.BOARD_SIZE - i - 1)

    return max_or_min_distance

def count_adjacent_blank_fields(i, j, state):
    adjacent_blank_fields = 0
    if (0 <= j+1 < label.BOARD_SIZE and state[i][j+1] == 0):
        adjacent_blank_fields += 1
    if (0 <= i+1 < label.BOARD_SIZE and state[i+1][ j] == 0):
        adjacent_blank_fields += 1
    if (0 <= i+1 < label.BOARD_SIZE and 0 <= j-1 < label.BOARD_SIZE and state[i+1][j-1] == 0):
        adjacent_blank_fields += 1
    if (0 <= j-1 < label.BOARD_SIZE and state[i][j-1] == 0):
        adjacent_blank_fields += 1
    if (0 <= i-1 < label.BOARD_SIZE and state[i-1][ j] == 0):
        adjacent_blank_fields += 1
    if (0 <= i-1 < label.BOARD_SIZE and 0 <= j+1 < label.BOARD_SIZE and state[i-1][j+1] == 0):
        adjacent_blank_fields += 1

    return adjacent_blank_fields

def get_appropriate_adj_blank_fields(i, j, state):
    adjacent_blank_fields = count_adjacent_blank_fields(i, j, state)
    if not is_max_depth_odd:
        adjacent_blank_fields = 6 - adjacent_blank_fields
    return adjacent_blank_fields


start = time.time()
print("The best action to take is: " + str(run_minimax(init_state, 1)))
print(time.time() - start)