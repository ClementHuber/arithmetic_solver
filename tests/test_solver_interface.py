#!/usr/bin/env python
###############################################################################
#
#    Arithmetic Solver
#
#    Copyright (c) Clément HUBER
#
#    MIT License
#
###############################################################################

__author__ = "Clément HUBER"
__copyright__ = "Clément HUBER"
__license__ = "MIT"

# IMPORTS =====================================================================

import operator

import numpy as np
import pytest
from arithmetic_solver.data.parameters import TARGET_MAX, TARGET_MIN
from arithmetic_solver.data.solution import Solution
from arithmetic_solver.solvers.bruteforce_solver import BruteforceSolver

# TESTS =======================================================================
#
# Test the methods implemented in the abstract class Solver Interface.
#
# Note: as this abstract class cannot be instantiated, a Bruteforce Solver is
#       instantiated instead.


def test_check_inputs():

    solver = BruteforceSolver()

    # OK
    target_result = (TARGET_MIN + TARGET_MAX) / 2
    numbers = np.array([25, 6, 2, 50, 100, 9])
    assert solver.check_inputs(target_result, numbers)

    # KO
    # Case: target result not in admissible range
    target_result = 2 * TARGET_MAX
    numbers = np.array([25, 6, 2, 50, 100, 9])
    with pytest.raises(ValueError):
        solver.check_inputs(target_result, numbers)

    # KO
    # Case: len(numbers) != N_NUMBERS
    target_result = (TARGET_MIN + TARGET_MAX) / 2
    numbers = np.array([25, 6, 2, 50, 100, 9, 75])
    with pytest.raises(ValueError):
        solver.check_inputs(target_result, numbers)

    # KO
    # Case: len(numbers) != N_NUMBERS
    target_result = (TARGET_MIN + TARGET_MAX) / 2
    numbers = np.array([25, 6, 2, 200, 100, 9])
    with pytest.raises(ValueError):
        solver.check_inputs(target_result, numbers)


def test_remove_duplicated_solutions():

    solver = BruteforceSolver()

    sol = Solution(np.array([100, 4, 10, 8]),
                   np.array([operator.sub, operator.add, operator.mul]),
                   848,
                   848)

    # Duplicate solutions
    solver._solutions.append(sol)
    solver._solutions.append(sol)

    solver.remove_duplicated_solutions()

    assert len(solver._solutions) == 1


def test_show_solutions():

    solver = BruteforceSolver()

    sol = Solution(np.array([100, 4, 10, 8]),
                   np.array([operator.sub, operator.add, operator.mul]),
                   848,
                   848)

    solver._solutions.append(sol)

    try:
        solver.show_solutions()
    except Exception as exc:
        assert False, f"'show_solutions()' raised an exception {exc}"
