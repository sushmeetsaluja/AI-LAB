# AI Problems Using Python

This project contains solutions to three basic Artificial Intelligence (AI) problems using Python.

## Problems Included

1. **Water Jug Problem** — solved using Breadth-First Search (BFS).
2. **Missionaries and Cannibals Problem** — solved using BFS.
3. **Basic Sudoku Solver** — solved using Backtracking.

---

## 1. Water Jug Problem

### Brief Explanation
The goal is to measure a target amount of water using two jugs with fixed capacities. Each state is represented as `(A, B)`, where `A` and `B` are the current amounts of water in the two jugs.

The program generates possible actions:
- Fill either jug.
- Empty either jug.
- Pour water from one jug into the other.

**BFS** explores states level by level and finds a solution using the fewest operations. A `visited` set prevents revisiting the same state.

### Input
Enter the capacities of both jugs and the target amount.

Example:
```text
Enter capacity of Jug A: 4
Enter capacity of Jug B: 3
Enter target amount: 2
```

### Output
The program displays each state in the solution path and the total number of operations.

Example:
```text
Step 0: (0, 0)
Step 1: (0, 3)
Step 2: (3, 0)
Step 3: (3, 3)
Step 4: (4, 2)

Total steps: 4
Final state: (4, 2)
```

---

## 2. Missionaries and Cannibals Problem

### Brief Explanation
Three missionaries and three cannibals must cross a river using a boat that carries one or two people. Cannibals must never outnumber missionaries on either bank when missionaries are present.

Each state is represented as `(M, C, B)`, where:
- `M` = missionaries on the left bank
- `C` = cannibals on the left bank
- `B` = boat position (`0` = left, `1` = right)

The program generates possible boat movements, rejects states that break the safety rules, and uses **BFS** to find a solution with the minimum number of crossings.

### Input
The program uses the standard starting configuration of three missionaries and three cannibals. No user input is required.

### Output
The program prints each state, the boat's position, and the total number of crossings. With the usual rules, a shortest solution takes **11 crossings**.

---

## 3. Basic Sudoku Solver

### Brief Explanation
The solver completes a 9×9 Sudoku grid. Every row, column, and 3×3 subgrid must contain digits 1–9 without duplicates. Use `0` to represent an empty cell.

The program uses **Backtracking**:
1. Find an empty cell.
2. Try digits from 1 to 9.
3. Check whether a digit is valid in the row, column, and 3×3 subgrid.
4. If valid, place the digit and solve the remaining grid recursively.
5. If the choice leads to a dead end, remove the digit and try another.

### Input
Enter nine rows, each containing nine numbers separated by spaces. Use `0` for empty cells.

Example:
```text
5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9
```

### Output
The program prints the completed Sudoku grid if a solution is found; otherwise, it reports that no solution exists.

---

## Requirements

- Python 3.x
- No external libraries are required. The first two programs use Python's built-in `collections.deque`.

## How to Run

Save each solution in its own Python file, for example:

```text
water_jug.py
missionaries_cannibals.py
sudoku_solver.py
```

Run a program from your terminal:

```bash
python water_jug.py
python missionaries_cannibals.py
python sudoku_solver.py
```

On some systems, use `python3` instead of `python`.

## Algorithms at a Glance

| Problem | Algorithm | Main Idea |
|---|---|---|
| Water Jug | Breadth-First Search (BFS) | Explore water states level by level to find a shortest solution |
| Missionaries and Cannibals | Breadth-First Search (BFS) | Explore safe river-crossing states and find a shortest path |
| Sudoku Solver | Backtracking | Try valid digits and undo choices when they lead to a dead end |

## Learning Objectives

- Understand state-space representation.
- Apply BFS to search for a solution.
- Use queues and visited sets to avoid repeated states.
- Apply recursion and backtracking to constraint-based problems.
- Validate solutions against problem-specific rules.

## Notes

- The Water Jug program checks whether a solution can be found by exploring reachable states. For a target amount, the target must be non-negative and achievable with the jug capacities.
- The Missionaries and Cannibals program uses the standard configuration of three missionaries and three cannibals.
- The basic Sudoku solver assumes the initial clues are valid. It does not separately validate whether the starting grid already contains duplicate clues.
