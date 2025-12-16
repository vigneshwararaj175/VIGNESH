def nextGreatestLetter(letters, target):
    n = len(letters)
    left, right = 0, n

    while left < right:
        mid = (left + right) // 2
        if letters[mid] <= target:
            left = mid + 1
        else:
            right = mid

    # If left == n, wrap around to first character
    return letters[left] if left < n else letters[0]
