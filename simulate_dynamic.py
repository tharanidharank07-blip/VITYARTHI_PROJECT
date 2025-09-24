
import json, time, argparse
from .utils import load_map, in_bounds
from .ucs import ucs
from .astar import astar
from .bfs import bfs

planners = {'bfs':bfs,'ucs':ucs,'astar':astar}

def load_schedule(path):
    with open(path) as f:
        return json.load(f)

def simulate(map_path, schedule_path, planner_name):
    grid = load_map(map_path)
    schedule = load_schedule(schedule_path)
    start = (0,0)
    goal = (len(grid)-1, len(grid[0])-1)
    planner = planners[planner_name]

    # initial plan (assume dynamic obstacles predictable for short horizon)
    res = planner(grid,start,goal)
    if not res.path:
        print('No initial path found')
        return
    path = res.path
    print('Initial plan length', len(path))

    t=0
    pos = start
    step_i=1
    while pos!=goal and step_i < len(path):
        # apply schedule: obstacles appearing at time t occupy cells
        # we will block cells in grid copy if scheduled at time t
        for ob in schedule.get(str(t), []):
            r,c = ob
            if in_bounds(grid,r,c):
                grid[r][c] = None
        next_cell = path[step_i]
        # if next cell now blocked, replan
        if grid[next_cell[0]][next_cell[1]] is None:
            print(f'Time {t}: next cell {next_cell} blocked -> replanning')
            res = planner(grid,pos,goal)
            if not res.path:
                print('Replan failed, no path')
                return
            path = res.path
            step_i = 1
        else:
            pos = next_cell
            step_i += 1
        t += 1
        time.sleep(0.01)
    if pos==goal:
        print('Reached goal')
    else:
        print('Failed to reach goal')

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--map', required=True)
    parser.add_argument('--schedule', required=True)
    parser.add_argument('--planner', choices=planners.keys(), default='ucs')
    args=parser.parse_args()
    simulate(args.map, args.schedule, args.planner)
