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

# IMPORTS =====================================================================

import sys
import numpy as np

from arithmetic_solver import __version__

from .data.parameters import (DATASET, GAME_RULES, N_NUMBERS, TARGET_MAX,
                              TARGET_MIN)
from .solvers.bruteforce_solver import BruteforceSolver

from .utilities.parser import _logger, setup_logging

# MAIN ========================================================================


def main(args):
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
    solver = BruteforceSolver()
    solver.solve(target, numbers)

    print("===========================================================\n")
    # End


def run():
    """
    Calls :func:`main` passing the CLI arguments extracted from :obj:`sys.argv`

    This function can be used as entry point to create console scripts with
    setuptools.
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    # Execute only if run as a script
    run()


# """Wrapper allowing :func:`fib` to be called with string arguments in a CLI fashion

#     Instead of returning the value from :func:`fib`, it prints the result to the
#     ``stdout`` in a nicely formatted message.

#     Args:
#       args (List[str]): command line parameters as list of strings
#           (for example  ``["--verbose", "42"]``).
#     """
#     args = parse_args(args)
#     setup_logging(args.loglevel)
#     _logger.debug("Starting crazy calculations...")
#     print("The {}-th Fibonacci number is {}".format(args.n, fib(args.n)))
#     _logger.info("Script ends here")
