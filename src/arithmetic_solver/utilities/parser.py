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

import argparse

from arithmetic_solver import __version__

# FUNCTIONS ===================================================================


def parse_args(args):
    """
    Parse command line parameters

    Arguments:
    ----------
      args (List[str]): Command line parameters as list of strings
                        (for example  ``["--help"]``).

    Returns:
    --------
      :obj:`argparse.Namespace`: Command line parameters namespace
    """

    parser = argparse.ArgumentParser(description="Solver of the arithmetic game 'Le Compte est bon' in the French TV game show 'Des Chiffres et des Lettres'")
    parser.add_argument("--version",
                        action="version",
                        version="arithmetic_solver {ver}".format(ver=__version__))
    parser.add_argument(dest="run", help="n-th Fibonacci number", type=int, metavar="INT")
    parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="set loglevel to INFO",
        action="store_const",
        const=logging.INFO,
    )
    parser.add_argument(
        "-vv",
        "--very-verbose",
        dest="loglevel",
        help="set loglevel to DEBUG",
        action="store_const",
        const=logging.DEBUG,
    )
    return parser.parse_args(args)
