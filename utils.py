
import heapq, time, json
from collections import deque, namedtuple

Result = namedtuple('Result', ['path','cost','expanded','time'])

def load_map(path):
    grid=[]
    with open(path) as f:
        for line in f:
            line=line.strip()
            if not line: continue
            row=[]
            for tok in line.split():
                if tok == '#':
                    row.append(None)  # None == obstacle
                else:
                    row.append(int(tok))
            grid.append(row)
    return grid

def in_bounds(grid, r, c):
    return 0<=r<len(grid) and 0<=c<len(grid[0])

def neighbors(grid, r, c):
    for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
        nr, nc = r+dr, c+dc
        if in_bounds(grid,nr,nc) and grid[nr][nc] is not None:
            yield nr,nc

def reconstruct(parent, goal):
    path=[]
    cur=goal
    while cur in parent:
        path.append(cur)
        cur=parent[cur]
    path.append(cur)
    path.reverse()
    return path

def manhattan(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])
