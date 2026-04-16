from Problem0 import Problem
import math

class Hanoi(Problem):
    """ """

    def __init__(self, initial=None, goal=None, **kwds):
        """Initial state = Number of disks on the first rod"""
        tower = (tuple(x for x in range(1, initial+1)), (), ())
        if goal == None:
            goal = ((), (), tuple(x for x in range(1, initial+1)))
        self.__dict__.update(initial=tower, goal=goal, **kwds)
        

    def actions(self, state):
        ''' The actions are a tuple indicating the move: (1, 2) indicates a move from the first to the second rod.'''
        valid_moves = []
        if len(state[0]) > 0:
            if (len(state[1]) == 0) or (state[0][0] < state[1][0]):
                valid_moves.append((0, 1))
            if (len(state[2]) == 0) or (state[0][0] < state[2][0]):
                valid_moves.append((0, 2))
        if len(state[1]) > 0:
            if (len(state[0]) == 0) or (state[1][0] < state[0][0]):
                valid_moves.append((1,0))
            if (len(state[2]) == 0) or (state[1][0] < state[2][0]):
                valid_moves.append((1,2))
        if len(state[2]) > 0:
            if (len(state[0]) == 0) or (state[2][0] < state[0][0]):
                valid_moves.append((2,0))
            if (len(state[1]) == 0) or (state[2][0] < state[1][0]):
                valid_moves.append((2,1))
        
        return valid_moves
    

    def result(self, state, action):
        """Go to the `action` place, if the map says that is possible."""
        a = action[0] # From
        b = action[1] # To

        new_state = [list(i) for i in state]
        old_a = new_state[a]
        old_b = new_state[b]
        new_state[a] = old_a[1:]
        new_state[b] = [old_a[0]] + old_b

        return tuple(tuple(i) for i in new_state)
        






    def action_cost(self, s, action, s1):
        """The distance (cost) to go from s to s1."""
        return 1


