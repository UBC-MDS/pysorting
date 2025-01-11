# pysorting

This package helps the user implement various sorting algorithms.
The package consists of 4 functions:

- `bubble.py`:
  -This function takes in a list of numbers provided by the user and sorts it following a bubble-sort algorithm. The function returns the sorted array to the user
- `insertion_sort.py`:
  -This function takes in a list of numbers provided by the user and sorts it following a insertion-sort algorithm. The function returns the sorted array to the user
- `quicksort.py`:
  -This function takes in a list of numbers provided by the user and sorts it following a quick-sort algorithm. The function returns the sorted array to the user
- `shell_sort.py`:
  -This function takes in a list of numbers provided by the user and sorts it following a shell-sort algorithm. The function returns the sorted array to the user

The package was created with the goal to be a tool for aspiring computer and data scientists to use in order to better understand the steps, similiraities and differences of various sorting functions. With the current functions included, a user can easily pass an array and implement a sorting function of his choosing to return the sorted array. Further developments for this package will include a function to generate a random list of desired size for sorting, one function to compute the big-o complexity of a given sorting algortithm, and a visualization of the sorting process for a chosen algorithm.

## pysorting in the python ecosystem
There are many presences of similar sorting functions within the python ecosystem. For one, python itself already has a built in `sort()` function. Additionally, several packages have also been created with similar goal of implementing various sorting algortithms. One example project is shown here: usehttps://pypi.org/project/sort-algorithms/
Our package aims to distinguish itself from other packages through its easy access to auxiliary tools making it easy to implement various sorting algorithm, and importantly to highlight differences between them.  

## Installation

```bash
$ pip install pysorting
```

## Usage

- TODO

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`pysorting` was created by Group 27. It is licensed under the terms of the MIT license.

## Credits

`pysorting` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
