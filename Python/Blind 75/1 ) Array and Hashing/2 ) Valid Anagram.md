https://neetcode.io/problems/is-anagram/question

### Sorting Method

Intuition
If two strings are anagrams, they must contain exactly the same characters with the same frequencies.
By sorting both strings, all characters will be arranged in a consistent order.
If the two sorted strings are identical, then every character and its count match, which means the strings are anagrams.

Algorithm
If the lengths of the two strings differ, return False immediately because they cannot be anagrams.
Sort both strings.
Compare the sorted versions of the strings:
If they are equal, return True.
Otherwise, return False.

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
```

### 2. Hash Map
Intuition
If two strings are anagrams, they must use the same characters with the same frequencies.
Instead of sorting, we can count how many times each character appears in both strings.
By using two hash maps (or dictionaries), we track the frequency of every character in each string.
If both frequency maps match exactly, then the strings contain the same characters with same frequencies, meaning they are anagrams.

Algorithm
If the two strings have different lengths, return False immediately.
Create two hash maps to store character frequencies for each string.
Iterate through both strings at the same time:
Increase the character count for s[i] in the first map.
Increase the character count for t[i] in the second map.
After building both maps, compare them:
If the maps are equal, return True.
Otherwise, return False.


```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
```
### 3. Hash Table (Using Array)
Intuition
Since the problem guarantees lowercase English letters, we can use a fixed-size array of length 26 to count character frequencies instead of a hash map.
As we iterate through both strings simultaneously, we increment the count for each character in s and decrement the count for each character in t.
If the strings are anagrams, every increment will be matched by a corresponding decrement, and all values in the array will end at zero.
This approach is efficient because it avoids hashing and uses constant space.

Algorithm
If the lengths of the strings differ, return False immediately.
Create a frequency array count of size 26 initialized to zero.
Iterate through both strings:
Increment the count at the index corresponding to s[i].
Decrement the count at the index corresponding to t[i].
After processing both strings, scan through the count array:
If any value is not zero, return False because the frequencies differ.
If all values are zero, return True since the strings are anagrams.

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True
```
