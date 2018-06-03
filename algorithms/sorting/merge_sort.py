

def sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) / 2
        left = arr[0:mid]
        right = arr[mid:len(arr)]
        return merge(sort(left), sort(right))


def merge(left, right):
    ret = []
    while len(left) and len(right):
        minimum = left.pop(0) if left[0] <= right[0] else right.pop(0)
        ret.append(minimum)
    ret.extend(left or right)  # Include remainder
    return ret
