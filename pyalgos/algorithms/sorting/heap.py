import pyalgos.data_structures.heap as h


def sort(arr):
    heap = h.MinHeap()
    for x in arr:
        heap.add(x)
    return list(heap)
