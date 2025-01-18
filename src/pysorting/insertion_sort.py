# insertion_sort.py
# author: Marek Boulerice
# date: 2024-01-10

def insertion_sort(unsorted[float]):
    """
    Performs insertion sorting algorithm on given list and returns new sorted list.

    This function takes in a single list as a parameter. It performs insertion sorting via the following algorithm:
        1. Begin with the second item in the list. 
        2. Compare the value of the item with the value of the item to its immediate left. 
        If the value is smaller than the item to its left, switch the position of the two items
        3. If If the value is larger than the item to its left, or if the item is in the first position of the list, stop. Otherwise repeat step 2.
        4. Repeat steps 2 and 3 for the next unchecked item, until all items have been checked
    After completing insertion sorting, function will return the newly sorted array
    
    Parameters
    ----------
    unsorted : list[float]
        a list of float values to be sorted

    Returns
    -------
    list[float]
        The list of sorted values.

    Examples
    ------
    insertion_sort([8, 2, 12, 5, 1])
    [1, 2, 5, 8, 12]

    insertion_sort([0.1, 0, 12, 0, 100.01])
    [0, 0, 0.1, 12, 100.01]
    """
    pass