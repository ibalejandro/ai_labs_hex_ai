from Agente_AlejandroS_AlejandroC import AgenteAlejandroSAlejandroC
import time

init_state = \
[[0, 1, 1, 1, 0],
[0, 1, 0, 0, 0],
[1, 2, 2, 2, 2],
[2, 0, 0, 0, 0],
[0, 0, 0, 0, 0]]

action = AgenteAlejandroSAlejandroC()
start = time.time()
print(action.get_action_to_take(init_state, 1))
print(time.time() - start)