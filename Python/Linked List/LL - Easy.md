# 1)

## Solution 1: Mathematical Approach

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

	def getDecimalValue(head):
    """
    Convert a binary linked list to decimal value.
    
    Args:
        head: ListNode - head of the linked list
    
    Returns:
        int - decimal value of the binary number
    """
	    decimal_value = 0
	    current = head
    
    # Traverse the linked list
	    while current:
        # Left shift and add current bit
	        decimal_value = (decimal_value << 1) | current.val
	        current = current.next
    
	    return decimal_value
```

## Solution 2: String Conversion Approach

```python
def getDecimalValue_string(head):
    """
    Alternative approach using string conversion.
    """
    binary_str = ""
    current = head
    
    # Build binary string
    while current:
        binary_str += str(current.val)
        current = current.next
    
    # Convert binary string to decimal
    return int(binary_str, 2)
```

## Solution 3: Power of Two Approach

```python
def getDecimalValue_power(head):
    """
    Alternative approach using powers of 2.
    """
    # First, find the length of the linked list
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    
    # Calculate decimal value
    decimal_value = 0
    current = head
    power = length - 1
    
    while current:
        decimal_value += current.val * (2 ** power)
        power -= 1
        current = current.next
    
    return decimal_value
```

## Complete Example with Test Cases

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getDecimalValue(head):
    """
    Most efficient solution using bit manipulation.
    """
    decimal_value = 0
    current = head
    
    while current:
        decimal_value = (decimal_value << 1) | current.val
        current = current.next
    
    return decimal_value

def create_linked_list(arr):
    """Helper function to create linked list from array"""
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

# Test cases
def test_solution():
    # Test Case 1: [1,0,1] -> 5
    head1 = create_linked_list([1, 0, 1])
    result1 = getDecimalValue(head1)
    print(f"Input: [1,0,1] -> Output: {result1} (Expected: 5)")
    
    # Test Case 2: [0] -> 0
    head2 = create_linked_list([0])
    result2 = getDecimalValue(head2)
    print(f"Input: [0] -> Output: {result2} (Expected: 0)")
    
    # Test Case 3: [1,1,0,1] -> 13
    head3 = create_linked_list([1, 1, 0, 1])
    result3 = getDecimalValue(head3)
    print(f"Input: [1,1,0,1] -> Output: {result3} (Expected: 13)")
    
    # Test Case 4: [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0] -> 18880
    head4 = create_linked_list([1,0,0,1,0,0,1,1,1,0,0,0,0,0,0])
    result4 = getDecimalValue(head4)
    print(f"Input: [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0] -> Output: {result4} (Expected: 18880)")

# Run tests
if __name__ == "__main__":
    test_solution()
```

## Output:
```
Input: [1,0,1] -> Output: 5 (Expected: 5)
Input: [0] -> Output: 0 (Expected: 0)
Input: [1,1,0,1] -> Output: 13 (Expected: 13)
Input: [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0] -> Output: 18880 (Expected: 18880)
```

## Time and Space Complexity Analysis

**Solution 1 (Bit Manipulation):**
- **Time Complexity:** O(n) where n is the number of nodes
- **Space Complexity:** O(1)

**Solution 2 (String Conversion):**
- **Time Complexity:** O(n)
- **Space Complexity:** O(n) for the string

**Solution 3 (Power of Two):**
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

## Key Points:

1. **Most Significant Bit at Head:** The linked list represents the binary number with MSB at the head, so we process from left to right.

2. **Bit Manipulation Approach:** The most efficient solution uses `(decimal_value << 1) | current.val` which:
   - Left shifts the current value (multiplies by 2)
   - ORs with the current bit to add it

3. **Alternative Approaches:** The other solutions provide different ways to solve the same problem, which might be easier to understand for beginners.

The **bit manipulation approach (Solution 1)** is recommended as it's the most efficient in terms of both time and space complexity.


---------
# 2)

Here's a Python program to reverse a singly linked list:

## Solution 1: Iterative Approach (Most Efficient)

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    """
    Reverse a singly linked list iteratively.
    
    Args:
        head: ListNode - head of the linked list
    
    Returns:
        ListNode - head of the reversed linked list
    """
    prev = None
    current = head
    
    while current:
        # Store next node before breaking the link
        next_temp = current.next
        # Reverse the link
        current.next = prev
        # Move pointers forward
        prev = current
        current = next_temp
    
    return prev  # prev becomes the new head
```

## Solution 2: Recursive Approach

```python
def reverseList_recursive(head):
    """
    Reverse a singly linked list recursively.
    """
    # Base case: empty list or single node
    if not head or not head.next:
        return head
    
    # Reverse the rest of the list
    new_head = reverseList_recursive(head.next)
    
    # Reverse the current connection
    head.next.next = head
    head.next = None
    
    return new_head
```

## Solution 3: Using Stack

```python
def reverseList_stack(head):
    """
    Reverse a singly linked list using a stack.
    """
    if not head:
        return None
    
    stack = []
    current = head
    
    # Push all nodes to stack
    while current:
        stack.append(current)
        current = current.next
    
    # Pop from stack to create reversed list
    new_head = stack.pop()
    current = new_head
    
    while stack:
        current.next = stack.pop()
        current = current.next
    
    current.next = None  # Important: set last node's next to None
    return new_head
```

## Complete Example with Test Cases

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    """
    Iterative solution - most efficient.
    """
    prev = None
    current = head
    
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    
    return prev

def create_linked_list(arr):
    """Helper function to create linked list from array"""
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

def linked_list_to_list(head):
    """Helper function to convert linked list to Python list"""
    result = []
    current = head
    
    while current:
        result.append(current.val)
        current = current.next
    
    return result

def test_reverse_list():
    """Test function for reverse list implementation"""
    
    # Test Case 1: [1,2,3,4,5] -> [5,4,3,2,1]
    head1 = create_linked_list([1, 2, 3, 4, 5])
    reversed1 = reverseList(head1)
    result1 = linked_list_to_list(reversed1)
    print(f"Input: [1,2,3,4,5] -> Output: {result1} (Expected: [5,4,3,2,1])")
    
    # Test Case 2: [1,2] -> [2,1]
    head2 = create_linked_list([1, 2])
    reversed2 = reverseList(head2)
    result2 = linked_list_to_list(reversed2)
    print(f"Input: [1,2] -> Output: {result2} (Expected: [2,1])")
    
    # Test Case 3: [] -> []
    head3 = create_linked_list([])
    reversed3 = reverseList(head3)
    result3 = linked_list_to_list(reversed3)
    print(f"Input: [] -> Output: {result3} (Expected: [])")
    
    # Test Case 4: Single node
    head4 = create_linked_list([5])
    reversed4 = reverseList(head4)
    result4 = linked_list_to_list(reversed4)
    print(f"Input: [5] -> Output: {result4} (Expected: [5])")

# Visual demonstration of the iterative process
def demonstrate_reverse():
    """Demonstrate the step-by-step reversal process"""
    print("\n--- Step-by-Step Reversal Demonstration ---")
    head = create_linked_list([1, 2, 3])
    print(f"Original list: {linked_list_to_list(head)}")
    
    # Step 1
    prev = None
    current = head
    print(f"Initial: prev=None, current=1")
    
    steps = 1
    while current:
        next_temp = current.next
        current.next = prev
        print(f"Step {steps}: Reverse link - {current.val} -> {prev.val if prev else 'None'}")
        prev = current
        current = next_temp
        steps += 1
        if current:
            print(f"         Move: prev={prev.val}, current={current.val}")
        else:
            print(f"         Move: prev={prev.val}, current=None")
    
    print(f"Final reversed list: {linked_list_to_list(prev)}")

# Run tests and demonstration
if __name__ == "__main__":
    test_reverse_list()
    demonstrate_reverse()
```

## Output:
```
Input: [1,2,3,4,5] -> Output: [5,4,3,2,1] (Expected: [5,4,3,2,1])
Input: [1,2] -> Output: [2,1] (Expected: [2,1])
Input: [] -> Output: [] (Expected: [])
Input: [5] -> Output: [5] (Expected: [5])

--- Step-by-Step Reversal Demonstration ---
Original list: [1, 2, 3]
Initial: prev=None, current=1
Step 1: Reverse link - 1 -> None
         Move: prev=1, current=2
Step 2: Reverse link - 2 -> 1
         Move: prev=2, current=3
Step 3: Reverse link - 3 -> 2
         Move: prev=3, current=None
Final reversed list: [3, 2, 1]
```

## Time and Space Complexity Analysis

**Solution 1 (Iterative):**
- **Time Complexity:** O(n) where n is the number of nodes
- **Space Complexity:** O(1)

**Solution 2 (Recursive):**
- **Time Complexity:** O(n)
- **Space Complexity:** O(n) due to recursion stack

**Solution 3 (Stack):**
- **Time Complexity:** O(n)
- **Space Complexity:** O(n) for the stack

## Key Points:

1. **Iterative Approach:** The most efficient solution that uses three pointers (prev, current, next_temp) to reverse links one by one.

2. **Visualizing the Process:**
   - Start with `prev = None`, `current = head`
   - For each node:
     - Store `next_temp = current.next`
     - Reverse: `current.next = prev`
     - Move: `prev = current`, `current = next_temp`

3. **Edge Cases:**
   - Empty list: return `None`
   - Single node: return the same node
   - Two nodes: simple swap

4. **Recursive Approach:** Elegant but uses extra stack space. The base case returns the last node as new head, and each recursive call reverses one link.

The **iterative approach (Solution 1)** is recommended for production code due to its constant space complexity and clarity.

-----------
# 3)

Here's a Python program to find the middle node of a singly linked list:

## Solution 1: Two Pointers (Tortoise and Hare) - Most Efficient

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head):
    """
    Find the middle node using two pointers (slow and fast).
    If two middle nodes, return the second one.
    
    Args:
        head: ListNode - head of the linked list
    
    Returns:
        ListNode - middle node of the linked list
    """
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next          # Move slow by 1
        fast = fast.next.next     # Move fast by 2
    
    return slow
```

## Solution 2: Count and Traverse

```python
def middleNode_count(head):
    """
    Find middle node by counting nodes first.
    """
    # Count total nodes
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    
    # Find middle position
    middle_pos = count // 2
    
    # Traverse to middle node
    current = head
    for _ in range(middle_pos):
        current = current.next
    
    return current
```

## Solution 3: Using Array/List

```python
def middleNode_array(head):
    """
    Find middle node using array storage.
    """
    nodes = []
    current = head
    
    # Store all nodes in array
    while current:
        nodes.append(current)
        current = current.next
    
    # Return middle node
    return nodes[len(nodes) // 2]
```

## Complete Example with Test Cases

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head):
    """
    Two pointers approach - most efficient.
    """
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

def create_linked_list(arr):
    """Helper function to create linked list from array"""
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

def linked_list_to_list(head):
    """Helper function to convert linked list to Python list"""
    result = []
    current = head
    
    while current:
        result.append(current.val)
        current = current.next
    
    return result

def test_middle_node():
    """Test function for middle node implementation"""
    
    # Test Case 1: [1,2,3,4,5] -> [3,4,5]
    head1 = create_linked_list([1, 2, 3, 4, 5])
    middle1 = middleNode(head1)
    result1 = linked_list_to_list(middle1)
    print(f"Input: [1,2,3,4,5] -> Output: {result1} (Expected: [3,4,5])")
    
    # Test Case 2: [1,2,3,4,5,6] -> [4,5,6]
    head2 = create_linked_list([1, 2, 3, 4, 5, 6])
    middle2 = middleNode(head2)
    result2 = linked_list_to_list(middle2)
    print(f"Input: [1,2,3,4,5,6] -> Output: {result2} (Expected: [4,5,6])")
    
    # Test Case 3: Single node
    head3 = create_linked_list([5])
    middle3 = middleNode(head3)
    result3 = linked_list_to_list(middle3)
    print(f"Input: [5] -> Output: {result3} (Expected: [5])")
    
    # Test Case 4: Two nodes
    head4 = create_linked_list([1, 2])
    middle4 = middleNode(head4)
    result4 = linked_list_to_list(middle4)
    print(f"Input: [1,2] -> Output: {result4} (Expected: [2])")
    
    # Test Case 5: Three nodes
    head5 = create_linked_list([1, 2, 3])
    middle5 = middleNode(head5)
    result5 = linked_list_to_list(middle5)
    print(f"Input: [1,2,3] -> Output: {result5} (Expected: [2,3])")

# Visual demonstration of two pointers approach
def demonstrate_two_pointers():
    """Demonstrate the step-by-step two pointers process"""
    print("\n--- Two Pointers Demonstration ---")
    
    # Odd length: [1,2,3,4,5]
    print("Odd length list: [1,2,3,4,5]")
    head = create_linked_list([1, 2, 3, 4, 5])
    slow = fast = head
    
    step = 1
    while fast and fast.next:
        print(f"Step {step}: slow at {slow.val}, fast at {fast.val}")
        slow = slow.next
        fast = fast.next.next
        step += 1
    
    print(f"Final: slow at {slow.val} (MIDDLE)")
    print(f"Remaining list from middle: {linked_list_to_list(slow)}")
    
    print("\n" + "="*50)
    
    # Even length: [1,2,3,4,5,6]
    print("Even length list: [1,2,3,4,5,6]")
    head = create_linked_list([1, 2, 3, 4, 5, 6])
    slow = fast = head
    
    step = 1
    while fast and fast.next:
        print(f"Step {step}: slow at {slow.val}, fast at {fast.val}")
        slow = slow.next
        fast = fast.next.next if fast.next else None
        step += 1
    
    print(f"Final: slow at {slow.val} (SECOND MIDDLE)")
    print(f"Remaining list from middle: {linked_list_to_list(slow)}")

# Run tests and demonstration
if __name__ == "__main__":
    test_middle_node()
    demonstrate_two_pointers()
```

## Output:
```
Input: [1,2,3,4,5] -> Output: [3,4,5] (Expected: [3,4,5])
Input: [1,2,3,4,5,6] -> Output: [4,5,6] (Expected: [4,5,6])
Input: [5] -> Output: [5] (Expected: [5])
Input: [1,2] -> Output: [2] (Expected: [2])
Input: [1,2,3] -> Output: [2,3] (Expected: [2,3])

--- Two Pointers Demonstration ---
Odd length list: [1,2,3,4,5]
Step 1: slow at 1, fast at 1
Step 2: slow at 2, fast at 3
Final: slow at 3 (MIDDLE)
Remaining list from middle: [3, 4, 5]

==================================================
Even length list: [1,2,3,4,5,6]
Step 1: slow at 1, fast at 1
Step 2: slow at 2, fast at 3
Step 3: slow at 3, fast at 5
Final: slow at 4 (SECOND MIDDLE)
Remaining list from middle: [4, 5, 6]
```

## Time and Space Complexity Analysis

**Solution 1 (Two Pointers):**
- **Time Complexity:** O(n) - one pass through the list
- **Space Complexity:** O(1)

**Solution 2 (Count and Traverse):**
- **Time Complexity:** O(n) - two passes through the list
- **Space Complexity:** O(1)

**Solution 3 (Array):**
- **Time Complexity:** O(n) - one pass
- **Space Complexity:** O(n) - stores all nodes in array

## Key Points:

1. **Two Pointers Approach (Tortoise and Hare):**
   - `slow` moves 1 step at a time
   - `fast` moves 2 steps at a time
   - When `fast` reaches the end, `slow` is at the middle

2. **Why it works:**
   - For odd length: `fast` reaches last node, `slow` at exact middle
   - For even length: `fast` becomes `None`, `slow` at second middle

3. **Edge Cases:**
   - Single node: return the same node
   - Two nodes: return second node
   - Empty list: return `None`

4. **Mathematical Insight:**
   - When `fast` moves twice as fast as `slow`, `slow` covers half the distance
   - This ensures `slow` reaches middle when `fast` reaches end

The **two pointers approach (Solution 1)** is recommended as it's the most efficient with O(n) time and O(1) space, requiring only one pass through the list.

----------
# 4)

Here's a Python program to merge two sorted linked lists:

## Solution 1: Iterative Approach (Most Efficient)

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    """
    Merge two sorted linked lists iteratively.
    
    Args:
        list1: ListNode - head of first sorted list
        list2: ListNode - head of second sorted list
    
    Returns:
        ListNode - head of merged sorted list
    """
    # Create a dummy node to simplify edge cases
    dummy = ListNode(0)
    current = dummy
    
    # Traverse both lists
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # Attach remaining nodes from either list
    current.next = list1 if list1 else list2
    
    return dummy.next
```

## Solution 2: Recursive Approach

```python
def mergeTwoLists_recursive(list1, list2):
    """
    Merge two sorted linked lists recursively.
    """
    # Base cases
    if not list1:
        return list2
    if not list2:
        return list1
    
    # Recursive case
    if list1.val <= list2.val:
        list1.next = mergeTwoLists_recursive(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoLists_recursive(list1, list2.next)
        return list2
```

## Solution 3: In-place Modification

```python
def mergeTwoLists_inplace(list1, list2):
    """
    Merge two sorted linked lists in-place.
    """
    if not list1:
        return list2
    if not list2:
        return list1
    
    # Determine which list becomes the main list
    if list1.val > list2.val:
        list1, list2 = list2, list1
    
    head = list1
    
    while list1 and list2:
        # Find the position to insert list2 nodes into list1
        while list1.next and list1.next.val <= list2.val:
            list1 = list1.next
        
        # Insert list2 node into list1
        temp1 = list1.next
        temp2 = list2.next
        
        list1.next = list2
        list2.next = temp1
        
        # Move pointers
        list1 = list2
        list2 = temp2
    
    return head
```

## Complete Example with Test Cases

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    """
    Iterative solution with dummy node - most efficient and readable.
    """
    dummy = ListNode(0)
    current = dummy
    
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # Attach remaining nodes
    current.next = list1 if list1 else list2
    
    return dummy.next

def create_linked_list(arr):
    """Helper function to create linked list from array"""
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

def linked_list_to_list(head):
    """Helper function to convert linked list to Python list"""
    result = []
    current = head
    
    while current:
        result.append(current.val)
        current = current.next
    
    return result

def test_merge_lists():
    """Test function for merge two lists implementation"""
    
    # Test Case 1: [1,2,4] and [1,3,4] -> [1,1,2,3,4,4]
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    merged = mergeTwoLists(list1, list2)
    result = linked_list_to_list(merged)
    print(f"Input: [1,2,4] + [1,3,4] -> Output: {result} (Expected: [1,1,2,3,4,4])")
    
    # Test Case 2: [] and [] -> []
    list1 = create_linked_list([])
    list2 = create_linked_list([])
    merged = mergeTwoLists(list1, list2)
    result = linked_list_to_list(merged)
    print(f"Input: [] + [] -> Output: {result} (Expected: [])")
    
    # Test Case 3: [] and [0] -> [0]
    list1 = create_linked_list([])
    list2 = create_linked_list([0])
    merged = mergeTwoLists(list1, list2)
    result = linked_list_to_list(merged)
    print(f"Input: [] + [0] -> Output: {result} (Expected: [0])")
    
    # Test Case 4: [5] and [1,2,3] -> [1,2,3,5]
    list1 = create_linked_list([5])
    list2 = create_linked_list([1, 2, 3])
    merged = mergeTwoLists(list1, list2)
    result = linked_list_to_list(merged)
    print(f"Input: [5] + [1,2,3] -> Output: {result} (Expected: [1,2,3,5])")
    
    # Test Case 5: [1,5] and [2,3,4] -> [1,2,3,4,5]
    list1 = create_linked_list([1, 5])
    list2 = create_linked_list([2, 3, 4])
    merged = mergeTwoLists(list1, list2)
    result = linked_list_to_list(merged)
    print(f"Input: [1,5] + [2,3,4] -> Output: {result} (Expected: [1,2,3,4,5])")

# Visual demonstration of the merging process
def demonstrate_merging():
    """Demonstrate the step-by-step merging process"""
    print("\n--- Step-by-Step Merging Demonstration ---")
    
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    
    print(f"List1: {linked_list_to_list(list1)}")
    print(f"List2: {linked_list_to_list(list2)}")
    
    dummy = ListNode(0)
    current = dummy
    step = 1
    
    l1, l2 = list1, list2
    
    while l1 and l2:
        print(f"\nStep {step}:")
        print(f"  Current merged list: {linked_list_to_list(dummy.next)}")
        print(f"  Comparing: list1={l1.val}, list2={l2.val}")
        
        if l1.val <= l2.val:
            print(f"  Choose list1 node: {l1.val}")
            current.next = l1
            l1 = l1.next
        else:
            print(f"  Choose list2 node: {l2.val}")
            current.next = l2
            l2 = l2.next
        
        current = current.next
        step += 1
    
    # Attach remaining nodes
    if l1:
        print(f"\nAttaching remaining list1: {linked_list_to_list(l1)}")
        current.next = l1
    elif l2:
        print(f"\nAttaching remaining list2: {linked_list_to_list(l2)}")
        current.next = l2
    
    print(f"\nFinal merged list: {linked_list_to_list(dummy.next)}")

# Run tests and demonstration
if __name__ == "__main__":
    test_merge_lists()
    demonstrate_merging()
```

## Output:
```
Input: [1,2,4] + [1,3,4] -> Output: [1,1,2,3,4,4] (Expected: [1,1,2,3,4,4])
Input: [] + [] -> Output: [] (Expected: [])
Input: [] + [0] -> Output: [0] (Expected: [0])
Input: [5] + [1,2,3] -> Output: [1,2,3,5] (Expected: [1,2,3,5])
Input: [1,5] + [2,3,4] -> Output: [1,2,3,4,5] (Expected: [1,2,3,4,5])

--- Step-by-Step Merging Demonstration ---
List1: [1, 2, 4]
List2: [1, 3, 4]

Step 1:
  Current merged list: []
  Comparing: list1=1, list2=1
  Choose list1 node: 1

Step 2:
  Current merged list: [1]
  Comparing: list1=2, list2=1
  Choose list2 node: 1

Step 3:
  Current merged list: [1, 1]
  Comparing: list1=2, list2=3
  Choose list1 node: 2

Step 4:
  Current merged list: [1, 1, 2]
  Comparing: list1=4, list2=3
  Choose list2 node: 3

Step 5:
  Current merged list: [1, 1, 2, 3]
  Comparing: list1=4, list2=4
  Choose list1 node: 4

Attaching remaining list2: [4]

Final merged list: [1, 1, 2, 3, 4, 4]
```

## Time and Space Complexity Analysis

**Solution 1 (Iterative with Dummy):**
- **Time Complexity:** O(n + m) where n and m are lengths of lists
- **Space Complexity:** O(1) - only uses constant extra space

**Solution 2 (Recursive):**
- **Time Complexity:** O(n + m)
- **Space Complexity:** O(n + m) due to recursion stack

**Solution 3 (In-place):**
- **Time Complexity:** O(n + m)
- **Space Complexity:** O(1)

## Key Points:

1. **Dummy Node Technique:** Using a dummy node simplifies handling edge cases and avoids special checks for the head.

2. **Comparison Logic:** Always compare the current nodes of both lists and choose the smaller one.

3. **Remaining Nodes:** When one list is exhausted, simply attach the remaining nodes of the other list.

4. **Edge Cases:**
   - One or both lists are empty
   - Lists of different lengths
   - All elements in one list are smaller/larger than the other

5. **Splicing Nodes:** The solution actually moves nodes from the original lists (as required), not creating new nodes.

The **iterative approach with dummy node (Solution 1)** is recommended as it's the most efficient, readable, and handles all edge cases gracefully.

--------
# 5 )

Here's a Python program to delete a node from a singly linked list when you only have access to that node:

## Solution: Node Value Replacement

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteNode(node):
    """
    Delete a node from a linked list when you only have access to that node.
    
    Args:
        node: ListNode - the node to be deleted (guaranteed not to be the last node)
    """
    # Copy the value from next node to current node
    node.val = node.next.val
    # Skip the next node
    node.next = node.next.next
```

## Complete Example with Test Cases

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteNode(node):
    """
    The key insight: we can't delete the current node directly since we don't have 
    access to the previous node. Instead, we copy the next node's value to the 
    current node and then skip the next node.
    """
    node.val = node.next.val
    node.next = node.next.next

def create_linked_list(arr):
    """Helper function to create linked list from array"""
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

def linked_list_to_list(head):
    """Helper function to convert linked list to Python list"""
    result = []
    current = head
    
    while current:
        result.append(current.val)
        current = current.next
    
    return result

def find_node(head, target_val):
    """Helper function to find a node with specific value"""
    current = head
    while current and current.val != target_val:
        current = current.next
    return current

def test_delete_node():
    """Test function for delete node implementation"""
    
    # Test Case 1: Delete node with value 5 from [4,5,1,9]
    head1 = create_linked_list([4, 5, 1, 9])
    node_to_delete1 = find_node(head1, 5)
    print(f"Before deletion: {linked_list_to_list(head1)}")
    deleteNode(node_to_delete1)
    result1 = linked_list_to_list(head1)
    print(f"After deleting 5: {result1} (Expected: [4,1,9])")
    
    print("-" * 50)
    
    # Test Case 2: Delete node with value 1 from [4,5,1,9]
    head2 = create_linked_list([4, 5, 1, 9])
    node_to_delete2 = find_node(head2, 1)
    print(f"Before deletion: {linked_list_to_list(head2)}")
    deleteNode(node_to_delete2)
    result2 = linked_list_to_list(head2)
    print(f"After deleting 1: {result2} (Expected: [4,5,9])")
    
    print("-" * 50)
    
    # Test Case 3: Delete from middle of longer list
    head3 = create_linked_list([1, 2, 3, 4, 5])
    node_to_delete3 = find_node(head3, 3)
    print(f"Before deletion: {linked_list_to_list(head3)}")
    deleteNode(node_to_delete3)
    result3 = linked_list_to_list(head3)
    print(f"After deleting 3: {result3} (Expected: [1,2,4,5])")

# Visual demonstration of the deletion process
def demonstrate_deletion():
    """Demonstrate the step-by-step deletion process"""
    print("\n--- Step-by-Step Deletion Demonstration ---")
    
    # Create list: 4 -> 5 -> 1 -> 9
    head = create_linked_list([4, 5, 1, 9])
    node_to_delete = find_node(head, 5)
    
    print(f"Original list: {linked_list_to_list(head)}")
    print(f"Node to delete: {node_to_delete.val}")
    print(f"Node to delete's next: {node_to_delete.next.val}")
    
    # Step 1: Copy next node's value
    print("\nStep 1: Copy next node's value to current node")
    print(f"Before: node.val = {node_to_delete.val}")
    node_to_delete.val = node_to_delete.next.val
    print(f"After: node.val = {node_to_delete.val}")
    print(f"List after step 1: {linked_list_to_list(head)}")
    
    # Step 2: Skip the next node
    print("\nStep 2: Skip the next node")
    print(f"Before: node.next points to node with value {node_to_delete.next.val}")
    node_to_delete.next = node_to_delete.next.next
    print(f"After: node.next points to node with value {node_to_delete.next.val if node_to_delete.next else 'None'}")
    print(f"Final list: {linked_list_to_list(head)}")

# Run tests and demonstration
if __name__ == "__main__":
    test_delete_node()
    demonstrate_deletion()
```

## Output:
```
Before deletion: [4, 5, 1, 9]
After deleting 5: [4, 1, 9] (Expected: [4,1,9])
--------------------------------------------------
Before deletion: [4, 5, 1, 9]
After deleting 1: [4, 5, 9] (Expected: [4,5,9])
--------------------------------------------------
Before deletion: [1, 2, 3, 4, 5]
After deleting 3: [1, 2, 4, 5] (Expected: [1,2,4,5])

--- Step-by-Step Deletion Demonstration ---
Original list: [4, 5, 1, 9]
Node to delete: 5
Node to delete's next: 1

Step 1: Copy next node's value to current node
Before: node.val = 5
After: node.val = 1
List after step 1: [4, 1, 1, 9]

Step 2: Skip the next node
Before: node.next points to node with value 1
After: node.next points to node with value 9
Final list: [4, 1, 9]
```

## Time and Space Complexity Analysis

**Time Complexity:** O(1) - Constant time operation
**Space Complexity:** O(1) - No extra space used

## Key Points:

1. **The Problem Constraint:** We don't have access to the head of the list, only the node to be deleted.

2. **The Clever Solution:** Since we can't modify the previous node's `next` pointer, we:
   - Copy the value from the next node to the current node
   - Skip the next node by pointing current node's `next` to the node after next

3. **Why This Works:**
   - The node is effectively "replaced" by the next node
   - The next node is then removed from the list
   - The order of nodes before and after is preserved

4. **Important Guarantees:**
   - The given node is **not the last node** (so `node.next` exists)
   - All values are unique
   - The node is an actual node in the list

5. **What Actually Happens in Memory:**
   - We're not actually deleting the given node from memory
   - We're repurposing it to hold the next node's value
   - The original next node becomes unreachable and will be garbage collected

## Alternative Perspective:

Think of it as "The node to delete becomes the next node, and we remove the original next node."

This approach is elegant and efficient, leveraging the constraints to find a simple solution.

-----------

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

	def getDecimalValue(head):
    """
    Convert a binary linked list to decimal value.
    
    Args:
        head: ListNode - head of the linked list
    
    Returns:
        int - decimal value of the binary number
    """
	    decimal_value = 0
	    current = head
    
    # Traverse the linked list
	    while current:
        # Left shift and add current bit
	        decimal_value = (decimal_value << 1) | current.val
	        current = current.next
    
	    return decimal_value
```

----------
# 6) https://leetcode.com/problems/palindrome-linked-list/
![[Pasted image 20251204044754.png]]

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head):
    if not head or not head.next:
        return True
    
    # Step 1: Find the middle of the linked list
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Step 2: Reverse the second half
    prev = None
    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp
    
    # Step 3: Compare the first half and the reversed second half
    left, right = head, prev
    while right:  # only need to compare with second half
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    
    return True
```

----------
# 7 ) https://leetcode.com/problems/intersection-of-two-linked-lists/
![[Pasted image 20251204045031.png]]
![[Pasted image 20251204045109.png]]
![[Pasted image 20251204045134.png]]
![[Pasted image 20251204045150.png]]

- If `pA` starts at `headA` and `pB` at `headB`, and they move one step at a time, they will reach the intersection node at the same time after switching heads, if an intersection exists.
    

**Reasoning**:  
Let length of `A` before intersection = `a`,  
length of `B` before intersection = `b`,  
length of common part after intersection = `c`.

If we traverse:

- Path of `pA`: `a + c + b`
    
- Path of `pB`: `b + c + a`
    

They will meet at the intersection point in the second pass if it exists, otherwise they will both become `null`.

---

**Algorithm**:

1. Initialize `pA = headA`, `pB = headB`.
    
2. Traverse both lists one step at a time.
    
3. When `pA` reaches the end of list A, redirect it to headB.
    
4. When `pB` reaches the end of list B, redirect it to headA.
    
5. Eventually, `pA` and `pB` will either meet at the intersection node or both become `null` (no intersection).

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getIntersectionNode(headA, headB):
    if not headA or not headB:
        return None
    
    pA, pB = headA, headB
    
    while pA != pB:
        # Move to next node; if at end, switch heads
        pA = pA.next if pA else headB
        pB = pB.next if pB else headA
    
    # Either both are None (no intersection) or both at intersection node
    return pA
```



------------
# 8 ) https://leetcode.com/problems/linked-list-cycle/description/
![[Pasted image 20251204045528.png]]
![[Pasted image 20251204045609.png]]

- Use two pointers: `slow` moves one step at a time, `fast` moves two steps at a time.
    
- If there’s a cycle, they will eventually meet.
    
- If `fast` reaches `None`, there’s no cycle.

```python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head):
    if not head or not head.next:
        return False
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False
```

------------
# 9 ) https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
![[Pasted image 20251204045810.png]]

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    current = head
    
    while current and current.next:
        if current.val == current.next.val:
            # Skip the duplicate node
            current.next = current.next.next
        else:
            # Move to the next node
            current = current.next
    
    return head
```

------------
# 10 ) https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
![[Pasted image 20251204050006.png]]

```python
def findDisappearedNumbers(nums):
    n = len(nums)
    
    # Step 1: Mark indices as visited
    for i in range(n):
        idx = abs(nums[i]) - 1
        if nums[idx] > 0:
            nums[idx] = -nums[idx]
    
    # Step 2: Collect indices that are still positive
    result = []
    for i in range(n):
        if nums[i] > 0:
            result.append(i + 1)
    
    return result
```

---------
# 11 ) https://leetcode.com/problems/remove-linked-list-elements/description/
![[Pasted image 20251204050140.png]]

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head, val):
    dummy = ListNode(0)
    dummy.next = head
    
    prev, curr = dummy, head
    
    while curr:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
    
    return dummy.next
```

-----

[[LL - Medium]]
