# shell_sort.py

def shell_sort(arr: list[float]) -> list[float]:
    """
    Sorts an array using the shell sort algorithm.

    Shell sort is a comparison-based sorting algorithm that generalizes the insertion sort algorithm.
    It starts by sorting pairs of elements far apart from each other, then progressively reduces the gap between elements to be compared.

    Here's a step-by-step breakdown:

    1. Start with a large gap size, typically half the size of the array.
    2. Compare elements at the current gap size and swap them if they are in the wrong order.
    3. Reduce the gap size by half and repeat step 2 until the gap size is 1.

    Examples:

    >>> shell_sort([5, 2, 8, 3, 1])
    [1, 2, 3, 5, 8]

    >>> shell_sort([3.5, 1.2, 2.8, 0.5])
    [0.5, 1.2, 2.8, 3.5]

    >>> shell_sort([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]

    Args:
        arr (list[float]): The array to be sorted.

    Returns:
        list[float]: The sorted array.
    """
    # Implementation of shell sort algorithm
    gap = len(arr) // 2

    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

    return arr  # Make sure to return the sorted array
    pass
