import math


def _dist(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])


def _brute_force(pts, indices):
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
    n = len(x_idx)

    if n <= 3:
        return _brute_force(pts, x_idx)

    mid = n // 2
    left_x = x_idx[:mid]
    right_x = x_idx[mid:]

    left_set = set(left_x)
    left_y = []
    right_y = []
    for idx in y_idx:
        if idx in left_set:
            left_y.append(idx)
        else:
            right_y.append(idx)

    d_left = _closest_pair_rec(pts, left_x, left_y)
    d_right = _closest_pair_rec(pts, right_x, right_y)

    if d_left[2] <= d_right[2]:
        best = d_left
    else:
        best = d_right
    delta = best[2]

    mid_x = pts[x_idx[mid]][0]
    strip = [idx for idx in y_idx if abs(pts[idx][0] - mid_x) < delta]

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
    pts = list(points)
    if len(pts) < 2:
        raise ValueError("At least 2 points are required")

    x_idx = sorted(range(len(pts)), key=lambda i: pts[i][0])
    y_idx = sorted(range(len(pts)), key=lambda i: pts[i][1])
    return _closest_pair_rec(pts, x_idx, y_idx)