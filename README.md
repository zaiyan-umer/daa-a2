# Divide and Conquer Algorithms

Implementation of two classic Divide and Conquer algorithms:

1. **Closest Pair of Points** — O(n log n) divide-and-conquer algorithm
2. **Karatsuba Integer Multiplication** — O(n^log₂(3)) ≈ O(n^1.585) divide-and-conquer multiplication

---

## Algorithms Implemented

### 1. Closest Pair of Points

Given a set of 2D points, finds the two points with minimum Euclidean distance.

**Algorithm:**
- Pre-sort points by X and Y coordinates
- Recursively divide into left/right halves
- Find closest pair in each half
- Check "strip" around dividing line (at most 7 subsequent Y-sorted points per point)
- Maintain Y-sorted order throughout recursion (no re-sorting)

**Time Complexity:** O(n log n)
- O(n log n) initial sort
- Recurrence: T(n) = 2T(n/2) + O(n) → O(n log n) by Master Theorem

**Function:**
```python
def closest_pair(points):
    """Returns (point1, point2, distance)"""
```

---

### 2. Karatsuba Multiplication

Multiplies two large integers using only three recursive multiplications per step.

**Algorithm:**
For x = a·10^m + b, y = c·10^m + d:
- z0 = b·d
- z2 = a·c
- z1 = (a+b)·(c+d) − z2 − z0
- Result = z2·10^(2m) + z1·10^m + z0

**Time Complexity:** O(n^log₂(3)) ≈ O(n^1.585)
- Recurrence: T(n) = 3T(n/2) + O(n) → O(n^log₂(3))

**Function:**
```python
def karatsuba(x, y):
    """Returns integer product"""
```

---

## Project Structure

```
divide-conquer-visualizer/
├── closest_pair.py       # O(n log n) closest pair algorithm
├── karatsuba.py          # Karatsuba multiplication
├── generate_datasets.py  # Dataset generation (fixed seed = 42)
├── run_benchmarks.py     # Execute algorithms on all datasets
├── datasets/
│   ├── closest_pair/     # 10 input files (150–5000 points)
│   └── multiplication/   # 10 input files (150–1000 digits)
├── results/
│   ├── closest_pair.csv  # 10 rows with timing + distance
│   └── multiplication.csv# 10 rows with timing
└── README.md             # This file
```

---

## Dataset Summary

### Closest Pair (10 files)
| File | Points | Coordinates |
|------|--------|-------------|
| input_01.txt | 150 | Unique integer coords in [-10M, 10M] |
| input_02.txt | 250 | ... |
| input_03.txt | 400 | ... |
| input_04.txt | 600 | ... |
| input_05.txt | 800 | ... |
| input_06.txt | 1,000 | ... |
| input_07.txt | 1,500 | ... |
| input_08.txt | 2,000 | ... |
| input_09.txt | 3,000 | ... |
| input_10.txt | 5,000 | ... |

### Multiplication (10 files)
| File | Digits per Integer |
|------|-------------------|
| input_01.txt | 150 |
| input_02.txt | 200 |
| input_03.txt | 300 |
| input_04.txt | 400 |
| input_05.txt | 500 |
| input_06.txt | 600 |
| input_07.txt | 700 |
| input_08.txt | 800 |
| input_09.txt | 900 |
| input_10.txt | 1,000 |

All datasets generated with fixed seed `42` for reproducibility.

---

## Usage

### Generate Datasets
```bash
python3 generate_datasets.py
```
Creates all 20 input files under `datasets/`.

### Run Benchmarks
```bash
python3 run_benchmarks.py
```
Executes both algorithms on all datasets, writes CSVs to `results/`, prints summary.

### Test Algorithms Individually
```python
from closest_pair import closest_pair
from karatsuba import karatsuba

# Closest pair
points = [(0, 0), (3, 4), (1, 1)]
p1, p2, d = closest_pair(points)  # d = 5.0

# Karatsuba
result = karatsuba(123456789, 987654321)  # Verified against x * y
```

---

## Benchmark Results

### Closest Pair
| Dataset | Points | Distance | Time (s) |
|---------|--------|----------|----------|
| input_01 | 150 | 145034.89 | 0.000765 |
| input_02 | 250 | 103234.06 | 0.001367 |
| input_03 | 400 | 44524.21 | 0.002138 |
| input_04 | 600 | 5926.19 | 0.003594 |
| input_05 | 800 | 19332.67 | 0.004265 |
| input_06 | 1,000 | 17576.49 | 0.006671 |
| input_07 | 1,500 | 1738.90 | 0.009230 |
| input_08 | 2,000 | 9752.97 | 0.011882 |
| input_09 | 3,000 | 3546.91 | 0.020596 |
| input_10 | 5,000 | 1688.17 | 0.035599 |

**Observation:** Time scales roughly as n log n. At 5000 points, execution takes ~36 ms.

---

### Karatsuba Multiplication
| Dataset | Digits | Time (s) | Verified |
|---------|--------|----------|----------|
| input_01 | 150 | 0.001906 | True |
| input_02 | 200 | 0.002634 | True |
| input_03 | 300 | 0.005619 | True |
| input_04 | 400 | 0.008134 | True |
| input_05 | 500 | 0.011469 | True |
| input_06 | 600 | 0.017069 | True |
| input_07 | 700 | 0.020935 | True |
| input_08 | 800 | 0.024714 | True |
| input_09 | 900 | 0.029097 | True |
| input_10 | 1,000 | 0.039748 | True |

**Observation:** Time scales as O(n^1.585). At 1000 digits, execution takes ~40 ms. All 10 results verified against Python's built-in `*` multiplication.