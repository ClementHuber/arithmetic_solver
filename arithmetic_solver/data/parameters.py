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

# PARAMETERS ==================================================================

# Bounds of the interval from which the target value is drawn
TARGET_MIN = 101
TARGET_MAX = 999

# Given dataset from are drawn 6 numbers
DATASET = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 25, 50, 75, 100])

# Number of initial numbers drawn
N_NUMBERS = 6

# Allowed arithmetic operations
ARITHMETIC_OPERATIONS = {operator.add: "+",
                         operator.sub: "-",
                         operator.mul: "*",
                         operator.floordiv: "/"}

# Game rules
GAME_RULES = [
    "Course of the game:",
    "",
    "1. Draw a target integer randomly in the range [101, 999]",
    "2. Draw 6 integers in the dataset:",
    "                  {[1, 10], 25, 50, 75, 100}",
    "   (each number is drawn from the entire set, so the same",
    "   number may appear more than once)",
    "3. Reach the target value using the 4 basic arithmetic",
    "   operations (+, -, x, ÷) applied to the 6 numbers",
    "   selected in less than 40 seconds",
    "4. If the target value is reached, say 'Le compte est bon !'",
    "",
    "Notes:",
    "",
    "- Each one of the 6 numbers selected can be used once maximum",
    "- It is not mandatory to use all numbers",
    "- The result of each operation can be used once maximum",
    "- If there is no solution (i.e. the target number cannot be",
    "  reached), the goal is to find the closest number",
    ""
]

GAME_RULES = "\n ".join(GAME_RULES)
