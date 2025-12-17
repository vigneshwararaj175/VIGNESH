### 1)
```python
animals = ['lion','tiger','monkey','elephant','frog']
filtered_animal = [animal.title() for animal in animals]
print(filtered_animal)
```
---
### 2 )
```python
values = []
for x in range(10):
    values.append(x)
print(values)

#    OR
#   BOTH ARE SAME

values = [value for value in range(10)]
print(values)
```
OP
```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```
-------
### 3 )
```python
values = [value + 1 for value in range(10)]
print(values)
```
OP
```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```
------
### 4 ) 
```python
evens = []
for number in range(50):
    is_even = number % 2 == 0
    if is_even:
        evens.append(number)
```
OP
```
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
```

```python
evens = [number for number in range(50) if number % 2 == 0]
print(evens)
```
OP
```
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
```

------
### 5 )
```python
options = ["any","albany","apple","world","hello",""]
valid_strings = []

for string in options:
    if len(string)<= 1:
        continue
    if string[0] != "a":
        continue
    if string[-1] != "y":
        continue
    valid_strings.append(string)
print(valid_strings)
```
OP
```
['any', 'albany']
```

```python
options = ["any","albany","apple","world","hello",""]
valid_strings = [
    string
    for string in options
    if len(string) >= 2
    if string[0] == "a"
    if string[-1] == "y"
]
print(valid_strings)
```
OP
```
['any', 'albany']
```

-----
### 6 ) Multiple List Comprehension

```python
matrix = [[1,2,3],[4,5,6],[7,8,9]]
flattened = []
for row in matrix:
    for num in row:
        flattened.append(num)
print(flattened)        
```
OP
```
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

```python
matrix = [[1,2,3],[4,5,6],[7,8,9]]
flattened = [num for row in matrix for num in row]
print(flattened)
```
OP
```
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```
----
### 7 ) If-else Comprehension

```python
categories = []  
for number in range(10):  
    if number % 2 == 0:  
        categories.append("Even")  
    else:  
        categories.append("Odd")  
print(categories)
```
OP
```
['Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd']
```

```python
categories = [
    "Even" if number % 2 == 0 else "Odd" for number in range(10)
    ]
print(categories)
```
OP
```
['Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd']
```

---
### 8 ) Nested

```python
lst = []
for a in range(5):
    l1 = []
    for b in range(5):
        l2 = []
        for num in range(5):
            l2.append(num)
        l1.append(l2)
    lst.append(l1)
print(lst)    
```
OP
```python
[[[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]], [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]], [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]], [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]], [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]]
```

```python
lst = [[[num for num in range(5)] for _ in range(5)] for _ in range(5)]
print(lst)
```
OP
```
[[[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]], [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]], [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]], [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]], [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]]
```

----
### 9 ) Transformation Comprehension

```python
def square(x):
    return x**2
squared_numbers = [square(x) for x in range(10)]
print(squared_numbers)
```

```python
squared_numbers = [x**2 for x in range(10)]
print(squared_numbers)
```
OP
```
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

-----
### 10 ) Dictionary Comprehension

```python
pairs = [("a",1),("b",2),("c",3)]
my_dict = {k:v for k,v in pairs}
print(my_dict)
```
OP
```
{'a': 1, 'b': 2, 'c': 3}
```

```python
def square(x):
    return x**2
    
pairs = [("a",1),("b",2),("c",3)]
my_dict = {k:square(v) for k,v in pairs}
print(my_dict)
```
OP
```
{'a': 1, 'b': 4, 'c': 9}
```

-----
### 11 ) set comprehension

```python
# remove duplicate elements
nums = [1,2,2,3,3,3,4,4,4,4]
unique_square = {x**2 for x in nums}
print(unique_square)
```
OP
```
{16, 1, 4, 9}
```

----
### 12 ) Generator Comprehension

```python
sum_of_squares = sum(x**2 for x in range(1000000))
print(sum_of_squares)
```
OP
```
333332833333500000
```

```python
sum_of_squares = sum([x**2 for x in range(1000000)])
print(sum_of_squares)
```
OP
```
333332833333500000
```

--------
