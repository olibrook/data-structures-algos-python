
def sort(arr):
    arr = arr[:]
    quicksort(arr, 0, len(arr)-1)
    return arr


def quicksort(arr, lo, hi):
    if lo < hi:
        p = partition(arr, lo, hi)
        quicksort(arr, lo, p)
        quicksort(arr, p + 1, hi)


def partition(arr, lo, hi):
    pivot = arr[lo]
    while lo < hi:
        while arr[lo] < pivot:
            lo += 1
        while arr[hi] > pivot:
            hi -= 1

        # Swap
        tmp = arr[lo]
        arr[lo] = arr[hi]
        arr[hi] = tmp

    return hi
