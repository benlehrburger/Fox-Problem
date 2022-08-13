# wrap a Fox Problem object
class FoxProblem:
    def __init__(self, start_state=(3, 3, 1)):

        # save start state
        self.start_state = start_state
        # save goal state
        self.goal_state = (0, 0, 0)
        # save starting state of chickens
        self.chickens = start_state[0]
        # save starting state of foxes
        self.foxes = start_state[1]

    # test if states are safe before adding to successor list
    def safe_state(self, state):

        # if there are more foxes than chickens
        if state[0] < state[1] and state[0] is not 0:
            return False

        # if there are less than the minimum value of chickens, foxes, or boats
        if state[0] < 0 or state[1] < 0 or state[2] < 0:
            return False

        # if there are more foxes than chickens on the other side of the river
        if self.chickens - state[0] < self.foxes - state[1] and self.chickens - state[0] is not 0:
            return False

        # if there are more chickens, foxes, or boats than the start state
        if state[0] > self.chickens or state[1] > self.foxes or state[2] > self.start_state[2]:
            return False

        # otherwise we are in a safe state
        else:
            return True

    # test if the current state is our goal state
    def goal_test(self, state):

        if self.goal_state == state:
            return True

        else:
            return False

    # get successor states for the given state
    def get_successors(self, state):

        # save a state for each possible action
        state0 = (state[0], state[1] - 1, state[2] - 1)
        state1 = (state[0], state[1] - 2, state[2] - 1)
        state2 = (state[0] - 1, state[1] - 1, state[2] - 1)
        state3 = (state[0] - 1, state[1], state[2] - 1)
        state4 = (state[0] - 2, state[1], state[2] - 1)
        state5 = (state[0], state[1] + 1, state[2] + 1)
        state6 = (state[0], state[1] + 2, state[2] + 1)
        state7 = (state[0] + 1, state[1] + 1, state[2] + 1)
        state8 = (state[0] + 1, state[1], state[2] + 1)
        state9 = (state[0] + 2, state[1], state[2] + 1)

        states = [state9, state8, state7, state6, state5, state4, state3, state2, state1, state0]
        successors = []

        # iterate through each state and add it as a successor if it is safe
        for s in states:
            if self.safe_state(s):
                successors.append(s)

        return successors

    def __str__(self):
        string = "Chickens and foxes problem: " + str(self.start_state)
        return string


# test code
if __name__ == "__main__":
    test_cp = FoxProblem((5, 5, 1))
    print(test_cp.get_successors((5, 5, 1)))
    print(test_cp)
