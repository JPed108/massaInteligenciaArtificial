from capitulo3A.exemplo_funcional.eightpuzzle_semambiente.eightpuzzle_semambiente0 import \
    EightPuzzleProblemSolvingProgram
from search import EightPuzzle

program = EightPuzzleProblemSolvingProgram()

state = (1,2,3,4,5,6,0,7,8)
problem = EightPuzzle(state)  # só para usar result/goal_test

while True:
    action = program(state)   # percept = state atual
    if action is None:
        print("Terminou (sem ação).")
        break

    print("Ação:", action)
    state = problem.result(state, action)  # mundo avança

    if problem.goal_test(state):
        print("Chegou no objetivo!")
        break