```python
class Solution:
    def count_digit(self, num):
        count = 0
        while num != 0:
            num = num // 10
            count += 1
        if count % 2 == 0:
            return True
    
    def findNumbers(self, nums: List[int]) -> int:
        even_digit = 0
        for i in nums:
            if self.count_digit(i):
                even_digit += 1
        return even_digit
```
    

