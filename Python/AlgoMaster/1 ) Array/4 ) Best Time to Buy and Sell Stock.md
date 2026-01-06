Link : https://www.youtube.com/watch?v=kJZrMGpyWpk
#### Brute Force (Time limit exceeds )
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]

                if profit > 0:
                    max_profit = max(profit, max_profit)
        return max_profit
```
#### Own code with the help of youtube video using logic
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            if prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit
```

### Youtube video code
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            
            profit = price - min_price
            
            if profit > max_profit:
                max_profit = profit
        
        return max_profit
```
