
# Autonomous Delivery Agent - Short Report

**Course:** CSA2001 - Fundamentals of AI and ML  
**Project:** Delivery agent on 2D grid  
**Authors:** _Your name here_

## 1. Environment model (brief)
- Grid-based, 4-connected movement.
- Cells contain integer movement cost >= 1. `#` denotes impassable obstacles.
- Dynamic obstacles represented by time-step schedule (JSON).

## 2. Agent design
- Planners implemented:
  - BFS (uninformed)
  - Uniform-Cost Search (optimal for variable costs)
  - A* with Manhattan heuristic (admissible)
  - Local search (simulated annealing) for unpredictable dynamics.
- Replanning: simulator detects when next cell becomes blocked and triggers replanning.

## 3. Heuristics
- Manhattan distance used for A* (admissible for 4-connected grids with unit step cost baseline).

## 4. Experimental results
- Use `src/runner.py` to reproduce runs; results saved to `results/summary.csv`.
- Include tables and short plots of path cost, expanded nodes, and time.

## 5. Analysis & Conclusion
- Discuss trade-offs: BFS good for uniform-cost small grids; UCS guarantees lowest-cost path but expensive;
  A* reduces expansions with a good heuristic; local search is useful for on-line replanning with unpredictability.

## 6. How to run
See `README.md`.
