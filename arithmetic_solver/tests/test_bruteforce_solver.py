#!/usr/bin/python3
# =============================================================================
#
#   Arithmetic Solver
#
#   Copyright (c) Clement HUBER
#
#   MIT License
#
# =============================================================================

# IMPORTS =====================================================================

import operator
import numpy as np
from arithmetic_solver.data.solution import Solution

from ..data.parameters import TARGET_MAX, TARGET_MIN
from ..solvers.bruteforce_solver import BruteforceSolver

# TESTS =======================================================================


def test_solve():

    # Case: there are many solutions
    solver = BruteforceSolver()
    target_result = (TARGET_MIN + TARGET_MAX) / 2
    numbers = np.array([25, 6, 2, 50, 100, 9])

    try:
        solver.solve(target_result, numbers)
    except Exception as exc:
        assert False, f"'BruteforceSolver::solve()' raised an exception {exc}"

    assert len(solver._solutions) == 692

    # Case: there is only one solution
    solver = BruteforceSolver()
    target_result = 751
    numbers = np.array([25, 50, 3, 7, 7, 4])

    try:
        solver.solve(target_result, numbers)
    except Exception as exc:
        assert False, f"'BruteforceSolver::solve()' raised an exception {exc}"

    assert len(solver._solutions) == 1

    # Case: there is no exact solution
    solver = BruteforceSolver()
    target_result = 273
    numbers = np.array([2, 2, 1, 1, 9, 5])

    try:
        solver.solve(target_result, numbers)
    except Exception as exc:
        assert False, f"'BruteforceSolver::solve()' raised an exception {exc}"

    assert len(solver._solutions) == 0

    closest_solution = Solution(
        np.array([1, 2, 5, 9, 1, 2]),
        np.array([operator.add,
                  operator.mul,
                  operator.mul,
                  operator.add,
                  operator.mul]),
        272,
        273)

    assert solver._closest_solution == closest_solution
