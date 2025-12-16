This is the classic **binary search** problem — we need to find either the exact position of `target` or the **insertion position** where it would maintain sorted order.  

---

## Step 1 — Understanding the output
We want `i` such that:
- If `target` is in `nums`, then `nums[i] == target`.
- If `target` is not in `nums`, then `nums[i-1] < target < nums[i]` (with boundary handling).

Equivalently: find the **smallest index `i`** where `nums[i] >= target`.  
If all elements are less than target, return `len(nums)`.

This is the **lower_bound** in C++ terms.

---

## Step 2 — Binary search setup
Let `left = 0`, `right = n` (where `n = len(nums)`).  
We search in `[left, right)` half-open interval.

Loop while `left < right`:
- `mid = (left + right) // 2`
- If `nums[mid] < target`, then target must be to the right → `left = mid + 1`
- Else (`nums[mid] >= target`), `mid` could be the answer, so move `right = mid`

After loop, `left` is the first index where `nums[left] >= target`, or `n` if none.

---

## Step 3 — Example walkthrough

**Example 1:**  
`nums = [1,3,5,6], target = 5`  
left=0, right=4  
mid=2: nums[2]=5 >= 5 → right=2  
mid=1: nums[1]=3 < 5 → left=2  
left=2, right=2 → stop → answer=2 ✅

**Example 2:**  
`nums = [1,3,5,6], target = 2`  
left=0, right=4  
mid=2: 5 >= 2 → right=2  
mid=1: 3 >= 2 → right=1  
mid=0: 1 < 2 → left=1  
left=1, right=1 → stop → answer=1 ✅

**Example 3:**  
`nums = [1,3,5,6], target = 7`  
Binary search:  
mid=2: 5<7 → left=3  
mid=3: 6<7 → left=4 → left=4, right=4 → stop → answer=4 ✅

---

## Step 4 — Implementation
```python
def searchInsert(nums, target):
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left
```

---

## Step 5 — Complexity
- **Time:** O(log n) because we halve the search space each iteration.
- **Space:** O(1).

---

