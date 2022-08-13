
from collections import deque
from queue import *
from SearchSolution import SearchSolution


# wrap state objects
class SearchNode:

    # state object constructor
    def __init__(self, state, parent=None):
        # save the node's state
        self.state = state
        # save the node's parent except the root
        self.parent = parent


# backtrack from the current node to the root and return a list
def backchain(node):

    # initialize new path
    path = []
    # add the current node's state to path
    path.append(node.state)
    # set an intermediate variable to point to each current node
    curr = node

    # until we reach the root
    while curr.parent is not None:
        # grab the current node's parent
        curr = curr.parent
        # insert that node at the front of our path
        path.insert(0, curr.state)

    # return the path as a list
    return path

# PA2 for BFS adapted from pseudocode provided in COSC 076 Uninformed Search Algorithms lecture

# breadth first search on a graph
def bfs_search(search_problem):

    # initialize a deque to hold leaf nodes
    frontier = deque()
    # make the root node with our problem's starting state
    start_state = SearchNode(search_problem.start_state)
    # add the root node to the frontier
    frontier.append(start_state)

    # initialize a set to check if we've visited a node or not
    explored = set()
    # add the root node to our explored set
    explored.add(start_state)

    # build a solution object for BFS
    solution = SearchSolution(search_problem, "BFS")
    # increment the number of nodes visited with the root node
    solution.nodes_visited += 1

    # while there are still nodes on the frontier
    while frontier:
        # grab the most recently added node from the frontier
        current_node = frontier.popleft()
        # get and save that node's state
        current_state = current_node.state

        # if our current state is the goal state
        if search_problem.goal_test(current_state):
            # backchain to find the solution path
            solution.path = backchain(current_node)
            # return the solution object
            return solution

        # for each successor of our current node
        for child in search_problem.get_successors(current_state):
            # if we haven't visited that node yet
            if child not in explored:
                # add the child to our explored set
                explored.add(child)
                # wrap the child in a state object
                child = SearchNode(child, current_node)
                # add the child node to the frontier
                frontier.append(child)
                # increment the number of nodes visited with the child node
                solution.nodes_visited += 1

    # return the solution object
    return solution

# PA2 for DFS adapted from pseudocode provided in AIMA (Russell and Norvig) pgs 104-106

# recursive and path-checking DFS
def recursive_dls(search_problem, node, depth_limit, solution):
    # increment the number of nodes visited with the root node
    solution.nodes_visited += 1

    # BASE CASE
    # if our current state is the goal state
    if search_problem.goal_test(node.state):
        # backchain to find the solution path
        solution.path = backchain(node)
        # return the solution object
        return solution

    # else if we reach the depth limit
    elif depth_limit == 0:
        # notify the console that we've reached the maximum depth
        return 'cutoff'

    # otherwise if we are still computing
    else:
        # flag that we have not yet reached the cutoff
        cutoff_occurred = False

        # for each successor of the current node
        for child_state in search_problem.get_successors(node.state):
            # wrap that successor in a state object
            child_node = SearchNode(child_state, node)
            # find the path from that successor back to the root
            path = backchain(child_node)
            # remove that child node from our path-check list
            path.pop()

            # if we haven't yet checked a successor
            if child_state not in path:
                # RECURSIVE CASE
                # recurse using that successor as our start state
                result = recursive_dls(search_problem, child_node, depth_limit-1, solution)

                # if we reach the depth limit
                if result == 'cutoff':
                    # flag that we've reached the maximum depth limit
                    cutoff_occurred = True

                # otherwise if the result is not void then proceed with recursion
                elif result is not None:
                    # return the recurse
                    return result

        # BASE CASE
        # if we reach the depth limit
        if cutoff_occurred:
            # notify the console that we've reached the maximum depth
            return 'cutoff'

        # otherwise if we don't find a solution
        else:
            # do not return a solution
            return None


# helper function to recurse through for DFS
def dfs_search(search_problem, search_type="DFS", depth_limit=100, node=None, solution=None):

    # if no node object given, create a new search from starting state
    if node == None:
        # wrap the root in a state object
        node = SearchNode(search_problem.start_state)
        # create a solution object for DFS
        solution = SearchSolution(search_problem, search_type)

    # save each recurse as the result of our current DFS
    result = recursive_dls(search_problem, node, depth_limit, solution)

    # if the result is not void
    if result is not None:
        # return that recurse
        return result

    # return the solution object
    return solution

# PA2 for IDS adapted from pseudocode provided in AIMA (Russell and Norvig) pgs 107-110

# iterative deepening search
def ids_search(search_problem, depth_limit=100):

    # for each depth level until we reach the depth limit
    for depth_level in range(0, depth_limit):
        # save each recurse as the result of our current DFS
        result = dfs_search(search_problem, "IDS", depth_level)

        # if we do not reach the maximum depth limit
        if result is not 'cutoff':
            # return the result of that recurse
            return result

