"""Tests for LeetCode 354: Russian Doll Envelopes."""

import pytest

from lc_354_russian_doll_envelopes import max_envelopes


class TestMaxEnvelopes:
    """Test suite for max_envelopes."""

    def test_empty(self) -> None:
        """Empty list returns 0."""
        assert max_envelopes([]) == 0

    def test_single_envelope(self) -> None:
        """Single envelope returns 1."""
        assert max_envelopes([[5, 5]]) == 1

    def test_example_1(self) -> None:
        """LeetCode example: [[5,4],[6,4],[6,7],[2,3]] -> 3."""
        assert max_envelopes([[5, 4], [6, 4], [6, 7], [2, 3]]) == 3

    def test_example_2(self) -> None:
        """LeetCode example: [[1,1],[1,1],[1,1]] -> 1."""
        assert max_envelopes([[1, 1], [1, 1], [1, 1]]) == 1

    def test_all_same_size(self) -> None:
        """All envelopes same size can only nest 1."""
        assert max_envelopes([[3, 3], [3, 3], [3, 3]]) == 1

    def test_strictly_increasing(self) -> None:
        """Strictly increasing w and h -> chain of length N."""
        envelopes = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
        assert max_envelopes(envelopes) == 5

    def test_same_width_different_heights(self) -> None:
        """Same width, different heights: only one per width in chain."""
        # [2,3], [5,4], [6,7] -> 3. Same-width [5,4],[6,4],[6,7] ->
        # sort by (w, -h): [5,4],[6,7],[6,4] -> heights [4,7,4] -> LIS [4,7] = 2
        # Actually [2,3],[5,4],[6,7] fits: 2<5, 3<4 and 5<6, 4<7. So 3.
        assert max_envelopes([[2, 3], [5, 4], [6, 7]]) == 3

    def test_descending_order(self) -> None:
        """Descending sizes -> chain of 1."""
        assert max_envelopes([[5, 5], [4, 4], [3, 3], [2, 2], [1, 1]]) == 1

    def test_mixed(self) -> None:
        """Mixed widths and heights."""
        envelopes = [[4, 5], [4, 6], [6, 7], [2, 3], [1, 1]]
        # Sorted: [1,1], [2,3], [4,6], [4,5], [6,7]
        # Heights: [1, 3, 6, 5, 7] -> LIS [1,3,5,7] or [1,3,6,7] = 4
        assert max_envelopes(envelopes) == 4

    def test_two_envelopes_nestable(self) -> None:
        """Two envelopes where one nests in the other."""
        assert max_envelopes([[1, 1], [2, 2]]) == 2

    def test_two_envelopes_not_nestable(self) -> None:
        """Two envelopes that cannot nest (e.g. same width)."""
        assert max_envelopes([[2, 1], [2, 3]]) == 1
