https://leetcode.com/problems/missing-number/
### Own Solution
```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        for j in range(0,len(nums)):
            if j != nums[j]:
                return j
        return j + 1
```
### 2 )
```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        actual_sum =  n * (n + 1) // 2
        list_sum = sum(nums)
        return actual_sum - list_sum
```

### 3 ) 
```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
```
