

def sort(arr):
    arr = arr[:]
    for i in range(len(arr)):
        curr = i
        prev = curr - 1
        while prev >= 0 and arr[curr] < arr[prev]:
            tmp = arr[prev]
            arr[prev] = arr[curr]
            arr[curr] = tmp
            curr = curr - 1
            prev = prev - 1
    return arr
