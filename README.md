# Boyer–Moore Majority Vote Algorithm

## 📌 Overview
The **Boyer–Moore Majority Vote Algorithm** is a simple yet powerful method to find a *dominant candidate* in a sequence.  
It works by progressively **cancelling out minority elements** and keeping track of a single candidate with a counter.

---

## 🔎 Principle
- Instead of counting occurrences of every element, the algorithm maintains:
  - **Candidate** → the current element suspected to be dominant.
  - **Counter** → a balance that increases when the candidate is confirmed, decreases when it is challenged.
- When the counter reaches zero, the algorithm switches to a new candidate.

This cancellation process ensures that if a majority element exists (appearing more than `n/2` times), it will remain as the final candidate.

---

## ⚙️ Procedure
1. **Initialization**
   - Candidate = None
   - Counter = 0

2. **Iterate through the sequence**
   - If Counter = 0 → set current element as new Candidate.
   - If current element == Candidate → increment Counter.
   - Else → decrement Counter.

3. **Result**
   - At the end, Candidate is the element that survived all cancellations.
   - A second pass may be required to verify that it truly is the majority.

---

## 📊 Example
Sequence: `[A, B, A, A, C, A, B, A]`

- Start: Candidate=None, Counter=0  
- `A` → Candidate=A, Counter=1  
- `B` → Counter=0  
- `A` → Candidate=A, Counter=1  
- `A` → Counter=2  
- `C` → Counter=1  
- `A` → Counter=2  
- `B` → Counter=1  
- `A` → Counter=2  

Final Candidate = **A**

---

## ⚖️ Complexity
- **Time**: `O(n)` (single pass through the sequence).
- **Space**: `O(1)` (only two variables needed).

---

## 📌 General Use
- Works on any sequence (numbers, characters, events).
- Useful in streaming or large datasets where memory efficiency is critical.
- Extended versions exist (e.g., finding elements appearing more than `n/3` times) by tracking multiple candidates.

---

## ✅ Summary
The **[Boyer–Moore Majority Vote Algorithm](ca://s?q=Boyer_Moore_majority_vote_algorithm)** is a cancellation-based method that efficiently identifies a dominant candidate in a sequence, using linear time and constant space.

---
---

# 🧠 Notes to Remember: set & dict Fundamentals

> Personal notes from working through the "Contains Duplicate" problem — set vs dict vs list approaches.

## Empty set vs empty dict
```python
s = set()   # ✅ empty set
s = {}      # ❌ this is an empty DICT, not a set!
d = {}      # ✅ empty dict
```
`{}` **always** means dict. There is no empty-set literal in Python.

## Why `in` is fast on set/dict but slow on list
| Structure | `x in s` | Reason |
|---|---|---|
| `list` | O(n) | must scan element by element |
| `set` | O(1) avg | hash table — jumps straight to the bucket |
| `dict` (keys) | O(1) avg | same hash table mechanism as set |

**Rule of thumb:** if you find yourself writing `if x in some_list:` inside a loop → that's a red flag for O(n²). Swap the list for a set/dict to get O(n).

## Contains Duplicate — 3 approaches compared
```python
# 1. Set-based (best fit for this exact problem)
def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# 2. Dict-based (useful when you also need extra info, e.g. index)
def containsNearbyDuplicate(nums, k):
    seen = {}  # num -> last index seen
    for i, num in enumerate(nums):
        if num in seen and i - seen[num] <= k:
            return True
        seen[num] = i
    return False

# 3. List-based (avoid — O(n²))
def containsDuplicate_slow(nums):
    seen = []
    for num in nums:
        if num in seen:   # O(n) scan every time!
            return True
        seen.append(num)
    return False
```

| Approach | Time | Space | When to use |
|---|---|---|---|
| set | O(n) | O(n) | Just need "have I seen this?" |
| dict | O(n) | O(n) | Need extra info per element (index, count...) |
| list | O(n²) | O(n) | Avoid — only if n is tiny |

## Space complexity = "extra memory beyond the input"
Building `seen`/`s`/`map` is **auxiliary space** — memory used *in addition to* the input array. This is the classic **time–space tradeoff**: spend O(n) extra memory to turn O(n²) time into O(n).

## The counting idiom — memorize this
```python
counts[num] = counts.get(num, 0) + 1
```
- `.get(key, default)` never raises `KeyError` — returns `default` if the key is missing.
- Equivalent to:
  ```python
  if num in counts:
      counts[num] += 1
  else:
      counts[num] = 1
  ```
- Shortcut version: `from collections import Counter; counts = Counter(nums)`

⚠️ **Bug to avoid**: check the count *after* incrementing, not before:
```python
# ❌ WRONG — checks before incrementing, misses duplicates that appear exactly twice
if num in map and map[num] > 1:
    return True
map[num] = map.get(num, 0) + 1

# ✅ CORRECT — increment first, then check
counts[num] = counts.get(num, 0) + 1
if counts[num] > 1:
    return True
```

## Hashability — required for set elements & dict keys
| Type | Hashable? |
|---|---|
| int, float, str, tuple* | ✅ |
| frozenset | ✅ |
| list, dict, set | ❌ (mutable) |

*tuple is hashable only if everything inside it is also hashable.

## set vs frozenset
| | set | frozenset |
|---|---|---|
| Mutable | Yes | No |
| Hashable | No | Yes |
| Can be a dict key / set element | No | Yes |



## Quick reference: when to reach for what
- **"Have I seen this?"** → `set`
- **"Have I seen this, and what was it associated with?"** → `dict`
- **Order matters, duplicates allowed, index access** → `list`
- **Fixed collection that itself needs to be hashable** → `frozenset`

## For anagram problem , the intuition is to trasnnfrom each string into a set then comapre but :
- Comparing two sets (s1 == s2) costs O(min(len(s1), len(s2))) on average — and the "how" is a nice mix of quick short-circuits plus hashing.

