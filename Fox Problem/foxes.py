from FoxProblem import FoxProblem
from uninformed_search import bfs_search, dfs_search, ids_search
import time

# Create a few test problems:
problem331 = FoxProblem((3, 3, 1))
problem541 = FoxProblem((5, 4, 1))
problem551 = FoxProblem((5, 5, 1))

# Run the searches.
#  Each of the search algorithms should return a SearchSolution object,
#  even if the goal was not found. If goal not found, len() of the path
#  in the solution object should be 0.


print('Breadth-first search')

t0 = time.time()

print(bfs_search(problem331))
print(bfs_search(problem551))
print(bfs_search(problem541))

t1 = time.time()
BFS_time = t1-t0

print('Breadth-first search runtime: ' + str(BFS_time))

print('Depth-first search')

t2 = time.time()

print(dfs_search(problem331))
print(dfs_search(problem551))
print(dfs_search(problem541))

t3 = time.time()
DFS_time = t3-t2

print('Depth-first search runtime: ' + str(DFS_time))

print('Iterative deepening')

t4 = time.time()

print(ids_search(problem331))
print(ids_search(problem551))
print(ids_search(problem541))

t5 = time.time()
ID_time = t5-t4

print('Iterative deepening runtime: ' + str(ID_time))


