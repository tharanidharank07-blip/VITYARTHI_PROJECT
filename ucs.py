
import heapq, time
from .utils import neighbors, reconstruct, Result

def ucs(grid, start, goal):
    t0=time.time()
    pq=[]
    heapq.heappush(pq,(grid[start[0]][start[1]], start))
    cost_so_far={start:grid[start[0]][start[1]]}
    parent={}
    expanded=0
    while pq:
        cost,node = heapq.heappop(pq)
        expanded+=1
        if node==goal:
            path=reconstruct(parent, goal)
            return Result(path,cost,expanded,time.time()-t0)
        # lazy-check
        if cost!=cost_so_far.get(node, None): continue
        for n in neighbors(grid, *node):
            ncost = cost + grid[n[0]][n[1]]
            if n not in cost_so_far or ncost < cost_so_far[n]:
                cost_so_far[n]=ncost
                parent[n]=node
                heapq.heappush(pq,(ncost,n))
    return Result(None,float('inf'),expanded,time.time()-t0)
