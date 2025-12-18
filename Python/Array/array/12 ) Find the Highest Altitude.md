```python
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxs = 0
        sums = 0
        for i in gain:
            sums += i
            if maxs < sums:
                maxs = sums
        return maxs
```
