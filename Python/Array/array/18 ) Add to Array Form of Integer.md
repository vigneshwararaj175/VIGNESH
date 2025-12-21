This problem can be solved efficiently using **digit-by-digit addition with carry processing**, similar to how we add numbers manually. Here's the approach:

## Method Used: **Digit-by-Digit Addition with Carry Processing**

### Step-by-step approach:
1. **Start from the least significant digit** (rightmost digit of `num`)
2. **Process digits one by one** while also processing `k` from least significant digit
3. **Maintain a carry** to handle sums ≥ 10
4. **Build the result in reverse order**, then reverse it at the end

### Time Complexity: **O(max(n, log k))**
### Space Complexity: **O(max(n, log k))** for the result

### Python Implementation:
```python
def addToArrayForm(num, k):
    result = []
    i = len(num) - 1
    carry = 0
    
    # Process both num and k until both are exhausted
    while i >= 0 or k > 0 or carry > 0:
        # Get current digit from num (if available)
        digit_from_num = num[i] if i >= 0 else 0
        
        # Get current digit from k
        digit_from_k = k % 10
        
        # Calculate sum
        total = digit_from_num + digit_from_k + carry
        
        # Update result with current digit
        result.append(total % 10)
        
        # Update carry
        carry = total // 10
        
        # Move to next digits
        if i >= 0:
            i -= 1
        k //= 10
    
    # Reverse result since we built it from least to most significant
    return result[::-1]
```

### Alternative Approach (Converting k to array form):
```python
def addToArrayForm(num, k):
    # Convert k to array form (digits in reverse order)
    k_digits = []
    while k > 0:
        k_digits.append(k % 10)
        k //= 10
    
    # If k is 0, k_digits will be empty
    if not k_digits:
        k_digits = [0]
    
    result = []
    carry = 0
    i = len(num) - 1
    j = 0
    
    # Add corresponding digits
    while i >= 0 or j < len(k_digits) or carry > 0:
        a = num[i] if i >= 0 else 0
        b = k_digits[j] if j < len(k_digits) else 0
        
        total = a + b + carry
        result.append(total % 10)
        carry = total // 10
        
        if i >= 0:
            i -= 1
        j += 1
    
    return result[::-1]
```

### Why this method works best:
1. **Handles large numbers efficiently** - We don't convert the entire array to an integer (which could overflow with very large arrays)
2. **Works with constraints** - `num.length` up to 10⁴ would make integer conversion problematic
3. **Memory efficient** - Only requires space for the result
4. **Simple and intuitive** - Mimics manual addition

### Example Walkthrough (num = [2,1,5], k = 806):
```
Step 1: Add 5 + 6 = 11 → digit = 1, carry = 1
Step 2: Add 1 + 0 + carry(1) = 2 → digit = 2, carry = 0  
Step 3: Add 2 + 8 = 10 → digit = 0, carry = 1
Step 4: Only carry remains → digit = 1
Result (reversed): [1,0,2,1]
```

This method is optimal for the given constraints and ensures we don't run into integer overflow issues with large arrays.
