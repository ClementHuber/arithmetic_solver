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

import numpy as np

from arithmetic_solver.solvers.solver_interface import SolverInterface

from .data.parameters import (DATASET, GAME_RULES, N_NUMBERS, TARGET_MAX,
                              TARGET_MIN)

# MAIN ========================================================================


def main():
    """
    This function runs the Arithmetic Solver program.
    """

    print("===========================================================")
    print("                Des Chiffres et des Lettres")
    print("                   - Le Compte est Bon -")
    print("===========================================================\n")

    print("--- RULES\n")

    print(GAME_RULES)

    print("--- RANDOM DRAWS\n")

    # Random generation of a target integer between 101 and 999
    target = np.random.randint(TARGET_MIN, high=TARGET_MAX + 1)

    # Random selection of 6 positive integers in the dataset
    numbers = np.random.choice(DATASET, size=N_NUMBERS)

    print("- Random draw of the target value:", target)
    print("- Random draw of 6 numbers:",
          ", ".join(map(str, numbers.tolist())))

    # Solve the arithmetic problem
    solver = SolverInterface()
    solver.solve(target, numbers)

    print("===========================================================\n")
    # End


if __name__ == "__main__":
    # Execute only if run as a script
    main()
