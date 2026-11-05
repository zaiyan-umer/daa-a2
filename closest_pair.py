"""
Closest Pair of Points - Divide and Conquer algorithm.

Finds the two points with minimum Euclidean distance in O(n log n) time.
Uses index-based partitioning to maintain O(n log n) complexity.
"""

import math


def _dist(p1, p2):
    """Euclidean distance between two points."""
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])


def _brute_force(pts, indices):
    """Brute-force closest pair for small sets (<=3 points)."""
    best = None
    n = len(indices)
    for i in range(n):
        for j in range(i + 1, n):
            p = pts[indices[i]]
            q = pts[indices[j]]
            d = _dist(p, q)
            if best is None or d < best[2]:
                best = (p, q, d)
    return best


def _closest_pair_rec(pts, x_idx, y_idx):
    """
    Recursive divide-and-conquer.

    pts: list of (x, y) tuples
    x_idx: indices into pts, sorted by x-coordinate
    y_idx: indices into pts, sorted by y-coordinate
    Returns (point1, point2, distance)
    """
    n = len(x_idx)

    # Base case: 3 or fewer points -> brute force
    if n <= 3:
        return _brute_force(pts, x_idx)

    # Divide: split x_idx into left/right halves
    mid = n // 2
    left_x = x_idx[:mid]
    right_x = x_idx[mid:]

    # Build left_y and right_y from y_idx using a set for O(1) membership
    left_set = set(left_x)
    left_y = []
    right_y = []
    for idx in y_idx:
        if idx in left_set:
            left_y.append(idx)
        else:
            right_y.append(idx)

    # Conquer
    d_left = _closest_pair_rec(pts, left_x, left_y)
    d_right = _closest_pair_rec(pts, right_x, right_y)

    if d_left[2] <= d_right[2]:
        best = d_left
    else:
        best = d_right
    delta = best[2]

    # Build strip (indices of points within delta of mid_x), y-sorted
    mid_x = pts[x_idx[mid]][0]
    strip = [idx for idx in y_idx if abs(pts[idx][0] - mid_x) < delta]

    # Check strip: for each point, compare against next up to 7 points
    strip_len = len(strip)
    for i in range(strip_len):
        p = pts[strip[i]]
        for j in range(i + 1, min(i + 8, strip_len)):
            q = pts[strip[j]]
            d = _dist(p, q)
            if d < best[2]:
                best = (p, q, d)
    return best


def closest_pair(points):
    """
    Finds the closest pair of points using Divide and Conquer.

    Args:
        points: iterable of (x, y) coordinate pairs

    Returns:
        (point1, point2, distance) where distance is the Euclidean distance
        between the two closest points.

    Raises:
        ValueError: if fewer than 2 points are provided.
    """
    pts = list(points)
    if len(pts) < 2:
        raise ValueError("At least 2 points are required")

    x_idx = sorted(range(len(pts)), key=lambda i: pts[i][0])
    y_idx = sorted(range(len(pts)), key=lambda i: pts[i][1])
    return _closest_pair_rec(pts, x_idx, y_idx)