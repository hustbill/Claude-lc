# 🚀 Staff SDE Interview Brain (Project Memory)

## 📌 Context & Goals
- **Objective:** Preparing for Staff SDE (L7+) interviews.
- **Focus:** High-performance Python, Distributed Systems, and DP optimization.
- **Principle:** Code must be "Production-Ready"—clean, typed, and edge-case resilient.

## 🛠️ Tech Stack & Conventions
- **Language:** Python 3.12+ (Utilize `typing`, `match`, and `itertools`).
- **Style:** Google Style docstrings, PEP 8 compliance.
- **Complexity:** Always aim for optimal time/space complexity (e.g., O(N log N) over O(N^2)).
- **Testing:** Use `pytest` for all verification. Focus on boundary conditions (empty, large, overflow).

## 📋 Common Commands
- **Test:** `pytest -v tests/test_*.py`
- **Lint:** `black . && mypy .`
- **Benchmark:** `python3 benchmarks/runner.py`

## 🧠 Memory & Decisions (The "Affaan" Layer)
- **DP Pattern:** Prefer iterative DP with space optimization over recursive + memoization where applicable.
- **Naming:** Variables must be descriptive (e.g., `tails` vs `dp_array`).
- **LIS Decision:** We implemented the Patience Sorting version of LIS on Feb 20. Do not revert to O(N^2) unless explicitly requested for comparison.

## 📝 Recent Progress
- [2026-02-15] Completed `Number of Islands` (Graph).
- [2026-02-18] Completed `Longest Increasing Subsequence` (DP O(N log N)).
- [Next Task] `354. Russian Doll Envelopes` (2D LIS).