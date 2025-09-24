
#!/bin/bash
python3 src/cli.py --map maps/small.map --planner astar --start 0 0 --goal 9 9
python3 src/simulate_dynamic.py --map maps/dynamic.map --schedule maps/dynamic_schedule.json --planner ucs
python3 src/runner.py
