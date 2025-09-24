
import random, math, time
from .utils import neighbors, Result

# A simple local-search (simulated annealing) that tries to find a low-cost path
# by mutating current path segments. This is provided as a baseline and is not guaranteed
# to be optimal. It's mainly for experimentation in dynamic/unpredictable scenarios.
def path_cost(grid, path):
    return sum(grid[r][c] for r,c in path)

def random_neighbor_path(grid, path):
    # randomly pick a node in path (not endpoints) and try to re-route locally
    if len(path)<=3: return path[:]
    i = random.randint(1,len(path)-2)
    node = path[i]
    # try to step to a random neighbor of previous node and reattach to suffix via greedy
    prev = path[i-1]
    options = [n for n in neighbors(grid, *prev)]
    if not options: return path[:]
    newmid = random.choice(options)
    newpath = path[:i] + [newmid]
    # greedily extend towards goal
    goal = path[-1]
    cur = newmid
    visited = set(newpath)
    while cur!=goal and len(newpath)<len(grid)*len(grid[0])*2:
        # choose neighbor that reduces manhattan distance to goal and not visited
        cand = sorted([n for n in neighbors(grid,*cur) if n not in visited],
                      key=lambda x: abs(x[0]-goal[0]) + abs(x[1]-goal[1]))
        if not cand:
            break
        cur = cand[0]
        newpath.append(cur)
        visited.add(cur)
    if newpath[-1]!=goal:
        return path[:]
    return newpath

def simulated_annealing(grid, start, goal, time_limit=1.0):
    t0=time.time()
    # initial naive path: straight-line greedy (might fail)
    cur = [start]
    cur_pos = start
    visited = set([start])
    while cur_pos != goal and time.time()-t0 < 0.2:
        cand = sorted([n for n in neighbors(grid,*cur_pos) if n not in visited],
                      key=lambda x: abs(x[0]-goal[0]) + abs(x[1]-goal[1]))
        if not cand: break
        cur_pos = cand[0]
        cur.append(cur_pos)
        visited.add(cur_pos)
    if cur[-1] != goal:
        # fallback to returning failure
        return Result(None, float('inf'), 0, time.time()-t0)
    cur_cost = path_cost(grid, cur)
    best = cur[:]
    best_cost = cur_cost
    iterations=0
    while time.time()-t0 < time_limit:
        iterations+=1
        cand = random_neighbor_path(grid, cur)
        cand_cost = path_cost(grid, cand)
        delta = cand_cost - cur_cost
        T = max(0.001, 1.0 - (time.time()-t0)/time_limit)
        if delta < 0 or random.random() < math.exp(-delta / (T*10 + 1e-9)):
            cur = cand; cur_cost = cand_cost
            if cur_cost < best_cost:
                best = cur[:]; best_cost = cur_cost
    return Result(best, best_cost, iterations, time.time()-t0)
