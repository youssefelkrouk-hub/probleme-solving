# 🧠 DSA Notes: Algorithms, Data Structures & Complexity

> Personal working notes — algorithm patterns, complexity analysis, and gotchas collected while solving problems.

---

## Table of Contents
1. [Boyer–Moore Majority Vote Algorithm](#-boyermoore-majority-vote-algorithm)
2. [Notes to Remember: set & dict Fundamentals](#-notes-to-remember-set--dict-fundamentals)
3. [Sliding Window Technique: Longest Substring Without Repeating Characters](#-sliding-window-technique-longest-substring-without-repeating-characters)

---

# 📌 Boyer–Moore Majority Vote Algorithm

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
The **Boyer–Moore Majority Vote Algorithm** is a cancellation-based method that efficiently identifies a dominant candidate in a sequence, using linear time and constant space.

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

## For anagram problem, the intuition is to transform each string into a set then compare, but:
- Comparing two sets (`s1 == s2`) costs O(min(len(s1), len(s2))) on average — and the "how" is a nice mix of quick short-circuits plus hashing.

---
---

# 🪟 Sliding Window Technique: Longest Substring Without Repeating Characters

> Notes from working through **LeetCode 3 — Longest Substring Without Repeating Characters**, progressing from brute force to the optimal O(n) solution.

## The problem
Find the length of the longest **contiguous** substring of `s` with no repeated characters.
(A *substring* must be contiguous — unlike a *subsequence*, e.g. `"pwke"` from `"pwwkew"` doesn't count.)

## The four approaches, in order of improvement

### 1. Naive — rebuild a set for every substring
```python
def is_unique(sub):
    return len(sub) == len(set(sub))

def length_of_longest_substring_naive(s):
    max_len = 0
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            if is_unique(s[i:j+1]):
                max_len = max(max_len, j - i + 1)
    return max_len
```
- Two nested loops generate every possible substring → O(n²) substrings.
- `is_unique` slices the substring *and* builds a `set()` from scratch each time → O(n) extra work per check.
- **Time: O(n³)** · **Space: O(n)**

### 2. Nested loop, incremental `seen` set (reset per `i`)
```python
def bruteforce_substring_longest(s):
    max_len = 0
    n = len(s)
    for i in range(n):
        seen = set()
        for j in range(i, n):
            if s[j] in seen:
                break
            seen.add(s[j])
            max_len = max(max_len, j - i + 1)   # careful: j - i + 1, not i - j + 1!
    return max_len
```
- Improvement: `seen` is built incrementally as `j` grows (O(1) per step) instead of rebuilt from scratch.
- Still brute force: `seen` is thrown away and rebuilt every time `i` advances — no reuse of work *across* different starting points.
- ⚠️ **Common bug**: writing `i - j + 1` instead of `j - i + 1`. Since `j >= i` always, the swapped version is `<= 1` and silently breaks the result — always double-check operand order when computing a window length.
- **Time: O(n²)** · **Space: O(min(n, m))**

### 3. Optimal — sliding window with a `set` (two pointers)
```python
def Longest_substring_set(s):
    left, max_len = 0, 0
    seen = set()
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len
```
- Never resets: `left` and `right` each only ever move **forward**, across the *whole* string, not per outer iteration.
- The `while` (not `if`) matters — it may need to shrink the window by more than one step to fully clear the duplicate before continuing.
- **Time: O(n)** — `right` advances n times total; `left` advances at most n times total across the *entire* run (amortized, not per-iteration).
- **Space: O(min(n, m))** — `seen` can't hold more entries than characters in `s`, and can't hold more than `m`, the number of distinct possible characters in the alphabet.

### 4. Optimal — sliding window with a hash map (`char → last index`)
```python
def longest_substring_2(s):
    last_index = {}
    left, max_len = 0, 0
    for right, c in enumerate(s):
        if c in last_index and last_index[c] >= left:
            left = last_index[c] + 1
        last_index[c] = right
        max_len = max(max_len, right - left + 1)
    return max_len
```
- Instead of removing characters one-by-one with a `while` loop, jump `left` **directly** to `last_index[c] + 1` — an O(1) constant-factor improvement over version 3 (each character is processed once, never removed and re-added).
- `last_index` never shrinks — it keeps every character ever seen, even ones outside the current window. That's fine: a dict key can only exist once, so re-seeing a character just **overwrites** its value instead of growing the dict.
- The `last_index[c] >= left` check matters: without it, you might rewind `left` backward based on a stale index from *outside* the current window (classic bug with strings like `"dvdf"`).
- **Time: O(n)** · **Space: O(min(n, m))**

## Why space is `O(min(n, m))`, not just `O(n)`
The extra structure (`seen` set or `last_index` dict) holds **at most one entry per distinct character** currently tracked. Two things cap its size:
- **`n`** — it can never exceed the number of characters in `s`.
- **`m`** — the size of the character alphabet (e.g. 26 for lowercase letters, 128 for ASCII). Once every possible character is a key, further characters just **overwrite** existing entries rather than growing the structure.

So the true bound is *whichever of the two is smaller*:
- Short string vs. big alphabet → `n` is the binding constraint (e.g. `"ab"` → at most 2 entries, however big the alphabet).
- Long string vs. small alphabet → `m` is the binding constraint (e.g. a 1000-char string of only lowercase letters → at most 26 entries, no matter how long the string gets).

## Complexity comparison — all four versions
| Version | Time | Space | Key idea |
|---|---|---|---|
| 1. Naive (rebuild set/substring) | O(n³) | O(n) | Check every substring from scratch |
| 2. Incremental `seen` per `i` | O(n²) | O(min(n, m)) | Reuse set within one `i`, reset per `i` |
| 3. Sliding window + `set` | **O(n)** | O(min(n, m)) | Never reset — shrink window one char at a time |
| 4. Sliding window + hash map | **O(n)** | O(min(n, m)) | Jump `left` directly using last-seen index |

