

def binary_search(arr, val):
    """The array must be sorted for binary search to work."""
    left = 0
    right = len(arr)
    result = -1
    while left < right:
        mid = left + (right - left) / 2
        if arr[mid] < val:
            left = mid + 1
        elif arr[mid] > val:
            right = mid
        else:
            # This is a match, but keep searching to
            # the left to handle duplicates
            result = mid
            right = mid
    return result


def test():
    assert binary_search([], 'a') == -1
    assert binary_search(['a'], 'a') == 0
    assert binary_search(['a', 'b'], 'b') == 1
    assert binary_search(['a'] * 50, 'a') == 0
    print('ok')

if __name__ == '__main__':
    test()
