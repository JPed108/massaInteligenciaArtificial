from search import SimpleProblemSolvingAgentProgram, EightPuzzle, astar_search

class EightPuzzleProblemSolvingProgram(SimpleProblemSolvingAgentProgram):
    def update_state(self, state, percept):
        # percept é o estado atual vindo do ambiente
        return percept

    def formulate_goal(self, state):
        return (1,2,3,4,5,6,7,8,0)

    def formulate_problem(self, state, goal):
        return EightPuzzle(state, goal)

    def search(self, problem):
        # A* usa problem.h se você não passar h explicitamente. :contentReference[oaicite:3]{index=3}
        node = astar_search(problem)
        if node is None:
            return []
        return node.solution()  # lista ['LEFT','UP',...] :contentReference[oaicite:4]{index=4}
