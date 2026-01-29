# eight_puzzle_env.py (ou no seu main.py)

from agents import Environment
from search import EightPuzzle

class EightPuzzleEnvironment(Environment):
    def __init__(self, initial_state, goal_state=(1,2,3,4,5,6,7,8,0)):
        super().__init__()
        self.problem = EightPuzzle(initial_state, goal_state)
        self.state = initial_state

    def percept(self, agent):
        # percepto = estado atual do tabuleiro
        return self.state

    def execute_action(self, agent, action):
        # O Environment do AIMA chama execute_action para cada agent a cada step. :contentReference[oaicite:1]{index=1}
        if action is None:
            agent.alive = False
            return

        # valida ação (opcional, mas útil)
        if action not in self.problem.actions(self.state):
            # ação inválida: penaliza e mata/ignora
            agent.performance -= 10
            agent.alive = False
            return

        # aplica ação no "mundo"
        self.state = self.problem.result(self.state, action)

        # performance (ex.: -1 por passo)
        agent.performance -= 1

        # se chegou no objetivo, encerra
        if self.problem.goal_test(self.state):
            agent.alive = False

    def is_done(self):
        # termina quando objetivo alcançado OU não há agente vivo
        return self.problem.goal_test(self.state) or super().is_done()

    def render(self):
        # print simples 3x3
        s = self.state
        def cell(x): return " " if x == 0 else str(x)
        print(f"{cell(s[0])} {cell(s[1])} {cell(s[2])}")
        print(f"{cell(s[3])} {cell(s[4])} {cell(s[5])}")
        print(f"{cell(s[6])} {cell(s[7])} {cell(s[8])}")
        print()
