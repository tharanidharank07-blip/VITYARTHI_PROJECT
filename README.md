
# Autonomous Delivery Agent - Project Package

This package contains a working Python implementation of path planners for a 2D grid environment,
with BFS, Uniform-Cost Search (UCS), A* (Manhattan heuristic), and a simple local search (simulated annealing)
based replanning strategy for dynamic obstacles.

## Structure
- `src/` : Python source code (planner implementations, simulator, utilities)
- `maps/`: Grid map files (small, medium, large, dynamic)
- `report/`: Report template (`report.md`)
- `demo/`: Example screenshots placeholder
- `results/`: Example experimental outputs (CSV)
- `run_examples.sh`: Example run commands

## Requirements
- Python 3.8+
- No external dependencies (only Python standard library)

## Quick start (examples)
Run the example runner which executes planners on all maps and produces CSV results:
```
python src/runner.py
```

To run a single planner:
```
python src/cli.py --map maps/small.map --planner astar --start 0 0 --goal 9 9
```

For dynamic replanning demo:
```
python src/simulate_dynamic.py --map maps/dynamic.map --planner ucs
```

## Notes
- Map format: text file with rows of integers separated by spaces. `0` = free cell cost 1, `#` = obstacle (impassable).
  Any integer >=1 denotes movement cost for that cell.
- Dynamic map includes a JSON schedule file `maps/dynamic_schedule.json` describing moving obstacles by time steps.
