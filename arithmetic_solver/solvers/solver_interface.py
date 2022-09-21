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

from abc import ABCMeta, abstractmethod

import numpy as np

from ..data.parameters import TARGET_MIN, TARGET_MAX, DATASET, N_NUMBERS
from ..data.solution import Solution

# CLASS =======================================================================


class SolverInterface(metaclass=ABCMeta):
    """
    This abstract class defines the solvers API that solve the arithmetic game
    "Le Compte est bon".

    Attributes:
    -----------
    - _name             : Solver name
    - _solutions        : List of solutions
    - _closest_solution : Closest solution if there is no exact solution found

    Methods:
    --------
    - solve (abstract method)     : API to launch the solver
    - check_inputs                : Check the arguments provided to the solver
    - remove_duplicated_solutions : Remove eventual duplicates amon solutions
    - show_solutions              : Print all computed solutions
    """

    def __init__(self):
        """
        Constructor
        """

        self._name = "Solver Interface"

        # List of solutions
        self._solutions = []

        # Closest solution if there is no exact solution found
        self._closest_solution = Solution(np.array([]), np.array([]), -1, -1)

    @abstractmethod
    def solve(self, target_value: int, given_numbers: np.array(int)) -> None:
        """
        This function solves the arithmetic problem "Le Compte est bon"

        It is supposed to:
        1. check inputs
        2. compute the solution(s) or the closest solution
        3. show the computed solutions

        Arguments:
        ----------
        - target_value (int): Target value in the range [TARGET_MIN,TARGET_MAX]
        - given_numbers (np.array): Array of N_NUMBERS integers from DATASET
        """
        raise NotImplementedError()

    def check_inputs(
            self, target_value: int, given_numbers: np.array(int)) -> bool:
        """
        This function checks that inputs comply with the game rules. If a check
        fails, a ValueError() is raised.

        Arguments:
        ----------
        - target_value (int): Target value
        - given_numbers (np.array): Array of given numbers

        Returns:
        --------
            bool: True if inputs are correct, else False
        """

        # Check if the target value is in the right range
        target_range = np.linspace(
            TARGET_MIN, TARGET_MAX, num=TARGET_MAX - TARGET_MIN + 1, dtype=int)

        if target_value not in target_range:

            message = ["The target value (= ", str(target_value),
                       ") must be within [", str(TARGET_MIN), ", ",
                       str(TARGET_MAX)]
            message = "".join(message)

            raise ValueError(message)
            return False

        # Check if there are the right quantity of numbers
        if len(given_numbers) != N_NUMBERS:

            message = ["There must be ",
                       str(N_NUMBERS),
                       " initial numbers but there are ",
                       str(len(given_numbers))]
            message = "".join(message)

            raise ValueError(message)
            return False

        # Check if the initial numbers are in the right dataset
        for num in given_numbers:
            if num not in DATASET:

                message = [
                    "Initial numbers must be selected from this dataset: {",
                    ", ".join(map(str, DATASET.tolist())),
                    "} but given numbers are: {",
                    ", ".join(map(str, given_numbers.tolist())),
                    "}"]
                message = "".join(message)

                raise ValueError(message)
                return False

        return True

    def remove_duplicated_solutions(self) -> None:
        """
        This function remove the eventual duplicates among solutions
        """
        self._solutions = list(set(self._solutions))

    def show_solutions(self) -> None:
        """
        This function print all computed solutions
        """

        print("\n--- SOLUTIONS\n")

        if len(self._solutions) > 0:
            print(str(len(self._solutions) + 1) + " solutions found!")

            for i in range(len(self._solutions)):
                print("\nSolution #" + str(i + 1))
                self._solutions[i].show()

        else:
            print("No exact solution found, the closest solution is:")
            self._closest_solution.show()
