from search import SimpleProblemSolvingAgentProgram, EightPuzzle, astar_search

class EightPuzzleProblemSolvingProgram(SimpleProblemSolvingAgentProgram):
    """
    Agent program no estilo da Figura 3.1:
    - recebe um percept (a configuração inicial do puzzle)
    - formula objetivo e problema
    - chama um algoritmo de busca (A*)
    - armazena a sequência de ações e devolve uma por vez
    """

    def update_state(self, state, percept):
        # Para o EightPuzzle, vamos tratar o percept como o "estado inicial" (tuple de 9 ints).
        # Depois que o plano existe, não precisamos atualizar mais nada.
        return percept if state is None else state

    def formulate_goal(self, state):
        # EightPuzzle já usa goal default = (1,2,3,4,5,6,7,8,0) se você não passar outro.
        return (1, 2, 3, 4, 5, 6, 7, 8, 0)

    def formulate_problem(self, state, goal):
        return EightPuzzle(initial=state, goal=goal)

    def search(self, problem):
        # astar_search retorna um Node (ou None). :contentReference[oaicite:1]{index=1}
        # Se h=None, ele usa problem.h automaticamente. :contentReference[oaicite:2]{index=2}
        node = astar_search(problem)
        if node is None:
            return []
        return node.solution()  # lista de ações (strings 'UP', 'DOWN', ...) :contentReference[oaicite:3]{index=3}
