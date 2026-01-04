```python
class Solution:
    def removeDuplicates(self, nums):
        # If the array is empty, return 0.
        if len(nums) == 0:
            return 0

        # writePos marks where the next unique element should be placed.
        writePos = 0

        # readPos scans through the array to find unique elements.
        for readPos in range(1, len(nums)):
            # When a new unique element is found
            if nums[readPos] != nums[writePos]:
                writePos += 1                 # Move writePos forward
                nums[writePos] = nums[readPos]  # Place the unique element

        # Number of unique elements is writePos + 1
        return writePos + 1
```
