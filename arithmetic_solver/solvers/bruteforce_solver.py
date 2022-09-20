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

import itertools as it
import time

import numpy as np

from ..data.parameters import ARITHMETIC_OPERATIONS, N_NUMBERS
from ..data.solution import Solution
from .solver_interface import SolverInterface

# CLASS =======================================================================


class BruteforceSolver(SolverInterface):
    """
    This class implements a bruteforce solver to solve the arithmetic game "Le
    Compte est bon".

    Principle:
    ----------
    This solver computes all possible calculations to find the ones that lead
    to the target result. There may be multiple ways to obtain the target
    result, or there may be none. In the latter case, the best computed solution
    is the closer to the target result.

    Complexity:
    -----------
    """

    def __init__(self):
        """
        Constructor
        """
        super().__init__()
        self._name = "Bruteforce Solver"

    def solve(self, target_result: int, given_numbers: np.array(int)) -> list:
        """

        Args:
            target_result (int): Target value in the range [101, 999]
            given_numbers (np.array): Array of 6 integers from the set
                                      {1 to 10, 25, 50, 75, 100}

        Returns:
            int: The computed value
        """

        print("\n--- PROBLEM SOLVING\n")
        print("Solve this arithmetic problem using the", self._name)

        begin = time.perf_counter()

        self.check_inputs(target_result, given_numbers)

        # Compute all permutations of the given numbers and remove duplicates
        # when there are several occurrences of a number in the initial array
        num_permutations = np.array(list(set(tuple(list(
            it.permutations(given_numbers))))))

        # Remove duplicated permutations
        # Note: it occurs when there are several times the same number
        num_permutations = np.unique(num_permutations, axis=0)

        # Compute all arrangements with repetition of the arithmetic operations
        # Note: there are len(ARITHMETIC_OPERATIONS)^(N_NUMBERS-1) arrangements
        ops_arrangements = np.array(list(it.product(
            list(ARITHMETIC_OPERATIONS.keys()), repeat=N_NUMBERS - 1)))

        # Initialize the closest solution
        self._closest_solution = Solution([], {}, -1, target_result)

        # Loop over all the permutations of the input numbers
        for i in range(num_permutations.shape[0]):

            # Loop over all the possible arrangements of operators
            for j in range(ops_arrangements.shape[0]):

                # Set the result of the current step
                result = num_permutations[i, 0]

                # Perform the calculation operation by operation
                for k in range(ops_arrangements.shape[1]):

                    result = ops_arrangements[j, k](
                        result, num_permutations[i, k + 1])

                    # Store the solution if the target result is reached
                    if result == target_result:
                        self._solutions.append(Solution(
                            num_permutations[i, :],
                            ops_arrangements[j, 0:k + 1],
                            result,
                            target_result))

                    # Else, if no solution yet, store the closest result
                    elif len(self._solutions) == 0:
                        gap = abs(result - target_result)
                        min_gap = abs(
                            self._closest_solution._result - target_result)
                        if gap < min_gap:
                            self._closest_solution = Solution(
                                num_permutations[i, :],
                                ops_arrangements[j, 0:k + 1],
                                result,
                                target_result)

        self.remove_duplicated_solutions()

        self.show_solutions()

        end = time.perf_counter()

        # print(computation)
        print("\nProblem solved in " + str(end - begin) + " seconds\n")

        return []
