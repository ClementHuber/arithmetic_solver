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
from arithmetic_solver.data.solution import Solution

# TESTS =======================================================================


def test__eq__():

    # OK
    sol_1 = Solution(
        np.array([100, 4, 10, 8]),
        np.array([operator.sub, operator.add, operator.mul]),
        848,
        848)

    sol_2 = sol_1

    assert sol_1 == sol_2

    # KO
    # Case: numbers are different
    sol_1 = Solution(
        np.array([100, 4, 10, 4]),
        np.array([operator.sub, operator.add, operator.mul]),
        848,
        848)

    sol_2 = Solution(
        np.array([100, 4, 10, 8]),
        np.array([operator.sub, operator.add, operator.mul]),
        848,
        848)

    assert sol_1 != sol_2

    # KO
    # Case: operators are different
    sol_1 = Solution(
        np.array([100, 4, 10, 4]),
        np.array([operator.sub, operator.add, operator.mul]),
        848,
        848)

    sol_2 = Solution(
        np.array([100, 4, 10, 4]),
        np.array([operator.sub, operator.mul, operator.mul]),
        848,
        848)

    assert sol_1 != sol_2

    # KO
    # Case: results are different
    sol_1 = Solution(
        np.array([100, 4, 10, 4]),
        np.array([operator.sub, operator.add, operator.mul]),
        848,
        848)

    sol_2 = Solution(
        np.array([100, 4, 10, 4]),
        np.array([operator.sub, operator.add, operator.mul]),
        320,
        848)

    assert sol_1 != sol_2

    # KO
    # Case: target results are different
    sol_1 = Solution(
        np.array([100, 4, 10, 4]),
        np.array([operator.sub, operator.add, operator.mul]),
        848,
        848)

    sol_2 = Solution(
        np.array([100, 4, 10, 4]),
        np.array([operator.sub, operator.add, operator.mul]),
        848,
        320)

    assert sol_1 != sol_2


def test__hash__():

    solution = Solution(
        np.array([100, 4, 10, 8]),
        np.array([operator.sub, operator.add, operator.mul]),
        848,
        848)

    try:
        solution.__hash__()
    except Exception as exc:
        assert False, f"'__hash__()' raised an exception {exc}"


def test_le_compte_est_bon():

    # OK
    solution = Solution(
        np.array([100, 4, 10, 8]),
        np.array([operator.sub, operator.add, operator.mul]),
        848,
        848)
    assert solution.le_compte_est_bon()

    # KO
    # Case: result != target_result
    solution = Solution(
        np.array([100, 4, 10, 8]),
        np.array([operator.sub, operator.add, operator.mul]),
        848,
        900)
    assert not solution.le_compte_est_bon()


def test_show():

    solution = Solution(
        np.array([100, 4, 10, 8]),
        np.array([operator.sub, operator.add, operator.mul]),
        848,
        848)

    try:
        solution.show()
    except Exception as exc:
        assert False, f"'show()' raised an exception {exc}"
