
from collections import deque
from .utils import neighbors, reconstruct, Result
import time

def bfs(grid, start, goal):
    t0=time.time()
    frontier=deque([start])
    parent={}
    visited=set([start])
    expanded=0
    while frontier:
        node=frontier.popleft()
        expanded+=1
        if node==goal:
            path=reconstruct(parent, goal)
            cost = sum(grid[r][c] for r,c in path)
            return Result(path,cost,expanded,time.time()-t0)
        for n in neighbors(grid, *node):
            if n not in visited:
                visited.add(n)
                parent[n]=node
                frontier.append(n)
    return Result(None,float('inf'),expanded,time.time()-t0)
