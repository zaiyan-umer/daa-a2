import csv
import os
import time
from closest_pair import closest_pair
from karatsuba import karatsuba


def run_closest_pair_benchmarks():
    results = []
    base_dir = os.path.join(os.path.dirname(__file__), "datasets", "closest_pair")

    for i in range(1, 11):
        fname = f"input_{i:02d}.txt"
        filepath = os.path.join(base_dir, fname)

        with open(filepath) as f:
            lines = f.readlines()

        n = int(lines[0].strip())
        pts = []
        for line in lines[1:]:
            x, y = line.strip().split()
            pts.append((int(x), int(y)))

        t0 = time.perf_counter()
        p1, p2, d = closest_pair(pts)
        t1 = time.perf_counter()

        results.append({
            "dataset": f"input_{i:02d}",
            "input_size": n,
            "closest_point_1": f"{p1[0]} {p1[1]}",
            "closest_point_2": f"{p2[0]} {p2[1]}",
            "distance": d,
            "execution_time_seconds": round(t1 - t0, 6)
        })

    return results


def run_multiplication_benchmarks():
    results = []
    base_dir = os.path.join(os.path.dirname(__file__), "datasets", "multiplication")

    for i in range(1, 11):
        fname = f"input_{i:02d}.txt"
        filepath = os.path.join(base_dir, fname)

        with open(filepath) as f:
            lines = f.readlines()

        x = int(lines[0].strip())
        y = int(lines[1].strip())

        t0 = time.perf_counter()
        prod = karatsuba(x, y)
        verified = prod == x * y
        t1 = time.perf_counter()

        results.append({
            "dataset": f"input_{i:02d}",
            "input_size": max(len(str(x)), len(str(y))),
            "execution_time_seconds": round(t1 - t0, 6),
            "verified": verified
        })

    return results


def write_closest_pair_csv(results, output_dir):
    filepath = os.path.join(output_dir, "closest_pair.csv")
    fieldnames = [
        "dataset", "input_size", "closest_point_1", "closest_point_2",
        "distance", "execution_time_seconds"
    ]
    with open(filepath, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in results:
            writer.writerow(r)
    print(f"Wrote {filepath}")


def write_multiplication_csv(results, output_dir):
    filepath = os.path.join(output_dir, "multiplication.csv")
    fieldnames = ["dataset", "input_size", "execution_time_seconds"]
    with open(filepath, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in results:
            writer.writerow({k: r[k] for k in fieldnames})
    print(f"Wrote {filepath}")


def print_summary(cp_results, mul_results):
    print("=" * 72)
    print("CLOSEST PAIR BENCHMARK RESULTS")
    print("=" * 72)
    print(f"{'Dataset':>10s}  {'Points':>8s}  {'Distance':>14s}  {'Time (s)':>12s}")
    print("-" * 72)
    for r in cp_results:
        print(f"{r['dataset']:>10s}  {r['input_size']:8d}  "
              f"{r['distance']:14.6f}  {r['execution_time_seconds']:12.6f}")

    print()
    print("=" * 72)
    print("MULTIPLICATION BENCHMARK RESULTS")
    print("=" * 72)
    print(f"{'Dataset':>10s}  {'Digits':>8s}  {'Time (s)':>12s}  {'Verified':>10s}")
    print("-" * 72)
    for r in mul_results:
        print(f"{r['dataset']:>10s}  {r['input_size']:8d}  "
              f"{r['execution_time_seconds']:12.6f}  {str(r['verified']):>10s}")

    print()
    print("Benchmark execution complete.")


if __name__ == "__main__":
    base_dir = os.path.dirname(__file__)
    output_dir = os.path.join(base_dir, "results")
    os.makedirs(output_dir, exist_ok=True)

    cp_results = run_closest_pair_benchmarks()
    mul_results = run_multiplication_benchmarks()

    write_closest_pair_csv(cp_results, output_dir)
    write_multiplication_csv(mul_results, output_dir)
    print_summary(cp_results, mul_results)