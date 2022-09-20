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

        *Note: this command creates a virtual environment located in `./venv` and, once activate, install the package `arithmetic_solver` and its dependencies.*

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

3. Reach the target result using the 4 basic arithmetic operations (+, -, x, ÷) applied to the 6 numbers selected in less than 40 seconds
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
    16 × 4 = 64
    6 − 4 = 2
    64 + 2 = 66
    66 × 9 = 594

Or

    8 × 8 = 64
    64 − 4 = 60
    60 + 6 = 66
    66 × 9 = 594

## Solvers
