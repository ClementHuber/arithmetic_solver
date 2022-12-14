# Arithmetic Solver

## Brief

Solver of the arithmetic game *"Le Compte est bon"* in the French TV game show *"Des Chiffres et des Lettres"* (*cf.* [Wikipedia](https://en.wikipedia.org/wiki/Des_chiffres_et_des_lettres#Numbers_round) or the [official website](https://www.france.tv/france-3/des-chiffres-et-des-lettres/)).

## Table of contents

- [Arithmetic Solver](#arithmetic-solver)
  - [Brief](#brief)
  - [Table of contents](#table-of-contents)
  - [Quick Start Guide](#quick-start-guide)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Usage](#usage)
  - [Rules of the game](#rules-of-the-game)
    - [Course of the game](#course-of-the-game)
      - [Notes](#notes)
    - [Example](#example)
  - [Solvers](#solvers)
    - [Bruteforce solver](#bruteforce-solver)
      - [Approach](#approach)
  - [TODO](#todo)

## Quick Start Guide

### Prerequisites

- Python >= 3.8
  - virtualenv >= 20.16.5
  - pip >= 22.2.2
- GNU Make

### Installation

1. Clone the repository:

    ```bash
    git clone git@github.com:ClementHuber/arithmetic_solver.git
    ```

2. Enter the repository:

   ```bash
   cd <path/to/arithmetic_solver>
   ```

3. Install the Python package according to your future usage:
   1. in *user* mode:

        ```bash
        make install
        ```

   2. in *dev* mode:

        ```bash
        make install-dev
        ```

        *Note: this command creates a virtual environment located in `./venv` and, once activated, install the package `arithmetic_solver` and its dependencies.*

### Usage

1. Activate the virtual environment:

    ```bash
    make activate
    ```

2. Launch the program:

    ```bash
    arithmetic_solver
    ```

3. Deactivate the virtual environment when you are done

    ```bash
    deactivate
    ```

4. Enjoy!

## Rules of the game

### Course of the game

1. Draw a target integer randomly in the range [101, 999]
2. Draw 6 integers in the dataset: `{[1, 10], 25, 50, 75, 100}`

    *(each number is drawn from the entire set, so the same number may appear more than once)*

3. Reach the target result using the 4 basic arithmetic operations (+, -, x, ??) applied to the 6 numbers selected in less than 40 seconds
4. If the target result is reached, say *"Le compte est bon !"*

#### Notes

- Each one of the 6 numbers selected can be used once maximum
- It is not mandatory to use all numbers
- The result of each operation can be used once maximum
- There may be multiple ways to compute the target result
- If there is no solution (*i.e.* the target number cannot be reached), the goal is to find the closest number

### Example

- Numbers given: `8`, `4`, `4`, `6`, `8`, `9`
- Target number: `594`

Computation steps:

    8 + 8 = 16
    16 ?? 4 = 64
    6 ??? 4 = 2
    64 + 2 = 66
    66 ?? 9 = 594

Or

    8 ?? 8 = 64
    64 ??? 4 = 60
    60 + 6 = 66
    66 ?? 9 = 594

## Solvers

### Bruteforce solver

#### Approach

This solver computes all possible calculations to find the ones that lead to the target result.

1. Compute all permutations of the given numbers (6! = 720 permutations)
2. Compute all arrangements with repetition of the 5 arithmetic operators - chosen among the 4 basic operators (+, -, x, ??) - to be applied to the given numbers (4^5 = 1 024 arrangements)
3. Init the result of the current configuration
4. Compute the result for all possible configurations:
   - For all permutations of the given numbers
     - For all arrangements of operators
       - Apply each operator of the current arrangement successively on the previous result and the next number in the current permutation
5. Remove duplicates among the computed solutions

The **computational complexity** of this algorithm is: `N! * 4^(N-1) * N ~ O(N!)`

## TODO

- UML diagram of the architecture
- Unit tests
