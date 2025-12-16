def findKthPositive(arr, k):
    n = len(arr)
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        missing = arr[mid] - mid - 1
        if missing < k:
            left = mid + 1
        else:
            right = mid - 1
    # After loop, left is the smallest index with missing >= k
    # If left == n, all missing counts < k
    return k + left
