# 🗺️NeetCode  Roadmap

![NeetCode-style DSA Roadmap](./Neetcode_Roadmap.jfif)

---

# 🧠 DSA Notes: Algorithms, Data Structures & Complexity

> Personal working notes — algorithm patterns, complexity analysis, and gotchas collected while solving problems.

---

## Table of Contents
1. [Boyer–Moore Majority Vote Algorithm](#-boyermoore-majority-vote-algorithm)
2. [Notes to Remember: set & dict Fundamentals](#-notes-to-remember-set--dict-fundamentals)
3. [Contains Duplicate II — Sliding Window (LeetCode 219)](#-contains-duplicate-ii--sliding-window-leetcode-219)
4. [Sliding Window Technique: Longest Substring Without Repeating Characters](#-sliding-window-technique-longest-substring-without-repeating-characters)
5. [Best Time to Buy and Sell Stock](#-best-time-to-buy-and-sell-stock-leetcode-121)

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

# 🪟 Contains Duplicate II — Sliding Window (LeetCode 219)

> Notes from working through **LeetCode 219 — Contains Duplicate II**, going from a hashmap-of-indices solution to an explicit sliding-window formulation, plus a brute-force O(n·k) baseline for comparison.

## The problem
Given an integer array `nums` and an integer `k`, return `true` if there are two **distinct indices** `i` and `j` such that `nums[i] == nums[j]` **and** `abs(i - j) <= k`.

Unlike plain "Contains Duplicate" (LeetCode 217), a duplicate only counts if the two occurrences are **close enough together** (within a window of `k` positions) — a duplicate far apart in the array doesn't trigger `true`.

## Core idea
Don't compare every pair of equal values across the whole array — only care about duplicates **within a window of size k**. This naturally leads to a **sliding window**: keep track of just the "recent" elements (the last `k` seen), and forget anything older, since it can no longer satisfy `abs(i - j) <= k`.

There are two equivalent ways to express this window:
- **Implicitly**, via a hashmap that stores `value → last index seen`, and checking the distance directly.
- **Explicitly**, via a `set` that only ever contains the elements currently "in range," maintained by adding/removing as the window slides.

## The four approaches, in order explored

### 1. Hashmap of last-seen indices (distance checked explicitly)
```python
def containsNearbyDuplicate(nums, k):
    hash_map = {}
    for index, num in enumerate(nums):
        if num in hash_map and abs(hash_map[num] - index) <= k:
            return True
        hash_map[num] = index
    return False
```
- Stores, for every value, the **index of its most recent occurrence**.
- On seeing `num` again, checks if the distance to its last occurrence is `<= k`.
- **Time: O(n)** average · **Space: O(min(n, k+1))** — at most one entry per distinct value in range.

### 2. Sliding window with a `set`, using a `for` loop and index math
```python
def contain_dupli_sliding_window(nums, k):
    window = set()
    for i, num in enumerate(nums):
        if num in window:
            return True
        window.add(num)
        if len(window) > k:
            window.remove(nums[i - k])
    return False
```
- The set holds **only** the elements currently within the window, never a stale one — this is what makes the `in` check automatically respect `abs(i - j) <= k`, without computing any distance.
- **Time: O(n)** average · **Space: O(min(n, k))**

### 3. Sliding window with two explicit pointers (`while` loop)
```python
def containsNearbyDuplicate(nums, k):
    window = set()
    left = 0
    right = 0
    n = len(nums)

    while right < n:
        while right - left > k:      # shrink until window size <= k+1
            window.remove(nums[left])
            left += 1
        if nums[right] in window:
            return True
        window.add(nums[right])
        right += 1
    return False
```
- Same logic as version 2, but the window boundaries are tracked explicitly with `left`/`right` instead of index arithmetic (`i - k`).
- The inner `while` never runs more than once per outer step here (since `right` only advances by 1 at a time), so total time stays **O(n)** — each element is added/removed from the set at most once.
- More general/robust pattern to have in your toolkit: in other sliding-window problems the window may need to shrink by more than one step per iteration, and `while` handles that; `if` would not.

### 4. Brute force — bounded nested loop (no hash structure)
```python
def containsNearbyDuplicate(nums, k):
    for i in range(len(nums)):
        for j in range(max(0, i - k), i):
            if nums[i] == nums[j]:
                return True
    return False
```
- For each `i`, only scans the **last `k` elements** before it — smarter than the full O(n²) brute force, but still re-scans a window instead of using a hash lookup.
- **Time: O(n·k)** · **Space: O(1)** — trades time for zero extra memory.
- Useful mainly to see *why* the hash-based versions help: same "look back at most k elements" idea, but a hash set turns each lookup from O(k) into O(1) average.

## 🔑 Key tip: why we remove `nums[i - k]` specifically
When processing index `i`, the **valid window** is `[i-k, i]` — that's `k+1` elements (the current one plus its `k` predecessors). So the set should never grow past `k+1` entries.

The element that becomes stale is the one that will fall **outside** the window as soon as we move to `i+1`: at that point the valid window becomes `[i-k+1, i+1]`, and index `i-k` is exactly the one left behind. That's why the eviction target is always `nums[i - k]` — it's not an arbitrary offset, it's "the element exactly `k` steps behind the one we just added."

Trace with `k=3`, `nums=[10,20,30,40,50]`:

| i | num | window before | action | window after |
|---|---|---|---|---|
| 0 | 10 | {} | add 10 | {10} |
| 1 | 20 | {10} | add 20 | {10,20} |
| 2 | 30 | {10,20} | add 30 | {10,20,30} |
| 3 | 40 | {10,20,30} | add 40 → size 4 > k(3) → remove `nums[3-3]=nums[0]=10` | {20,30,40} |
| 4 | 50 | {20,30,40} | add 50 → size 4 > k(3) → remove `nums[4-3]=nums[1]=20` | {30,40,50} |

After cleanup, the set always holds exactly the `k` most recent elements *before* the current candidate — so any hit found via `num in window` is guaranteed to satisfy `abs(i - j) <= k`.

## Complexity comparison — all four versions
| Version | Time | Space | Key idea |
|---|---|---|---|
| 1. Hashmap of last index | O(n) avg | O(min(n, k+1)) | Store last index per value, check distance directly |
| 2. Sliding window + set (`for`, index math) | O(n) avg | O(min(n, k)) | Set only ever holds elements in range |
| 3. Sliding window + set (two pointers, `while`) | O(n) avg | O(min(n, k)) | Same idea, window bounds tracked explicitly |
| 4. Brute force (bounded nested loop) | O(n·k) | O(1) | No hash structure — same window idea, slower lookup |

## Note on "O(1) average, not worst case"
Hash set/dict operations (`in`, `add`, `remove`) are **O(1) on average**, not guaranteed worst case — collisions can in theory degrade a single operation to O(n), making the true worst case O(n²) for the hashmap/set versions. In practice (especially with `int` keys, as in this problem), Python's dynamic table resizing keeps the load factor low and collisions rare, so treating these as O(n) total is the standard and reasonable assumption for interview/LeetCode purposes.

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

---
---

# 📈 Best Time to Buy and Sell Stock (LeetCode 121)

> Notes from working through **LeetCode 121 — Best Time to Buy and Sell Stock**, comparing brute force, greedy (min-tracking), and two-pointer approaches.

## The problem
Given `prices[i]` = the stock price on day `i`, find the **maximum profit** from **one buy + one sell**, where the sell day must come **after** the buy day (you cannot buy and sell on the same day, and you cannot sell before you buy).

If no profit is possible (prices only decrease), the answer is `0` — you simply don't do the transaction.

## The three approaches, in order of improvement

### 1. Naive — check every pair of days
```python
def best_time_buy_sell(nums):
    n = len(nums)
    max_profit = 0
    for i in range(n):
        for j in range(i+1, n):
            profit = nums[j] - nums[i]
            max_profit = max(max_profit, profit)
    return max_profit
```
- Outer loop `i` = every possible **buy day**, inner loop `j` (starting at `i+1`) = every possible **sell day after it**.
- Generates all valid `(buy, sell)` pairs and keeps the best profit found.
- **Time: O(n²)** — every pair of days is compared.
- **Space: O(1)** — only `max_profit` is stored.

This works, but it re-examines information you already know: once you've found the cheapest price so far, you don't need to re-compare against every earlier day again for each new `j`.

---

### 2. Greedy — track the minimum price seen so far
```python
def best_time_optimized(prices):
    min_price = float('inf')
    max_profit = 0
    for i in range(len(prices)):
        if prices[i] < min_price:      # new lowest buy price found
            min_price = prices[i]
        profit = prices[i] - min_price  # profit if sold today
        max_profit = max(max_profit, profit)
    return max_profit
```
**Key idea**: instead of comparing every pair, keep a **running minimum** of the cheapest price seen up to (and including) the current day.

- `min_price` = best day to have bought, *so far*.
- At each day `i`, compute: *"if I sold today, having bought at the cheapest point so far, what would my profit be?"* → `prices[i] - min_price`.
- Because `min_price` only ever comes from a day **before or equal to** `i`, this naturally respects "buy before sell" without needing a nested loop.
- One single pass replaces the need to re-scan previous days.

**Time: O(n)** — one pass, one comparison + one subtraction per element.
**Space: O(1)** — only two variables (`min_price`, `max_profit`).

⚠️ **Why `if prices[i] < min_price` and not `<=`**: using `<=` wouldn't break correctness here (profit would just be `0` that day), but `<` is the natural/minimal condition — you only update the minimum when you find something strictly cheaper.

---

### 3. Two-pointer variant — `left` (buy) / `right` (sell)
```python
def another_way(prices):
    n, max_profit = len(prices), 0
    right, left = 1, 0
    while right < n:
        if prices[right] < prices[left]:
            left = right
        current_profit = prices[right] - prices[left]
        max_profit = max(max_profit, current_profit)
        right += 1
    return max_profit
```
**Key idea**: this is the *same greedy logic* as version 2, reframed with two explicit pointers instead of a `min_price` variable.

- `left` = index of the best day to buy so far (equivalent to where `min_price` currently is).
- `right` = the day being considered as a potential sell day, always ahead of `left`.
- If `prices[right] < prices[left]`, the current buy point is no longer optimal → move `left` to `right` (found a cheaper buy day).
- Otherwise, compute the profit `prices[right] - prices[left]` and update `max_profit`.
- `right` always moves forward one step at a time; `left` "jumps" to `right` only when a new minimum is found — it never moves backward.

**Time: O(n)** — `right` traverses the array once; `left` only ever jumps forward.
**Space: O(1)** — just two indices and one profit variable.

### Why this is equivalent to the greedy `min_price` approach
`prices[left]` **is** the minimum price so far — the pointer version is just storing the *index* of that minimum instead of the *value* directly. Both encode the exact same invariant: *"the best possible buy day up to the current point."*

---

## Common pitfall across all optimal versions
```python
# ❌ WRONG — comparing to a price seen AFTER the current day would violate "buy before sell"
if prices[right] < prices[left] and right > left:   # redundant guard, right is always > left by construction here
```
This isn't actually a bug — just worth noting *why* it's safe: because `left` and `right` (or `min_price`) are only ever updated using **information already scanned**, the "buy must happen before sell" constraint is automatically respected. You never need to check `right > left` explicitly, since the loop structure guarantees it.

## Complexity comparison — all three versions

| Version | Time | Space | Key idea |
|---|---|---|---|
| 1. Naive (all pairs) | O(n²) | O(1) | Compare every buy day against every later sell day |
| 2. Greedy (`min_price`) | **O(n)** | O(1) | Track cheapest price seen so far, compute profit at each step |
| 3. Two-pointer (`left`/`right`) | **O(n)** | O(1) | Same greedy logic, expressed with index pointers instead of a value |

## Test case worth remembering
```python
prices = [7, 6, 4, 3, 1]   # strictly decreasing → no profit possible
best_time_optimized(prices)  # → 0
```
This is the classic edge case: if prices only go down, `max_profit` correctly stays at `0` because every `prices[i] - min_price` comparison ends up `≤ 0`, and `max()` never lets `max_profit` go negative.