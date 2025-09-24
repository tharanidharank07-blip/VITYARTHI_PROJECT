
import os, csv
from .utils import load_map
from .bfs import bfs
from .ucs import ucs
from .astar import astar
from .local_search import simulated_annealing

planners = {
    'bfs': bfs,
    'ucs': ucs,
    'astar': astar,
    'local': simulated_annealing
}

maps = [
    ('maps/small.map', (0,0), (9,9)),
    ('maps/medium.map', (0,0), (29,29)),
    ('maps/large.map', (0,0), (59,59)),
]

os.makedirs('results', exist_ok=True)
with open('results/summary.csv','w',newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(['map','planner','path_cost','expanded','time','found'])
    for m,start,goal in maps:
        grid = load_map(m)
        for name,planner in planners.items():
            if name=='local':
                res = planner(grid,start,goal,time_limit=1.0)
            else:
                res = planner(grid,start,goal)
            writer.writerow([m,name,res.cost,res.expanded,res.time, bool(res.path)])
print('Wrote results/summary.csv')
