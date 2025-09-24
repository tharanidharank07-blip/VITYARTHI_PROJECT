
import heapq, time
from .utils import neighbors, reconstruct, Result, manhattan

def astar(grid, start, goal):
    t0=time.time()
    start_cost = grid[start[0]][start[1]]
    pq=[]
    heapq.heappush(pq,(start_cost+manhattan(start,goal), start_cost, start))
    gscore={start:start_cost}
    parent={}
    expanded=0
    while pq:
        f, cost, node = heapq.heappop(pq)
        expanded+=1
        if node==goal:
            path=reconstruct(parent, goal)
            return Result(path,cost,expanded,time.time()-t0)
        # lazy check
        if cost!=gscore.get(node, None): continue
        for n in neighbors(grid, *node):
            ncost = cost + grid[n[0]][n[1]]
            if n not in gscore or ncost < gscore[n]:
                gscore[n]=ncost
                parent[n]=node
                heapq.heappush(pq,(ncost + manhattan(n,goal), ncost, n))
    return Result(None,float('inf'),expanded,time.time()-t0)
