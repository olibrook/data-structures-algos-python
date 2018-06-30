

def sort(arr):
    arr = arr[:]
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if not min_index == i:
            tmp = arr[i]
            arr[i] = arr[min_index]
            arr[min_index] = tmp
    return arr
