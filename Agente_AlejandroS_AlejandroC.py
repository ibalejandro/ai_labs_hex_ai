import sys
import label

def main():
    print("-main-")
    state = [[0, 1, 2], [2, 0, 0], [1, 0, 0]]
    player = label.P1
    action = agent(state, player)
    print("Put a piece in the position: ")
    print(action)
#   print(str(sys.argv))


def agent(state, player):
    print("-agent-")
    print("State: ")
    print(state)
    print("Player: ")
    print(player)
    print("State in [1, 0]: ")
    print(state[1][0])

    player_1_pieces = []
    player_2_pieces = []
    empty_fields = []
    for i in range(0, len(state)):
        for j in range(0, len(state[i])):
            position = [i, j]
            piece_owner = state[i][j]
            if piece_owner == 1:
                player_1_pieces.append(position)
            elif piece_owner == 2:
                player_2_pieces.append(position)
            else:
                empty_fields.append(position)

    print("Player 1 pieces are located in: ")
    print(player_1_pieces)
    print("Player 2 pieces are located in: ")
    print(player_2_pieces)
    print("Empty fields are located in: ")
    print(empty_fields)

    return [0, 0]


if __name__ == '__main__':
    main()
