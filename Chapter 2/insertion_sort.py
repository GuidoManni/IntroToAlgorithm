'''
This is a python implementation of the Insertion Sort algorithm (Chapter 2, Algorithm 2.1, page 44).
Insertion sort is an efficient algorithm for sorting a small number of elements.

Description of the Algorithm:
Input: A sequence of n numbers (a1, a2, ..., an)
Output: A permutation (reordering) (a'1, a'2, ..., a'n) of the input sequence such that a'1 <= a'2 <= ... <= a'n

Pseudocode:
INSERTION-SORT(A, n)
    for i = 2 to n
        key = A[i]
        // Insert A[i] into the sorted subarray A[1:i-1]
        j = i - 1
        while j > 0 and A[j] > key
            A[j+1] = A[j]
            j = j - 1
        A[j + 1] = key

It takes two parameters: an array A containing the values to be sorted and the number n of values of sort.
The values occupy positions A[1] through A[n] of the array, which we denote by A[1:n]. When the
INSERTION-SORT procedure is finished, array A[1:n] contains the original values, but in sorted order.

This algorithm it the best case (when everything is already sorted) has a running time that increase linearly with the
input size (n).
In the worst case (when the array is in reverse order) the algorithm has a running time that increase quadratically as
the size of the array (n) increase.
'''
from utility import generate_random_sequence

def insertion_sort(a: list, n: int) -> list:
    '''
    Sorts a list of n elements using the Insertion Sort algorithm.

    Parameters:
    a (list): The list of elements to be sorted.
    n (int): The number of elements in the list.

    Returns:
    list: The sorted list of elements.
    '''
    for i in range(n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j = j - 1
        a[j+1] = key

    return a


if __name__ == "__main__":
    A = generate_random_sequence(10, 0, 1000)
    print(f"Unsorted A: {A}")

    A_sorted = insertion_sort(A, len(A))
    print(f"Sorted A: {A_sorted}")


