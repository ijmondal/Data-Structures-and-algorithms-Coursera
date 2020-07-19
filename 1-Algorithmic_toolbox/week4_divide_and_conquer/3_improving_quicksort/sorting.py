# Uses python3
import sys
import random

def partition3(A, l, r):

    lt = l  # We initiate lt to be the part that is less than the pivot
    i = l   # We scan the array from left to right
    gt = r  # The part that is greater than the pivot
    pivot = A[l]    # The pivot, chosen to be the first element of the array, that why we'll randomize the first elements position
                    # in the quick_sort function.
    while i <= gt:      # Starting from the first element.
        if A[i] < pivot:
            A[lt], A[i] = A[i], A[lt]
            lt += 1
            i += 1
        elif A[i] > pivot:
            A[i], A[gt] = A[gt], A[i]
            gt -= 1
        else:
            i += 1
            
    return lt, gt



def quick_sort(A, l, r):
    """
    quick_sort: One of the most used sorting algorithm. 
    It makes to recursive calls. One to sort the left part separately, other for sorting the right part.
    The partition key is chosen randomly via ``random.randint(l, r)`` and it's between the ``l,  r``.
    
    PARAMETERS:
    -----------
    A: Array or the sequence that we want to sort.
    l: The lower bound of the array that we want to sort. It's not very important we might replace it by a wrapper function
    that only takes in an array as input. In this case it's the first element in the left part of the array.
    r: It's the same as l, only differs as it's the first element from the end.
    
    RETURNS:
    -------
    Sorted list A.
    """
    if l >= r:
        return
    k = random.randint(l, r)
    A[k], A[l] = A[l], A[k]
    
    lt, gt = partition3(A, l, r)
    quick_sort(A, l, lt - 1)
    quick_sort(A, gt + 1, r)  

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m = partition2(a, l, r)
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, m + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
