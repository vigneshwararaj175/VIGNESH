### Own Solution - Time complexcity ( Time limit exceeded )
```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums) // 2
        n = len(nums)
        
        for i in range(n):
            count = 0
            for j in range(n):
                if nums[i] == nums[j]:
                    count += 1
                if count > majority:
                    return nums[i]
```
### See through the remaining programs
```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        res, maxCount = 0, 0
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            res = n if count[n] > maxCount else res
            maxCount = max(count[n], maxCount)
        return res
```

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0
        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
        return res
```
