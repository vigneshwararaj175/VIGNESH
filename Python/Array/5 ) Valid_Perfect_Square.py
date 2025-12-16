class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start, end = 0, num // 2
        while start <= end:
            mid = start + (end - start) // 2
            sq = mid * mid
            if sq == num:
                return True
            elif sq < num:
                left = mid + 1
            else:
                right = mid - 1
        return False

            
