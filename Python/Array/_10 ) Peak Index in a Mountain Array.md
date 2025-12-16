<img width="951" height="662" alt="image" src="https://github.com/user-attachments/assets/2a7eee26-796f-4e78-92b0-4a72e8a7548f" />


This is a **peak finding** problem in a mountain (bitonic) array.  

We know the array increases to a peak and then decreases, with no plateaus (strictly increase then strictly decrease).  
We need to find the **peak index** in **O(log n)** time.

---

## Step 1 — Understanding the mountain property

In a mountain array:
- For `i < peak`, `arr[i] < arr[i+1]`
- For `i > peak`, `arr[i] > arr[i+1]` is false (actually decreases)
- The peak is the maximum element.

We can use binary search to find where the increasing trend stops.

---

## Step 2 — Binary search idea

Compare `arr[mid]` and `arr[mid+1]`:
- If `arr[mid] < arr[mid+1]` → we are on the **ascending** slope, so peak is to the **right** → move `left = mid + 1`.
- If `arr[mid] > arr[mid+1]` → we are on the **descending** slope, so peak is at `mid` or to the **left** → move `right = mid`.

We stop when `left == right`.

---

## Step 3 — Why this works

Because the array is strictly increasing then strictly decreasing, there is exactly one peak.  
The condition `arr[mid] < arr[mid+1]` tells us if `mid` is before the peak.

---

## Step 4 — Example walkthrough

**Example:** `arr = [0, 2, 1, 0]`

left=0, right=3  
mid=1 → arr[1]=2, arr[2]=1 → 2 > 1 → right=1  
mid=0 → arr[0]=0, arr[1]=2 → 0 < 2 → left=1  
left=1, right=1 → stop → peak index=1 ✅

---

**Example:** `arr = [0, 10, 5, 2]`

left=0, right=3  
mid=1 → arr[1]=10, arr[2]=5 → 10 > 5 → right=1  
mid=0 → arr[0]=0, arr[1]=10 → 0 < 10 → left=1  
left=1, right=1 → stop → peak index=1 ✅

---

## Step 5 — Implementation

```python
def peakIndexInMountainArray(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid + 1]:
            # ascending part
            left = mid + 1
        else:
            # descending part
            right = mid
    return left
```

---

## Step 6 — Complexity
- **Time:** O(log n) — binary search.
- **Space:** O(1).

---

\[
\boxed{\text{binary search comparing arr[mid] and arr[mid+1]}}
\]
