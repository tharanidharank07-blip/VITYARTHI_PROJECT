
import argparse
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

def parse_coord(a, b):
    return (int(a), int(b))

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--map', required=True)
    parser.add_argument('--planner', choices=planners.keys(), required=True)
    parser.add_argument('--start', nargs=2, required=True)
    parser.add_argument('--goal', nargs=2, required=True)
    parser.add_argument('--time_limit', type=float, default=1.0)
    args = parser.parse_args()
    grid = load_map(args.map)
    start = parse_coord(*args.start)
    goal = parse_coord(*args.goal)
    planner = planners[args.planner]
    if args.planner=='local':
        res = planner(grid, start, goal, time_limit=args.time_limit)
    else:
        res = planner(grid, start, goal)
    print('Result:', res)
