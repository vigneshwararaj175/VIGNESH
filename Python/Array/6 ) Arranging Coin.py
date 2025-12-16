def arrangeCoins(n: int) -> int:
    left, right = 1, int((2*n)**0.5) + 1
    while left <= right:
        mid = (left + right) // 2
        total = mid * (mid + 1) // 2
        if total == n:
            return mid
        elif total < n:
            left = mid + 1
        else:
            right = mid - 1
    return right  # right is the largest satisfying total <= n
