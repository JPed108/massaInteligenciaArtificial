from capitulo3A.exemplo_funcional.eightpuzzle_semambiente.eightpuzzle_semambiente0 import \
    EightPuzzleProblemSolvingProgram

program = EightPuzzleProblemSolvingProgram()

percept_inicial = (1, 2, 3,
                   4, 5, 6,
                   0, 7, 8)

# Cada chamada devolve UMA ação. Quando acabar, devolve None.
while True:
    action = program(percept_inicial)
    if action is None:
        break
    print("Ação:", action)
