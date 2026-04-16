from Algortimos0 import *

from Hanoi0 import Hanoi

'''
state  --->  goal


'''

disks = 5
r1 = Hanoi(disks)
print('*' * 30)
print("Lista definitiva de Estados e ações utilizando breadth_first_bfs():")
print( r1 )
solution_node = breadth_first_bfs(r1)
print( path_states( solution_node ))
print('\n')
path = path_actions(solution_node)
print( path)
print(f"\nOptimal algorithm: {2**disks-1}\nBFS: {len(path)}")

