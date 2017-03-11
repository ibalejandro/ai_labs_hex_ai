from Agente_AlejandroS_AlejandroC import AgenteAlejandroSAlejandroC
import time

init_state = \
 [[1, 1, 2, 1, 1, 2, 2, 1, 2, 1, 0],
  [1, 2, 2, 1, 1, 1, 2, 0, 0, 0, 0],
  [1, 1, 1, 1, 1, 2, 1, 0, 0, 0, 0],
  [1, 1, 2, 0, 1, 1, 2, 0, 0, 0, 0],
  [1, 1, 2, 1, 0, 2, 1, 0, 0, 0, 0],
  [1, 1, 2, 1, 1, 1, 2, 0, 0, 0, 0],
  [1, 1, 2, 1, 1, 2, 1, 0, 0, 0, 0],
  [1, 1, 2, 1, 1, 1, 2, 0, 0, 0, 0],
  [1, 1, 2, 1, 1, 2, 1, 0, 0, 0, 0],
  [1, 1, 2, 1, 1, 1, 2, 0, 0, 0, 0],
  [1, 1, 2, 1, 1, 2, 1, 0, 0, 0, 0]]
#80

 # [[2, 1, 2, 1, 1, 2, 2, 1, 2, 1, 0],
 #              [1, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0],
 #              [1, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0],
 #              [1, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0],
 #              [1, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0],
 #              [1, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0],
 #              [1, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0],
 #              [1, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0],
 #              [1, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0],
 #              [1, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0],
 #              [1, 1, 2, 1, 1, 0, 0, 0, 0, 0, 0]]
 #70

 # [[2, 1, 2, 1, 1, 2, 2, 1, 2, 1, 0],
 #              [1, 1, 2, 1, 1, 1, 2, 1, 2, 0, 0],
 #              [1, 1, 2, 1, 1, 2, 1, 2, 1, 0, 0],
 #              [1, 1, 2, 1, 1, 1, 2, 1, 2, 0, 0],
 #              [1, 1, 2, 1, 1, 2, 1, 2, 1, 0, 0],
 #              [1, 1, 2, 1, 1, 1, 2, 1, 2, 0, 0],
 #              [1, 1, 2, 1, 1, 2, 1, 2, 1, 0, 0],
 #              [1, 1, 2, 1, 1, 1, 2, 1, 2, 0, 0],
 #              [1, 1, 2, 1, 1, 2, 1, 2, 1, 0, 0],
 #              [1, 1, 2, 1, 1, 1, 2, 1, 2, 0, 0],
 #              [1, 1, 2, 1, 1, 2, 1, 2, 1, 0, 0]]
 #100

 # [[2, 1, 2, 1, 1, 2, 2, 1, 2, 1, 0],
 #              [1, 1, 2, 1, 1, 1, 2, 1, 2, 0, 0],
 #              [1, 1, 2, 1, 1, 2, 1, 2, 1, 0, 0],
 #              [1, 1, 2, 1, 1, 1, 2, 1, 2, 0, 0],
 #              [1, 1, 2, 1, 1, 2, 1, 2, 1, 0, 0],
 #              [1, 1, 2, 1, 1, 1, 2, 1, 2, 0, 0],
 #              [1, 1, 2, 1, 1, 2, 1, 2, 1, 0, 0],
 #              [1, 1, 2, 1, 1, 1, 2, 1, 0, 0, 0],
 #              [1, 1, 2, 1, 1, 2, 1, 2, 0, 0, 0],
 #              [1, 1, 2, 1, 1, 1, 2, 1, 0, 2, 0],
 #              [1, 1, 2, 1, 1, 2, 1, 2, 0, 0, 1]]
 #98

 # [[2, 1, 2, 1, 1, 2, 2, 1, 2, 1, 0],
 #              [1, 1, 2, 1, 1, 1, 2, 1, 0, 0, 0],
 #              [1, 1, 2, 1, 1, 2, 1, 2, 0, 0, 0],
 #              [1, 1, 2, 1, 1, 1, 2, 1, 0, 0, 0],
 #              [1, 1, 2, 1, 1, 2, 1, 2, 0, 0, 0],
 #              [1, 1, 2, 1, 1, 1, 2, 1, 0, 0, 0],
 #              [1, 1, 2, 1, 1, 2, 1, 2, 0, 0, 0],
 #              [1, 1, 2, 1, 1, 1, 2, 1, 0, 0, 0],
 #              [1, 1, 2, 1, 1, 2, 1, 2, 0, 0, 0],
 #              [1, 1, 2, 1, 1, 1, 2, 1, 0, 0, 0],
 #              [1, 1, 2, 1, 1, 2, 1, 2, 0, 0, 0]]
 #90

 # [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 #     [1, 1, 2, 1, 1, 1, 2, 1, 2, 0, 0],
 #     [1, 1, 2, 1, 1, 2, 1, 2, 1, 0, 0],
 #     [1, 1, 2, 1, 1, 1, 2, 1, 0, 0, 0],
 #     [1, 1, 2, 1, 1, 2, 1, 2, 0, 0, 0],
 #     [1, 1, 2, 1, 1, 1, 2, 1, 0, 0, 0],
 #     [1, 1, 2, 1, 1, 2, 1, 2, 0, 0, 0]]
 #50

  # [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  #  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  #  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  #  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  #  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  #  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  #  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  #  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  #  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  #  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  #  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# init_state = \
#     [[1, 0, 0],
#      [0, 0, 0],
#      [0, 0, 2]]

action = AgenteAlejandroSAlejandroC()
start = time.time()
print(action.get_action_to_take_main(init_state, 1))
print(time.time() - start)
