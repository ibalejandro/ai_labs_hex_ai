import math
import copy


class AgenteAlejandroSAlejandroCTry:

    BOARD_LENGTH_AND_WIDTH = 11
    CENTRAL_ROW_COLUMN = 5
    P1 = 1
    INCR_VALUE = 50
    DISTANCE_TO_OPTIMAL_PATH = [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]

    # Constructor.
    def __init__(self):
        self.current_player = 0  # There is no current_player at that moment.
        self.turns_count = 0
        self.max_depth = 3  # It can´t be higher at the beginning due to the time constraint of 5 seconds.

    # Returns the best action for the current state of the game.
    def get_action_to_take(self, state, current_player):
        self.current_player = current_player
        if self.turns_count == self.INCR_VALUE:
            self.max_depth += 1
        state_utility = -math.inf  # Negative infinite because the state utility wants to be maximized.

        if current_player == self.P1:
            # Iterates over every field on the board vertically.
            for j in range(0, self.BOARD_LENGTH_AND_WIDTH):
                for i in range(0, self.BOARD_LENGTH_AND_WIDTH):
#                    print("vertical",i,j)
                    piece_owner = state[i][j]
                    if piece_owner == 0:  # It is a blank field.
                        minimax_value = self.iterate_over_state(i, j, state, current_player, state_utility)
#                        print("minimax_value", minimax_value, "state utility", state_utility)
                        if minimax_value > state_utility:
                            state_utility = minimax_value
                            action = (i, j)
#                            print("minimax_value > state_utility", action)
        else:
            # Iterates over every field on the board horizontally.
            for i in range(0, self.BOARD_LENGTH_AND_WIDTH):
                for j in range(0, self.BOARD_LENGTH_AND_WIDTH):
#                    print("horizontal", i, j)
                    piece_owner = state[i][j]
                    if piece_owner == 0:  # It is a blank field.
                        minimax_value = self.iterate_over_state(i, j, state, current_player, state_utility)
                        if minimax_value > state_utility:
                            state_utility = minimax_value
                            action = (i, j)
        self.turns_count += 2  # When this algorithm executes again, the current turn will be incremented by two.
        return action

    def iterate_over_state(self, i, j, state, current_player, state_utility):
        next_state = copy.deepcopy(state)
        next_state[i][j] = current_player  # The current state of the game is modified on that position.
        # The MiniMax algorithm receives the modification, the state with that modification, a 1 indicating
        # that one movement has already been done and the alpha and beta values.
        minimax_value = self.minimax(i, j, next_state, 1, state_utility, math.inf)
        return minimax_value

    def minimax(self, row_modified, column_modified, state, depth, alpha, beta):
        is_state_level_minimizing = depth % 2  # The odd state levels minimize.
        state_utility = (1 if is_state_level_minimizing else -1) * math.inf

        # If the state's depth is at the limit, the utility is calculated using the evaluation function.
        if depth == self.max_depth:
#            print("depth", depth)
            return self.get_utility_from_eval_function(row_modified, column_modified, state)

        # Iterates over every field on the board.
        for i in range(0, self.BOARD_LENGTH_AND_WIDTH):
            for j in range(0, self.BOARD_LENGTH_AND_WIDTH):
                piece_owner = state[i][j]
                if piece_owner == 0:
                    next_state = copy.deepcopy(state)
                    # The current state of the game is modified on that position putting a 2 if the state level is
                    # minimizing (1+1) and a 1 if it is not (0+1).
                    next_state[i][j] = is_state_level_minimizing + 1
                    # The depth is incremented to execute the opposite action in the next iteration of MiniMax.
                    minimax_value = self.minimax(i, j, next_state, depth + 1, alpha, beta)
                    if is_state_level_minimizing:
                        state_utility = min(state_utility, minimax_value)
                        if state_utility <= alpha:
#                            print("alpha")
                            # The current state utility is bad enough with respect to the best already explored option
                            # along the path to the root for maximizing levels. It is already known that this state
                            # won´t be took into account in the above max level.
                            return state_utility
                        # The best already explored option along the path to the root for minimizing levels is updated
                        # for the alpha-beta pruning.
                        beta = min(beta, state_utility)
                    else:
                        state_utility = max(state_utility, minimax_value)
                        if state_utility >= beta:
#                            print("beta")
                            # The current state utility is bad enough with respect to the best already explored option
                            # along the path to the root for minimizing levels. It is already known that this state
                            # won´t be took into account in the above min level.
                            return state_utility
                        # The best already explored option along the path to the root for maximizing levels is updated
                        # for the alpha-beta pruning.
                        alpha = max(alpha, state_utility)
        # It happens when no other actions were available from the given state.
        if state_utility == math.inf or state_utility == -math.inf:
            state_utility = self.get_utility_from_eval_function(row_modified, column_modified, state)

        return state_utility

    def get_utility_from_eval_function(self, i, j, state):
        visited_states = [[False] * self.BOARD_LENGTH_AND_WIDTH for i in range(self.BOARD_LENGTH_AND_WIDTH)]
        # The states are going to be evaluated according to the difference between the max and min i (if the player for
        # the evaluation wins vertically) or to the difference between the max and min j (if the player for the
        # evaluation wins horizontally).
        piece_owner = self.get_last_movement_owner()
        if piece_owner == self.P1:
            state_utility = (3 * self.dfs_vertical(i, j, state, piece_owner, visited_states, i, i)) \
                            + (2 * self.count_virtual_connections_vertically(i, j, state, piece_owner)) \
                            + self.count_adjacent_own_fields(i, j, state, piece_owner)
                            # self.DISTANCE_TO_OPTIMAL_PATH[j]

        else:
            state_utility = (3 * self.dfs_horizontal(i, j, state, piece_owner, visited_states, j, j)) \
                            + (2 * self.count_virtual_connections_horizontally(i, j, state, piece_owner)) \
                            + self.count_adjacent_own_fields(i, j, state, piece_owner)
                            # + self.DISTANCE_TO_OPTIMAL_PATH[i]

#        print("State utility for", i, ",", j, ":", state_utility)
        return state_utility

    # Determines the owner of the last movement for the evaluation.
    def get_last_movement_owner(self):
        # The player for the evaluation is the opposite to the current one when the max depth is even.
        return (self.current_player % 2) + 1 if self.max_depth % 2 == 0 else self.current_player

    # DFS is used to find the max top index and min bottom index that can be achieved from the current position
    # going through every existing path of connected pieces that belong to the piece owner. Using those indexes, the
    # difference between them is calculated in order to find the maximum vertical delta and return it as the evaluation
    # for the given state.
    def dfs_vertical(self, i, j, state, piece_owner, visited_states, max_i_reached, min_i_reached):
        vertical_delta = max_i_reached - min_i_reached + 1
        visited_states[i][j] = True

        # Each of the six possible movements from the given position is analyzed if the next position exist, it was
        # not visited yet and the piece on that position belongs to the piece owner.
        if 0 <= j + 1 < self.BOARD_LENGTH_AND_WIDTH and state[i][j + 1] == piece_owner and not visited_states[i][j + 1]:
            branch_delta = self.dfs_vertical(i, j + 1, state, piece_owner, visited_states, max(max_i_reached, i),
                                             min(min_i_reached, i))
            vertical_delta = max(vertical_delta, branch_delta)
        if 0 <= i + 1 < self.BOARD_LENGTH_AND_WIDTH and state[i + 1][j] == piece_owner and not visited_states[i + 1][j]:
            branch_delta = self.dfs_vertical(i + 1, j, state, piece_owner, visited_states, max(max_i_reached, i + 1),
                                             min(min_i_reached, i + 1))
            vertical_delta = max(vertical_delta, branch_delta)
        if 0 <= i + 1 < self.BOARD_LENGTH_AND_WIDTH and 0 <= j - 1 < self.BOARD_LENGTH_AND_WIDTH \
                and state[i + 1][j - 1] == piece_owner and not visited_states[i + 1][j - 1]:
            branch_delta = self.dfs_vertical(i + 1, j - 1, state, piece_owner, visited_states,
                                             max(max_i_reached, i + 1), min(min_i_reached, i + 1))
            vertical_delta = max(vertical_delta, branch_delta)
        if 0 <= j - 1 < self.BOARD_LENGTH_AND_WIDTH and state[i][j - 1] == piece_owner and not visited_states[i][j - 1]:
            branch_delta = self.dfs_vertical(i, j - 1, state, piece_owner, visited_states, max(max_i_reached, i),
                                             min(min_i_reached, i))
            vertical_delta = max(vertical_delta, branch_delta)
        if 0 <= i - 1 < self.BOARD_LENGTH_AND_WIDTH and state[i - 1][j] == piece_owner and not visited_states[i - 1][j]:
            branch_delta = self.dfs_vertical(i - 1, j, state, piece_owner, visited_states, max(max_i_reached, i - 1),
                                             min(min_i_reached, i - 1))
            vertical_delta = max(vertical_delta, branch_delta)
        if 0 <= i - 1 < self.BOARD_LENGTH_AND_WIDTH and 0 <= j + 1 < self.BOARD_LENGTH_AND_WIDTH \
                and state[i - 1][j + 1] == piece_owner and not visited_states[i - 1][j + 1]:
            branch_delta = self.dfs_vertical(i - 1, j + 1, state, piece_owner, visited_states,
                                             max(max_i_reached, i - 1), min(min_i_reached, i - 1))
            vertical_delta = max(vertical_delta, branch_delta)

        return vertical_delta

    # DFS is used to find the max right index and min left index that can be achieved from the current position
    # going through every existing path of connected pieces that belong to the piece owner. Using those indexes, the
    # difference between them is calculated in order to find the maximum horizontal delta and return it as the
    # evaluation for the given state.
    def dfs_horizontal(self, i, j, state, piece_owner, visited_states, max_j_reached, min_j_reached):
        horizontal_delta = max_j_reached - min_j_reached + 1
        visited_states[i][j] = True

        # Each of the six possible movements from the given position is analyzed if the next position exist, it was
        # not visited yet and the piece on that position belongs to the piece owner.
        if 0 <= j + 1 < self.BOARD_LENGTH_AND_WIDTH and state[i][j + 1] == piece_owner and not visited_states[i][j + 1]:
            branch_delta = self.dfs_horizontal(i, j + 1, state, piece_owner, visited_states, max(max_j_reached, j + 1),
                                               min(min_j_reached, j + 1))
            horizontal_delta = max(horizontal_delta, branch_delta)
        if 0 <= i + 1 < self.BOARD_LENGTH_AND_WIDTH and state[i + 1][j] == piece_owner and not visited_states[i + 1][j]:
            branch_delta = self.dfs_horizontal(i + 1, j, state, piece_owner, visited_states, max(max_j_reached, j),
                                               min(min_j_reached, j))
            horizontal_delta = max(horizontal_delta, branch_delta)
        if 0 <= i + 1 < self.BOARD_LENGTH_AND_WIDTH and 0 <= j - 1 < self.BOARD_LENGTH_AND_WIDTH \
                and state[i + 1][j - 1] == piece_owner and not visited_states[i + 1][j - 1]:
            branch_delta = self.dfs_horizontal(i + 1, j - 1, state, piece_owner, visited_states,
                                               max(max_j_reached, j - 1), min(min_j_reached, j - 1))
            horizontal_delta = max(horizontal_delta, branch_delta)
        if 0 <= j - 1 < self.BOARD_LENGTH_AND_WIDTH and state[i][j - 1] == piece_owner and not visited_states[i][j - 1]:
            branch_delta = self.dfs_horizontal(i, j - 1, state, piece_owner, visited_states, max(max_j_reached, j - 1),
                                               min(min_j_reached, j - 1))
            horizontal_delta = max(horizontal_delta, branch_delta)
        if 0 <= i - 1 < self.BOARD_LENGTH_AND_WIDTH and state[i - 1][j] == piece_owner and not visited_states[i - 1][j]:
            branch_delta = self.dfs_horizontal(i - 1, j, state, piece_owner, visited_states, max(max_j_reached, j),
                                               min(min_j_reached, j))
            horizontal_delta = max(horizontal_delta, branch_delta)
        if 0 <= i - 1 < self.BOARD_LENGTH_AND_WIDTH and 0 <= j + 1 < self.BOARD_LENGTH_AND_WIDTH \
                and state[i - 1][j + 1] == piece_owner and not visited_states[i - 1][j + 1]:
            branch_delta = self.dfs_horizontal(i - 1, j + 1, state, piece_owner, visited_states,
                                               max(max_j_reached, j + 1), min(min_j_reached, j + 1))
            horizontal_delta = max(horizontal_delta, branch_delta)

        return horizontal_delta

    def count_adjacent_own_fields(self, i, j, state, piece_owner):
        adjacent_own_fields = 0
        if 0 <= j + 1 < self.BOARD_LENGTH_AND_WIDTH and state[i][j + 1] == piece_owner:
            adjacent_own_fields += 1
        if 0 <= i + 1 < self.BOARD_LENGTH_AND_WIDTH and state[i + 1][j] == piece_owner:
            adjacent_own_fields += 1
        if 0 <= i + 1 < self.BOARD_LENGTH_AND_WIDTH and 0 <= j - 1 < self.BOARD_LENGTH_AND_WIDTH \
                and state[i + 1][j - 1] == piece_owner:
            adjacent_own_fields += 1
        if 0 <= j - 1 < self.BOARD_LENGTH_AND_WIDTH and state[i][j - 1] == piece_owner:
            adjacent_own_fields += 1
        if 0 <= i - 1 < self.BOARD_LENGTH_AND_WIDTH and state[i - 1][j] == piece_owner:
            adjacent_own_fields += 1
        if 0 <= i - 1 < self.BOARD_LENGTH_AND_WIDTH and 0 <= j + 1 < self.BOARD_LENGTH_AND_WIDTH \
                and state[i - 1][j + 1] == piece_owner:
            adjacent_own_fields += 1

        return adjacent_own_fields

    def count_virtual_connections_vertically(self, i, j, state, piece_owner):
        virtual_connections = 0
        if 0 <= i - 2 < self.BOARD_LENGTH_AND_WIDTH and 0 <= j + 1 < self.BOARD_LENGTH_AND_WIDTH \
                and state[i - 2][j + 1] == piece_owner:
            virtual_connections += self.exist_virtual_connection(i, j, i - 2, j + 1, state)
        if 0 <= i - 1 < self.BOARD_LENGTH_AND_WIDTH and 0 <= j - 1 < self.BOARD_LENGTH_AND_WIDTH \
                and state[i - 1][j - 1] == piece_owner:
            virtual_connections += self.exist_virtual_connection(i, j, i - 1, j - 1, state)
        if 0 <= i + 2 < self.BOARD_LENGTH_AND_WIDTH and 0 <= j - 1 < self.BOARD_LENGTH_AND_WIDTH \
                and state[i + 2][j - 1] == piece_owner:
            virtual_connections += self.exist_virtual_connection(i, j, i + 2, j - 1, state)
        if 0 <= i + 1 < self.BOARD_LENGTH_AND_WIDTH and 0 <= j + 1 < self.BOARD_LENGTH_AND_WIDTH \
                and state[i + 1][j + 1] == piece_owner:
            virtual_connections += self.exist_virtual_connection(i, j, i + 1, j + 1, state)

        return virtual_connections

    def count_virtual_connections_horizontally(self, i, j, state, piece_owner):
        virtual_connections = 0
        if 0 <= i - 1 < self.BOARD_LENGTH_AND_WIDTH and 0 <= j + 2 < self.BOARD_LENGTH_AND_WIDTH \
                and state[i - 1][j + 2] == piece_owner:
            virtual_connections += self.exist_virtual_connection(i, j, i - 1, j + 2, state)
#            print("virtual_connections with ", i - 1, j + 2, "VC", virtual_connections)
        if 0 <= i - 1 < self.BOARD_LENGTH_AND_WIDTH and 0 <= j - 1 < self.BOARD_LENGTH_AND_WIDTH \
                and state[i - 1][j - 1] == piece_owner:
            virtual_connections += self.exist_virtual_connection(i, j, i - 1, j - 1, state)
#            print("virtual_connections with ", i - 1, j - 1, "VC", virtual_connections)
        if 0 <= i + 1 < self.BOARD_LENGTH_AND_WIDTH and 0 <= j - 2 < self.BOARD_LENGTH_AND_WIDTH \
                and state[i + 1][j - 2] == piece_owner:
            virtual_connections += self.exist_virtual_connection(i, j, i + 1, j - 2, state)
#            print("virtual_connections with ", i + 1, j - 2, "VC", virtual_connections)
        if 0 <= i + 1 < self.BOARD_LENGTH_AND_WIDTH and 0 <= j + 1 < self.BOARD_LENGTH_AND_WIDTH \
                and state[i + 1][j + 1] == piece_owner:
            virtual_connections += self.exist_virtual_connection(i, j, i + 1, j + 1, state)
#            print("virtual_connections with ", i + 1, j + 1, "VC", virtual_connections)
#        print("virtual connections:", virtual_connections, "pos", i, j)
        return virtual_connections

    def exist_virtual_connection(self, evaluating_i, evaluating_j, fix_i, fix_j, state):
        adjacent_blank_neighbors = len(set(self.get_blank_adjacent_fields_list(evaluating_i, evaluating_j, state))
                                       & set(self.get_blank_adjacent_fields_list(fix_i, fix_j, state)))
        return 1 if adjacent_blank_neighbors == 2 else 0

    def get_blank_adjacent_fields_list(self, i, j, state):
        blank_adjacent_fields_list = []
        if 0 <= j + 1 < self.BOARD_LENGTH_AND_WIDTH and state[i][j + 1] == 0:
            blank_adjacent_fields_list.append((i, j + 1))
        if 0 <= i + 1 < self.BOARD_LENGTH_AND_WIDTH and state[i + 1][j] == 0:
            blank_adjacent_fields_list.append((i + 1, j))
        if 0 <= i + 1 < self.BOARD_LENGTH_AND_WIDTH and 0 <= j - 1 < self.BOARD_LENGTH_AND_WIDTH \
                and state[i + 1][j - 1] == 0:
            blank_adjacent_fields_list.append((i + 1, j - 1))
        if 0 <= j - 1 < self.BOARD_LENGTH_AND_WIDTH and state[i][j - 1] == 0:
            blank_adjacent_fields_list.append((i, j - 1))
        if 0 <= i - 1 < self.BOARD_LENGTH_AND_WIDTH and state[i - 1][j] == 0:
            blank_adjacent_fields_list.append((i - 1, j))
        if 0 <= i - 1 < self.BOARD_LENGTH_AND_WIDTH and 0 <= j + 1 < self.BOARD_LENGTH_AND_WIDTH \
                and state[i - 1][j + 1] == 0:
            blank_adjacent_fields_list.append((i - 1, j + 1))
        return blank_adjacent_fields_list

## Iterative deepening.
## Constraint time.
