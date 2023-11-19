# Sorting-Algorithms

**Overview**
<br>
This project presents a collection of sorting algorithms implemented in Python. It covers a range of sorting techniques, each with unique characteristics and performance implications. The project includes selection sort, bubble sort, insertion sort, hybrid merge sort, and quicksort, catering to diverse sorting needs. Additionally, it features a function to maximize rewards through strategic pairings in a list, showcasing the practical application of sorting algorithms in real-world scenarios.

<br>

**Sorting Algorithms**
<br>
1. Selection Sort: An in-place comparison sorting algorithm. It divides the input list into two parts: a sorted sublist of items already processed and a remaining sublist for the remaining unsorted items.
2. Bubble Sort: A simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
3. Insertion Sort: Builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort.
4. Hybrid Merge Sort: Combines the standard merge sort algorithm with insertion sort to optimize the sorting of smaller sublists.
5. Quicksort: An efficient sorting algorithm, serving as a systematic method for placing the elements of a random access file or an array in order.

<br>

**Features**
<br>
1. Comparator Function: Each sorting algorithm uses a comparator function to determine the order of elements.
2. Ascending and Descending Order: The sorting functions are designed to sort both in ascending and descending order.
3. Hybrid Approach: The hybrid merge sort algorithm uses a threshold to switch to insertion sort for smaller sublists, enhancing performance.
4. Maximize Rewards Function: A special function to pair elements from a list based on their sum and product, maximizing the total reward.

<br>

**Usage**
<br>
To use these sorting algorithms, import the desired function and provide it with a list to sort. You can customize the order using the comparator function.
<br>
from sorting_project import selection_sort, quicksort
<br>
data = [3, 1, 4, 1, 5, 9, 2, 6, 5]
<br>
selection_sort(data)
<br>
print(data)  # Output: [1, 1, 2, 3, 4, 5, 5, 6, 9]
<br>
quicksort(data, lambda x, y: x > y)
<br>
print(data)  # Output: [9, 6, 5, 5, 4, 3, 2, 1, 1]

<br>

**Requirements**
<br>
Python 3.x

<br>

**Authors**
<br>
Nathan Gu
<br>
Blake Potvin
