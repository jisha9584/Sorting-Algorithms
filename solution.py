"""
Nathan Gu and Blake Potvin
Sorting Project - Starter
CSE 331 Fall 2023
"""

import random
import time
from typing import TypeVar, List, Callable, Dict, Tuple
from dataclasses import dataclass

T = TypeVar("T")  # represents generic type


# do_comparison is an optional helper function but HIGHLY recommended!!!
def do_comparison(first: T, second: T, comparator: Callable[[T, T], bool], descending: bool) -> bool:
    """
    Compares two elements based on a provided comparator and a descending flag.

    Parameters:
    - first (T): The first element for comparison.
    - second (T): The second element for comparison.
    - comparator (Callable[[T, T], bool]): Comparator function to define the sorting order.
    - descending (bool): Flag indicating whether sorting should be in descending order.

    Returns:
    bool: True if 'first' should precede 'second', False otherwise.
    """
    # Use the comparator function to compare the elements
    comparison_result = comparator(first, second)

    # If sorting in descending order, reverse the comparison result
    if descending:
        return comparator(second, first)
    else:
        return comparison_result


def selection_sort(data: List[T], *, comparator: Callable[[T, T], bool] = lambda x, y: x < y,
                   descending: bool = False) -> None:
    """
    Performs in-place selection sort on a given list using a provided comparator.

    Parameters:
    - data (List[T]): List of elements to be sorted.
    - comparator (Callable[[T, T], bool]): Function to compare two elements. Returns True if first element is less than the second.
    - descending (bool): If True, sorts the list in descending order. Defaults to False.

    Returns:
    None
    """
    n = len(data)

    for i in range(n - 1):
        min_max_index = i

        # Find the index of the minimum (or maximum) element in the unsorted portion
        for j in range(i + 1, n):
            if do_comparison(data[j], data[min_max_index], comparator, descending):
                min_max_index = j

        # Swap the current element with the minimum (or maximum) element found
        if i != min_max_index:
            data[i], data[min_max_index] = data[min_max_index], data[i]


def bubble_sort(data: List[T], *, comparator: Callable[[T, T], bool] = lambda x, y: x < y,
                descending: bool = False) -> None:
    """
    Sorts a list in-place using the bubble sort algorithm with the provided comparator.

    Parameters:
    - data (List[T]): List of items to be sorted.
    - comparator (Callable[[T, T], bool]): Function to compare two elements. Returns True if the first element is less than the second.
    - descending (bool): If True, sorts the list in descending order. Defaults to False.

    Returns:
    None
    """
    n = len(data)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            # Use the do_comparison function to compare adjacent elements
            if do_comparison(data[j+1], data[j], comparator, descending):
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True

        # If no swaps were made in this pass, the list is already sorted
        if not swapped:
            break


def insertion_sort(data: List[T], *, comparator: Callable[[T, T], bool] = lambda x, y: x < y,
                   descending: bool = False) -> None:
    """
    Sorts a list in-place using the insertion sort algorithm with the provided comparator.

    Parameters:
    - data (List[T]): List of items to be sorted.
    - comparator (Callable[[T, T], bool]): Function to compare two elements. Returns True if the first element is less than the second.
    - descending (bool): If True, sorts the list in descending order. Defaults to False.

    Returns:
    None
    """
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and do_comparison(key, data[j], comparator, descending):
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key


def hybrid_merge_sort(data: List[T], *, threshold: int = 12,
                      comparator: Callable[[T, T], bool] = lambda x, y: x < y, descending: bool = False) -> None:
    """
    Sorts a list in-place using a hybrid merge sort algorithm. Uses insertion sort for smaller sublists.

    Parameters:
    - data (List[T]): List of elements to be sorted.
    - threshold (int): The size limit for sublists where insertion sort is used instead of merge sort. Defaults to 12.
    - comparator (Callable[[T, T], bool]): Function to compare two elements. Returns True if the first element is less than the second.
    - descending (bool): If True, sorts the list in descending order. Defaults to False.

    Returns:
    None
    """

    if len(data) > 1:
        if len(data) <= threshold:
            insertion_sort(data, comparator=comparator, descending=descending)
        else:
            mid = len(data) // 2
            left = data[:mid]
            right = data[mid:]

            hybrid_merge_sort(left, threshold=threshold, comparator=comparator, descending=descending)
            hybrid_merge_sort(right, threshold=threshold, comparator=comparator, descending=descending)

            i = j = k = 0
            while i < len(left) and j < len(right):
                if do_comparison(left[i], right[j], comparator, descending):
                    data[k] = left[i]
                    i += 1
                else:
                    data[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                data[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                data[k] = right[j]
                j += 1
                k += 1


def maximize_rewards(item_prices: List[int]) -> (List[Tuple[int, int]], int):
    """
    Determines the maximum possible rewards that can be obtained by pairing the given
    `item_prices` such that the sum of each pair remains consistent throughout the entire
    list of pairs. The reward for each pair is calculated as the product of the two numbers in the pair.

    Parameters:
    - item_prices (List[int]): A list of integers representing the prices of items.

    Returns:
    - Tuple[List[Tuple[int, int]], int]: A tuple containing two elements:
        1. A list of tuples, where each tuple contains a pair of numbers from `item_prices`
           that together sum up to a common sum.
        2. An integer representing the total reward, which is the sum of the products of each pair.
           If it's not possible to create pairs with a consistent sum, the function returns an
           empty list and a reward of -1.
    """

    # Check for empty list or odd length
    if not item_prices or len(item_prices) % 2 != 0:
        return ([], -1)

    # Use hybrid merge sort instead of built-in sort
    hybrid_merge_sort(item_prices)

    # Calculate the common sum using the first and last element after sorting
    common_sum = item_prices[0] + item_prices[-1]

    pairs = []
    rewards = 0

    left, right = 0, len(item_prices) - 1

    while left < right:
        # If the current pair doesn't match the common sum, it's not possible
        if item_prices[left] + item_prices[right] != common_sum:
            return ([], -1)

        pairs.append((item_prices[left], item_prices[right]))
        rewards += item_prices[left] * item_prices[right]

        left += 1
        right -= 1

    return (pairs, rewards)

def quicksort(data) -> None:
    """
    Sorts a list in place using quicksort
    :param data: Data to sort
    """

    def quicksort_inner(first, last) -> None:
        """
        Sorts portion of list at indices in interval [first, last] using quicksort

        :param first: first index of portion of data to sort
        :param last: last index of portion of data to sort
        """
        # List must already be sorted in this case
        if first >= last:
            return

        left = first
        right = last

        # Need to start by getting median of 3 to use for pivot
        # We can do this by sorting the first, middle, and last elements
        midpoint = (right - left) // 2 + left
        if data[left] > data[right]:
            data[left], data[right] = data[right], data[left]
        if data[left] > data[midpoint]:
            data[left], data[midpoint] = data[midpoint], data[left]
        if data[midpoint] > data[right]:
            data[midpoint], data[right] = data[right], data[midpoint]
        # data[midpoint] now contains the median of first, last, and middle elements
        pivot = data[midpoint]
        # First and last elements are already on right side of pivot since they are sorted
        left += 1
        right -= 1

        # Move pointers until they cross
        while left <= right:
            # Move left and right pointers until they cross or reach values which could be swapped
            # Anything < pivot must move to left side, anything > pivot must move to right side
            #
            # Not allowing one pointer to stop moving when it reached the pivot (data[left/right] == pivot)
            # could cause one pointer to move all the way to one side in the pathological case of the pivot being
            # the min or max element, leading to infinitely calling the inner function on the same indices without
            # ever swapping
            while left <= right and data[left] < pivot:
                left += 1
            while left <= right and data[right] > pivot:
                right -= 1

            # Swap, but only if pointers haven't crossed
            if left <= right:
                data[left], data[right] = data[right], data[left]
                left += 1
                right -= 1

        quicksort_inner(first, left - 1)
        quicksort_inner(left, last)

    # Perform sort in the inner function
    quicksort_inner(0, len(data) - 1)
