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
