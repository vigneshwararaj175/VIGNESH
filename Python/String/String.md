### 1 ) https://leetcode.com/problems/defanging-an-ip-address/
![[Pasted image 20250831071837.png]]

```python
class Solution:

    def defangIPaddr(self, address: str) -> str:

        return address.replace('.', '[.]')
```

---
### 2 ) https://leetcode.com/problems/shuffle-string/

![[Pasted image 20250831175541.png]]
![[Pasted image 20250831175617.png]]

```python
class Solution:

    def restoreString(self, s: str, indices: List[int]) -> str:

        shuffled = [''] * len(s)

        for i, char in enumerate(s):

            shuffled[indices[i]] = char

        return ''.join(shuffled)
```
-----
### 3 ) https://leetcode.com/problems/goal-parser-interpretation/description/
![[Pasted image 20250831181055.png]]

```python
class Solution:

    def interpret(self, command: str) -> str:

        command = command.replace("()","o")

        command = command.replace("(al)","al")

        return command
```
-------
### 4 ) https://leetcode.com/problems/longest-common-prefix/description/?envType=problem-list-v2&envId=string
![[Pasted image 20250831181255.png]]

```python
class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:

        res = ""

        for i in range(len(strs[0])):

            for s in strs:

                if i == len(s) or s[i] != strs[0][i]:

                    return res

            res += strs[0][i]

        return res
```
--------
### 5 ) https://leetcode.com/problems/count-items-matching-a-rule/description/
![[Pasted image 20250831181831.png]]

```python
class Solution:

    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:

        key_map = {"type": 0, "color": 1, "name": 2}

        index = key_map[ruleKey]

        count = 0

  

        for item in items:

            if item[index] == ruleValue:

                count += 1

        return count
```

```python
class Solution:

    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:

        if ruleKey =="type":

            index = 0

        elif ruleKey == "color":

            index = 1

        elif ruleKey == "name":

            index = 2

        count = 0

        for item in items:

            if item[index] == ruleValue:

                count += 1

        return count
```

-----
### 6 ) https://leetcode.com/problems/sorting-the-sentence/
![[Pasted image 20250903180600.png]]

```python
class Solution:

    def sortSentence(self, s: str) -> str:

        words = s.split()

        ans = [None]*len(words)

        for w in words:

            position = int(w[-1]) - 1

            ans[position] = w[:-1]

        return " ".join(ans)
```
-------
### 7 ) https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/submissions/1758195081/
![[Pasted image 20250903181113.png]]

```python
class Solution:

    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:

        ans1 = ""

        ans2 = ""

        for i in word1:

            ans1 += i

        for j in word2:

            ans2 += j

        if ans1 == ans2:

            return True

        else:

            return False
```
------
### 8 ) https://leetcode.com/problems/to-lower-case/description/
![[Pasted image 20250903181307.png]]
```python
class Solution:

    def toLowerCase(self, s: str) -> str:

        return s.lower()
```
-------
### 9 ) https://leetcode.com/problems/determine-if-string-halves-are-alike/description/

![[Pasted image 20251010065511.png]]

```python
class Solution:

    def halvesAreAlike(self, s: str) -> bool:

        def count_vowels(string):

            vowels = set('aeiouAEIOU')

            count = 0

            for char in string:

                if char in vowels:

                    count += 1

            return count

  

        mid = len(s)//2

        first_half = s[:mid]

        second_half = s[mid:]

  

        return count_vowels(first_half) == count_vowels(second_half)
```

----
### 10 https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/submissions/1798918720/
![[Pasted image 20251012084628.png]]

```python
class Solution:

    def freqAlphabets(self, s: str) -> str:

        result = []

        i = len(s)-1

  

        while i >= 0:

            if s[i] == '#':

                num = int(s[i-2:i])

                result.append(chr(num + 96))

                i -= 3

            else:

                num = int(s[i])

                result.append(chr(num +96))

                i -= 1

        return ''.join(result[::-1])
```
------
# 11 https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/description/
![[Pasted image 20251012085337.png]]

```python
class Solution:

    def numOfStrings(self, patterns: List[str], word: str) -> int:

        count = 0

        for pattern in patterns:

            if pattern in word:

                count += 1

        return count
```

Another answer using list comprehension

```python
class Solution:

    def numOfStrings(self, patterns: List[str], word: str) -> int:

        return sum(pattern in word for pattern in patterns)
```

Another answer using list comprehension

```python
class Solution:

    def numOfStrings(self, patterns: List[str], word: str) -> int:

        return sum(1 for pattern in patterns if pattern in word)
```

## Version 1: Using Generator Expression with `sum(1 for...)`

```python
def numOfStrings(patterns, word):
    return sum(1 for pattern in patterns if pattern in word)
```
**Breakdown:**

1. **`for pattern in patterns`**: Iterates through each string in the `patterns` list
    
2. **`if pattern in word`**: Checks if the current pattern exists as a substring in `word`
    
3. **`1 for pattern in patterns if pattern in word`**: Creates a generator that yields `1` for each pattern that is a substring of `word`
    
4. **`sum(...)`**: Adds up all the `1`s, effectively counting how many patterns are substrings
    

**Example with `patterns = ["a","abc","bc","d"]`, `word = "abc"`:**

- `"a" in "abc"` → True → yield 1
    
- `"abc" in "abc"` → True → yield 1
    
- `"bc" in "abc"` → True → yield 1
    
- `"d" in "abc"` → False → skip
    
- Sum = 1 + 1 + 1 = 3
    

## Version 2: Using Boolean Summation

```python
def numOfStrings_v2(patterns, word):
    return sum(pattern in word for pattern in patterns)
```
**Breakdown:**

1. **`pattern in word for pattern in patterns`**: Creates a generator of boolean values (`True`/`False`)
    
2. **`sum(...)`**: In Python, `True` equals `1` and `False` equals `0`, so summing booleans counts the `True` values
    

**Example with same input:**

- `"a" in "abc"` → True → 1
    
- `"abc" in "abc"` → True → 1
    
- `"bc" in "abc"` → True → 1
    
- `"d" in "abc"` → False → 0
    
- Sum = 1 + 1 + 1 + 0 = 3
    

## Key Python Concepts:

### 1. **Generator Expressions**

- `(expression for item in iterable if condition)`
    
- Lazy evaluation - generates values on the fly
    
- Memory efficient for large datasets
    
### 2. **Boolean Arithmetic**

```python
print(True + True)   # 2
print(True + False)  # 1  
print(False + False) # 0
```
### 3. **`in` Operator with Strings**

- Checks if a string contains another string as substring
    
- Returns `True`/`False`
    
- Case-sensitive

----------
# 12 https://leetcode.com/problems/robot-return-to-origin/
![[Pasted image 20251012091108.png]]

```python
class Solution:

    def judgeCircle(self, moves: str) -> bool:

        x,y = 0, 0

        for move in moves:

            if move == 'U':

                x += 1

            if move == 'D':

                x -= 1

            if move == 'R':

                y += 1

            if move == 'L':

                y -= 1

        return x == 0 and y == 0
```

```python
class Solution:

    def judgeCircle(self, moves: str) -> bool:

        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')
```

-----
# 13 https://leetcode.com/problems/reverse-words-in-a-string-iii/

![[Pasted image 20251012091717.png]]
```python
class Solution:

    def reverseWords(self, s: str) -> str:

        words = s.split()

        reversed_word = [word[::-1] for word in words]

        return ' '.join(reversed_word)
```

```python
class Solution:

    def reverseWords(self, s: str) -> str:

        return ' '.join(word[::-1] for word in s.split())
```

--------
# 14 https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/


![[Pasted image 20251012103055.png]]

```python
class Solution:

    def strStr(self, haystack: str, needle: str) -> int:

        if not needle:

            return 0

        n, m = len(haystack), len(needle)

        for i in range (n - m + 1):

            if haystack[i : i + m] == needle:

                return i

        return -1
```

```python
class Solution:

    def strStr(self, haystack: str, needle: str) -> int:

        return haystack.find(needle)
```
