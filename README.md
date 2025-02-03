# [pysorting](https://pysorting.readthedocs.io/en/latest/)

[![Documentation Status](https://readthedocs.org/projects/pysorting/badge/?version=latest)](https://pysorting.readthedocs.io/en/latest/?badge=latest)![ci-cd](https://github.com/UBC-MDS/pysorting/actions/workflows/ci-cd.yml/badge.svg) [![codecov](https://codecov.io/gh/UBC-MDS/pysorting/branch/main/graph/badge.svg)](https://app.codecov.io/gh/UBC-MDS/pysorting)

## Overview

This Python package provides an interactive and educational platform for understanding popular sorting algorithms. Designed for students and educators, it includes implementations of four key sorting algorithms. The package is simple to use and highly customizable, making it an excellent tool for learning and teaching sorting concepts.

## Contributors

- Chukwunonso Ebele-muolokwu
- Marek Boulerice
- Shashank Hosahalli Shivamurthy
- Siddarth Subrahmanian

# Features

- `bubble_sort`:
  -This function takes in a list of numbers provided by the user and sorts it following a bubble-sort algorithm. A simple, comparison-based sorting algorithm that repeatedly swaps adjacent elements if they are in the wrong order.
- `insertion_sort`:
  -This function takes in a list of numbers provided by the user and sorts it following a insertion-sort algorithm. A straightforward algorithm that builds the sorted array one element at a time.
- `quick_sort`:
  -This function takes in a list of numbers provided by the user and sorts it following a quick-sort algorithm. Implements the divide-and-conquer sorting algorithm that partitions the array around a pivot element.
- `shell_sort`:
  -This function takes in a list of numbers provided by the user and sorts it following a shell-sort algorithm. A generalization of insertion sort that allows the exchange of far-apart elements to improve performance.

## Time Complexity Measurement

The library allows users to measure the time complexity of a specific sorting function. This helps in optimizing code by choosing the most suitable sorting algorithm for different use cases. For example

- Bubble Sort is efficient for small datasets.
- Insertion Sort performs well for iterables that are partially sorted.

This feature ensures users can make informed decisions about algorithm selection based on their dataset characteristics.

## Comparing Sorting Algorithms

The library provides functionality to compare the performance of two or more sorting functions. By passing in a list, the function identifies and returns the fastest sorting algorithm for the given dataset. This is particularly useful for benchmarking and optimizing your code.

## Checking if a list is sorted

A convenient helper function is included to verify if a list is sorted. It takes a list as input and returns a boolean value:

- True if the list is sorted.
- False otherwise.

This utility is handy for debugging and ensuring the correctness of sorting implementations.

---

The package was created with the goal to be a tool for aspiring computer and data scientists to use in order to better understand the steps, similiraities and differences of various sorting functions. With the current functions included, a user can easily pass an array and implement a sorting function of his choosing to return the sorted array. Further developments for this package will include a function to generate a random list of desired size for sorting, one function to compute the big-o complexity of a given sorting algortithm, and a visualization of the sorting process for a chosen algorithm.

## `pysorting` in the Python Ecosystem

There are many presences of similar sorting functions within the python ecosystem. For one, python itself already has a built in [`.sort()` function](https://docs.python.org/3/library/stdtypes.html#list.sort). There is also a [`sorted()` built-in function](https://docs.python.org/3/library/functions.html#sorted) that builds a new sorted list from an iterable.Additionally, several packages have also been created with similar goal of implementing various sorting algortithms. One example project is shown here: [https://pypi.org/project/sort-algorithms/](https://github.com/DahlitzFlorian/SortingAlgorithms)
Our package aims to distinguish itself from other packages through its easy access to auxiliary tools making it easy to implement various sorting algorithm, and importantly to highlight differences between them.  

## Installation

```bash
pip install pysorting
```

## Usage

The following examples illustrate how the sorting functions in this package are intended to be used. Please note that the functions are currently not implemented—only their docstrings are in place for now.

After installing the package, you can import the functions (once implemented) as follows:

```python
from pysorting import quick_sort, bubble_sort, shell_sort, insertion_sort

bubble_sort([4, 2, 7, 1, 3], ascending = False)
```

For more examples on usage of the different functions,you can check out this [Example NoteBook](https://pysorting.readthedocs.io/en/latest/example.html)

## Contributing

Interested in contributing? Check out the [contributing guidelines](https://github.com/UBC-MDS/pysorting/blob/main/CONTRIBUTING.md). Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`pysorting` was created by Nonso, Marek, Siddarth, Shashank. It is licensed under the terms of the MIT license.

## Credits

`pysorting` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
