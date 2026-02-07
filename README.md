# CMPE 300 – Project 1  
## Hamiltonian* Path Analysis on Tricky Random Graphs

This repository contains my solution to **Project 1** of **CMPE 300 – Analysis of Algorithms** at **Boğaziçi University**.  
The project focuses on the **theoretical and experimental analysis** of algorithms for detecting a *Hamiltonian\** path in specially constructed random graphs.

---

## Problem Overview

We study a variant of the Hamiltonian Path problem, called the **Hamiltonian\*** Path:

> Given an undirected graph with **3n vertices**, determine whether there exists a simple path  
> - starting at `start`,  
> - ending at `end`,  
> - visiting **exactly `n` distinct vertices**.

### Graph Structure
The input graph is generated as follows:
- The graph consists of **three disjoint connected components**, each of size `n`
- No edges exist between different components
- Each component contains:
  - A guaranteed spanning path (to ensure connectivity)
  - Additional random edges (Bernoulli with probability 1/2)
- A random permutation is applied to hide the component structure

A Hamiltonian* path can exist **if and only if** `start` and `end` lie in the **same component**.

---

## Implemented Algorithms

The repository includes **three algorithms**, each analyzed both theoretically and experimentally.

### Naive Algorithm
- Enumerates **all subsets of size `n`** containing `{start, end}`
- Tries **all permutations** of each subset
- Checks adjacency sequentially with early termination

**Complexity**
- Best case: Θ(n)
- Worst case: Θ((3n−2)! / (2n)! · n)
- Average case: Θ((3n−2)! / (2n)!)

This approach exhibits super-exponential growth and becomes infeasible beyond `n ≈ 8`.

---

### Optimized Algorithm (Component-Aware)
- Finds the connected component of `start` using DFS
- Immediately rejects if `end` is not in the same component
- Runs permutation search only on the relevant component

**Complexity**
- Best case: O(1)
- Worst case: Θ((n−1)!)
- Average case: Θ(2ⁿ)

This optimization reduces factorial growth to exponential growth and provides dramatic speedups in practice.

---

### Bonus Algorithm (Subset Dynamic Programming)
- Uses subset-based dynamic programming
- State representation: `(visited_set, last_vertex)`
- Builds paths incrementally without enumerating permutations

**Complexity**
- Time: Θ(n² · 2ⁿ)
- Space: Θ(n · 2ⁿ)

This approach is asymptotically superior to permutation-based methods.

---

## Experimental Results

All algorithms were implemented in **Python**, tested on randomly generated graphs, and evaluated by averaging multiple runs per input size.

Key observations:
- The naive algorithm exhibits factorial growth
- The optimized algorithm remains practical for significantly larger values of `n`
- Experimental results closely match theoretical predictions

Detailed plots and analysis are provided in the report.

---

## Repository Structure

```
.
├── src/
│ └── solution.py # Algorithm implementations
├── docs/
│ └── Report.pdf # Theoretical and experimental analysis
└── README.md # Project documentation
```

---

## How to Run

```bash
python3 solution.py
```

The following functions are provided:

```python
hamiltonian_naive(graph, start, end)
hamiltonian_optimized(graph, start, end)
hamiltonian_bonus(graph, start, end)
```

Each function returns `True` or `False`.

---

## Course Information

- Course: CMPE 300 – Analysis of Algorithms  
- Institution: Boğaziçi University  
- Term: Fall 2025

---

## Notes

This project was completed for academic purposes and is intended for educational and portfolio use.
