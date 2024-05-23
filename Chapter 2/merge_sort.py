'''
This is a python implementation of the Merge Sort algorithm (Chapter 2, Algorithm 2.3.1, page 64).
This algorithm follow the divide-and-conquer method: they break the problem into several subproblems that are
similar to the original problem but smaller in size, solve the problems recursively, and then combine these solutions
to create a solution to the original problem.
The merge sort algorithm in each step, it sorts a subarray A[p:r], starting with the entire array A[1:n] and recursing
down to smaller and smaller subarrays.
Following the divide-and-conquer methods we can distinguish 3 phases of the sorting procedure:
- Divide: the subarray A[p:r] to be sorted into two adjacent subarrays, each of half the size. To do so,
  compute the midpoint q of A[p:r] (taking the average of p and r), and divide A[p:r] into two subarrays
  A[p:q] and A[q+1:r]
- Conquer: by sorting each of the two subarrays A[p:q] and A[q+1:r] recursively using merge sort
- Combine: by merging the two sorted subarrays A[p:q] and A[q+1:r] back into A[p:r], producing the sorted answer

the merge sort algorithm uses an auxilary function to perform the merging.

Pseudocode:
MERGE(A, p, q, r)
    nl = q - p + 1 \\ length of A[p:q]
    nr = r - q \\ length of A[q + 1:r]
    let L[0 : nl - 1] and R[0 : nr - 1] be new arrays

    for i = 0 to nl - 1 // copy A[p:q] into L[0:nl - 1]
        L[i] = A[p+i]

    for j = 0 to nr - 1 // copy A[q + 1 : r] into R[0 : nr-1]
        R[j] = A[q+j+1]

    i = 0 // i indexes the smallest remaining element in L
    j = 0 // j indexes the smallest remaining element in R
    k = p // k indexes the location A to fill

    // As long as each of the arrays L and R contains un unmerged element, copy the smallest unmerged element back
    // into A[p:r].

    while i < nl and j < nr
        if L[i] <= R[j]
            A[k] = L[i]
            i = i + 1
        else A[k] = R[j]
            j = j + 1
        k = k + 1

    // Having gone through one of L and R entirely, copy the remainder of the other to the end of A[p:r]
    while i < nl
        A[k] = L[i]
        i = i + 1
        k = k + 1
    while j < nr
        A[k] = R[j]
        j = j + 1

MERGE-SORT(A, p, r)
    if p >= r // zero or one element?
        return A
    q = (p + r)/ 2 // midpoint of A[p:r]

    MERGE-SORT(A, p, q) // recursively sort A[p:q]
    MERGE-SORT(A, q + 1, r) // recursively sort A[q + 1: r]
    // MERGE A[p:q] and A[q+1, r] into A[p:r]
    MERGE(A, p, q, r)

'''
from utility import generate_random_sequence
import sys
sys.setrecursionlimit(10000)



def merge(a: list, p: int, q: int, r: int):
    L = a[p:q+1]  # Include the element at index q
    nl = len(L)
    R = a[q+1:r+1]  # Include the element at index r
    nr = len(R)
    i = 0
    j = 0
    k = p

    # As long as each of the arrays L and R contains an unmerged element, copy the smallest unmerged element back into
    # A[p:r]
    while i < nl and j < nr:
        if L[i] <= R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
        k += 1

    # Having gone through one of L and R entirely, copy the remainder of the other to the end of A[p:r]
    while i < nl:
        a[k] = L[i]
        i += 1
        k += 1

    while j < nr:
        a[k] = R[j]
        j += 1
        k += 1

def merge_sort(a: list, p: int, r: int):
    if p>=r:
        return a

    q = int((p + r)/2)
    merge_sort(a, p, q)
    merge_sort(a, q+1, r)
    merge(a, p, q, r)


if __name__ == "__main__":
    A = generate_random_sequence(10, 0, 1000)
    print(f"Unsorted A: {A}")

    merge_sort(A, 0, len(A) - 1)  # Use len(A) - 1 instead of 10
    print(f"Sorted A: {A}")


# TODO: continue reading 2.3.2 (pag. 71)
