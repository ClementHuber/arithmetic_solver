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

import numpy as np

from .parameters import ARITHMETIC_OPERATIONS

# CLASS =======================================================================


class Solution:
    """
    This class defines a Solution object.

    Attributes:
    -----------
    - _numbers      : Ordered array of the input numbers
    - _operators    : Ordered operations to apply on the input numbers
    - _result       : Computed result given the numbers and the operations
    - _target_result: Expected result
    """

    def __init__(self,
                 numbers: np.array,
                 operators: np.array,
                 result: int,
                 target: int) -> None:
        """
        Constructor

        Arguments:
        ----------
            numbers (np.array): Ordered array of the input numbers
            operators (np.array): Ordered operations to apply on numbers
            result (int): Computed result given the numbers and the operations
            target (int): Expected result
        """
        self._numbers = numbers
        self._operators = operators
        self._result = result
        self._target_result = target

    def __eq__(self, other: object) -> bool:
        """
        This function overloads the operator == to check if 2 Solution objects
        are equal: self == other ?

        Arguments:
        ----------
            other (Solution): Other Solution object to compare self with

        Returns:
        --------
            bool: True if self == other, else False
        """
        if isinstance(other, Solution):
            return (np.array_equal(self._numbers, other._numbers) and
                    np.array_equal(self._operators, other._operators) and
                    self._result == other._result and
                    self._target_result == other._target_result)
        else:
            return False

    def __ne__(self, other: object) -> bool:
        """
        This function overloads the operator != to check if 2 Solution objects
        are not equal: self != other ?

        Arguments:
        ----------
            other (Solution): Other Solution object to compare self with

        Returns:
        --------
            bool: True if self != other, else False
        """
        return not self == other

    def __hash__(self) -> int:
        """
        This function overloads the hash method so a Solution object is
        hashable.

        Note: it is used here when calling set() to remove duplicated solutions

        Returns:
        --------
            int: The hash of the object
        """
        return hash(("numbers", tuple(self._numbers.tolist()),
                     "operators", tuple(self._operators.tolist()),
                     "result", self._result,
                     "target_result", self._target_result))

    def le_compte_est_bon(self) -> bool:
        """
        This function checks that the computed result is the target result

        Returns:
        --------
            bool: True if computed result == target result, else False
        """
        return self._result == self._target_result

    def show(self) -> None:
        """
        This function prints the computation steps and the computed results.
        If the computed results is the target result, then it also prints:
                            "Le compte est bon !"
        Else, it prints the difference between the result and the target.
        """

        print("Computation steps:\n")

        # Initialization
        intermediate_result = self._numbers[0]

        # Loop over the computation steps
        for i in range(len(self._operators)):

            step = "\t" + str(intermediate_result) + " "
            step += ARITHMETIC_OPERATIONS[self._operators[i]] + " "
            step += str(self._numbers[i + 1]) + " "

            # Perform the operation of the computation step
            intermediate_result = self._operators[i](
                intermediate_result, self._numbers[i + 1])

            step += "= " + str(intermediate_result)

            # Print the computation step
            print(step)

        print("")

        # Check that the computed result is the target one
        if self.le_compte_est_bon():
            print("Le compte est bon !")
        else:
            print("Difference to the target number:",
                  self._result - self._target_result)
