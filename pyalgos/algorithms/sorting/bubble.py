
def sort(arr):
    arr = arr[:]
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr) - 1):
            if arr[j + 1] < arr[j]:
                tmp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = tmp
                swapped = True
        if not swapped:
            break
    return arr
