from Try import AgenteAlejandroSAlejandroCTry
import time

init_state = \
estado = [[0]*11 for i in range(11)]

action = AgenteAlejandroSAlejandroCTry()
start = time.time()
print(action.get_action_to_take(init_state, 1))
print(time.time() - start)