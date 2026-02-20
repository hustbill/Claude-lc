"""LeetCode 354: Russian Doll Envelopes.

You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi]
represents the width and the height of an envelope.

One envelope can fit into another if and only if both the width and height
of one envelope are greater than the other envelope's width and height.

Return the maximum number of envelopes you can Russian doll (i.e., put one
inside the other).

Note: You cannot rotate an envelope.
"""

from bisect import bisect_left


def max_envelopes(envelopes: list[list[int]]) -> int:
    """Return the maximum number of envelopes that can be nested.

    Uses sort + 1D LIS (Patience Sorting) for O(N log N) time.

    Args:
        envelopes: List of [width, height] pairs.

    Returns:
        Maximum chain length (number of nested envelopes).

    Examples:
        >>> max_envelopes([[5, 4], [6, 4], [6, 7], [2, 3]])
        3
        >>> max_envelopes([[1, 1], [1, 1], [1, 1]])
        1
    """
    if not envelopes:
        return 0

    # Sort by width ascending; for equal width, sort height descending
    # so same-width envelopes never appear in the same LIS chain.
    sorted_env = sorted(envelopes, key=lambda e: (e[0], -e[1]))
    heights = [h for _, h in sorted_env]

    # Patience Sorting LIS: tails[i] = smallest height ending a chain of length i+1
    tails: list[int] = []
    for h in heights:
        idx = bisect_left(tails, h)
        if idx == len(tails):
            tails.append(h)
        else:
            tails[idx] = h
    return len(tails)
