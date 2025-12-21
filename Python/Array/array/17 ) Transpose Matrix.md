```python
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        result = [[0] * row for _ in range(col)]
        for i in range(row):
            for j in range(col):
                result[j][i] = matrix[i][j]
        return result
```

---------

## **Understanding the Problem**
We need to flip a matrix over its main diagonal (top-left to bottom-right). This means:
- Rows become columns
- Columns become rows
- Element at `(i, j)` moves to `(j, i)`

## **Key Observations**
- For an `m x n` matrix, the transpose will be `n x m`
- Original dimensions: `rows = len(matrix)`, `cols = len(matrix[0])`
- Transpose dimensions: `rows = len(matrix[0])`, `cols = len(matrix)`

## **Solutions**

### **1. Basic Approach - Create New Matrix**
```python
def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Create result matrix with swapped dimensions
    result = [[0] * rows for _ in range(cols)]
    
    # Fill result[j][i] = matrix[i][j]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    
    return result
```

### **2. Pythonic One-Liner (Using zip)**
```python
def transpose(matrix):
    return list(zip(*matrix))
    
# If you need lists instead of tuples:
def transpose(matrix):
    return [list(row) for row in zip(*matrix)]
```

### **3. List Comprehension**
```python
def transpose(matrix):
    rows, cols = len(matrix), len(matrix[0])
    return [[matrix[i][j] for i in range(rows)] for j in range(cols)]
```

## **Time & Space Complexity**
- **Time Complexity**: O(m × n) where m = rows, n = columns
- **Space Complexity**: O(m × n) for the new matrix

## **Edge Cases**
1. **Empty matrix**: `[]`
2. **Single row**: `[[1, 2, 3]]`
3. **Single column**: `[[1], [2], [3]]`
4. **Square matrix** (special case where m = n)

## **Testing**
```python
# Test with provided examples
matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
print(transpose(matrix1))  # [[1,4,7],[2,5,8],[3,6,9]]

matrix2 = [[1,2,3],[4,5,6]]
print(transpose(matrix2))  # [[1,4],[2,5],[3,6]]

# Test edge cases
print(transpose([[1]]))  # [[1]]
print(transpose([[]]))   # []
```

## **In-Place Transpose (For Square Matrices Only)**
If the matrix is square (n × n), we can transpose in-place:
```python
def transpose_in_place(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):  # Only swap upper triangle
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix
```

## **Recommended Solution**
For most cases, the Pythonic `zip` solution is clean and efficient:
```python
def transpose(matrix):
    """Return transpose of matrix using zip."""
    return [list(row) for row in zip(*matrix)]
```

This solution:
1. Is concise and readable
2. Leverages Python's optimized `zip` function
3. Handles all edge cases correctly
4. Is efficient (zip is implemented in C)
