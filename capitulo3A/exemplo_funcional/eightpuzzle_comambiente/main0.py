from agents import Agent, TraceAgent
from eight_puzzle_env import EightPuzzleEnvironment
from eight_puzzle_program import EightPuzzleProblemSolvingProgram

initial = (1, 2, 3,
           4, 5, 6,
           0, 7, 8)

env = EightPuzzleEnvironment(initial)
program = EightPuzzleProblemSolvingProgram()

agent = Agent(program)
agent = TraceAgent(agent)  # imprime percepto e ação (debug) :contentReference[oaicite:6]{index=6}

env.add_thing(agent)

# roda passo a passo para ver o tabuleiro evoluir
env.render()
while not env.is_done():
    env.step()
    env.render()

print("Performance:", agent.performance)
print("Final:", env.state)
