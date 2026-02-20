
Here’s a plan for **LeetCode 354: Russian Doll Envelopes** that fits your current setup and conventions.

---

# Plan: 354. Russian Doll Envelopes (2D LIS)

## Problem Summary

- **Input:** `envelopes: list[list[int]]` where each `[w, h]` is width and height.
- **Rule:** Envelope A fits in B iff both `w_A < w_B` and `h_A < h_B`.
- **Goal:** Maximum chain length (maximum number of nested envelopes).

---

## Approach: Sort + 1D LIS (O(N log N))

Reduce the 2D problem to 1D LIS (Patience Sorting) so you can reuse your LIS solution and keep O(N log N) time.

### Step 1: Sort

- Sort by width **ascending**.
- For equal width, sort by height **descending**.

This avoids putting two envelopes of the same width in the same chain, since they cannot nest.

### Step 2: 1D LIS on Heights

- Extract heights in sorted order.
- Run Patience Sorting (binary search + `tails`) on the heights.

### Step 3: Result

- Return `len(tails)`.

---

## Implementation Checklist

| # | Task | Notes |
|---|------|-------|
| 1 | **Solution module** | Add `lc_354_russian_doll_envelopes.py` (or under `dp/` if you use that layout) |
| 2 | **Core function** | `max_envelopes(envelopes: list[list[int]]) -> int` with full typing and docstrings |
| 3 | **Sort key** | `key=lambda e: (e[0], -e[1])` (width ↑, height ↓) |
| 4 | **LIS logic** | Use `bisect_left` and a `tails` array, same pattern as your LIS implementation |
| 5 | **Edge cases** | Empty `envelopes`, single envelope, duplicates, very large inputs |

---

## Complexity Targets

- **Time:** O(N log N) — sort + one LIS pass with binary search.
- **Space:** O(N) — `tails` (and a height array if you materialize it).

---

## Testing (pytest)

- Empty list → `0`
- Single envelope → `1`
- Small examples from LeetCode
- All same size → `1`
- All strictly increasing → `N`
- Mixed widths and heights
- Large inputs (e.g. 5000+ envelopes) to confirm performance

---

## File Layout (Suggested)

```
claude-lc/
├── src/                          # or dp/
│   └── lc_354_russian_doll_envelopes.py
├── tests/
│   └── test_354_russian_doll_envelopes.py
└── benchmarks/
    └── (optional) 354 benchmark
```

---

## Optional: Reuse LIS Helper

If you already have a standalone LIS (Patience Sorting) helper, you can call it:

```python
# Pseudocode
heights = [h for _, h in sorted(envelopes, key=lambda e: (e[0], -e[1]))]
return lis_length(heights)  # Your existing Patience Sorting LIS
```

Otherwise, inline the `tails` + `bisect_left` logic in `max_envelopes`.

---

## References

- Labuladong: [Russian Doll Envelopes](https://labuladong.gitbook.io/algo-en/iii.-algorithmic-thinking/russiandollenvelopes)
- LeetCode 354 problem and examples