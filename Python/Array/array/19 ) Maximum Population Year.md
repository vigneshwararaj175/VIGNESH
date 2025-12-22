I'll help you solve this problem step by step in a beginner-friendly way.

## Understanding the Problem
We need to find the **earliest year** when the **population is maximum**.  
Each person is alive from their birth year up to (but not including) their death year.

---

## Thought Process

### Step 1: Restating in my own words
- We have people with birth and death years.
- A person is counted in year `x` if `birth ≤ x < death`.
- We need to find the year with the most people alive.
- If multiple years have the same max population, pick the earliest one.

---

### Step 2: Understanding the example
Example 2: `[[1950,1961],[1960,1971],[1970,1981]]`

- Person 1: alive 1950 to 1960 (since 1961 not included)
- Person 2: alive 1960 to 1970
- Person 3: alive 1970 to 1980

Let's count year by year:
- 1950–1959: only person 1 → population = 1
- 1960: person 1 + person 2 → population = 2
- 1961–1969: person 1 + person 2 → population = 2
- 1970: person 2 + person 3 → population = 2
- 1971–1979: only person 3 → population = 1

Max population = 2, earliest year = 1960.

---

### Step 3: Planning the approach
We can:
1. Check every possible year from the earliest birth to the latest death.
2. For each year, count how many people are alive.
3. Track the maximum population and the earliest year it occurs.

---

### Step 4: Implementation steps
1. Find the range of years we need to check (min birth to max death).
2. For each year in that range:
   - Count people whose birth ≤ year < death.
3. Track max population and earliest year.

---

### Step 5: Writing the code

```python
def maximumPopulation(logs):
    # Step 1: Find the range of years
    min_year = min(birth for birth, death in logs)
    max_year = max(death for birth, death in logs)
    
    max_population = 0
    earliest_year = min_year
    
    # Step 2: Check each year in the range
    for year in range(min_year, max_year + 1):
        count = 0
        for birth, death in logs:
            if birth <= year < death:
                count += 1
        
        # Step 3: Update if we found a larger population
        if count > max_population:
            max_population = count
            earliest_year = year
        # If same population but earlier year, we don't change because
        # we are checking years in increasing order anyway
    
    return earliest_year

# Test with examples
print(maximumPopulation([[1993,1999],[2000,2010]]))  # Output: 1993
print(maximumPopulation([[1950,1961],[1960,1971],[1970,1981]]))  # Output: 1960
```

---

### Step 6: Complexity
- **Time complexity:** O(N × Y) where N = number of people, Y = range of years.
- **Space complexity:** O(1) extra space.

Since constraints are small (people ≤ 100, years ≤ 100), this is fine.

---

### Step 7: Optimization idea (for learning)
We can optimize using the "line sweep" approach:
- Treat birth as +1 to population, death as -1.
- Sort events and sweep through them to find max population year.

But for a beginner, the brute force method is easiest to understand first.

---

## Alternative optimized solution (for reference)

```python
def maximumPopulation(logs):
    # Array to store population changes
    # Year range: 1950 to 2050
    delta = [0] * 101  # index 0 = year 1950, index 100 = year 2050
    
    for birth, death in logs:
        delta[birth - 1950] += 1
        delta[death - 1950] -= 1
    
    max_pop = 0
    curr_pop = 0
    earliest_year = 1950
    
    for i in range(101):
        curr_pop += delta[i]
        if curr_pop > max_pop:
            max_pop = curr_pop
            earliest_year = 1950 + i
    
    return earliest_year
```

This is faster: O(N + Y) time, O(Y) space.

---

**For a beginner**, stick with the brute force method first — it’s straightforward and works within the given constraints. Once comfortable, you can learn the optimized approach.
