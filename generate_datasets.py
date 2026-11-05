import os
import random


def generate_closest_pair_datasets(num_datasets=10, seed=42):
    point_counts = [150, 250, 400, 600, 800, 1000, 1500, 2000, 3000, 5000]
    rng = random.Random(seed)
    base_dir = os.path.join(os.path.dirname(__file__), "datasets", "closest_pair")

    for i in range(1, num_datasets + 1):
        n = point_counts[i - 1]
        filename = f"input_{i:02d}.txt"
        filepath = os.path.join(base_dir, filename)

        coords = set()
        points = []
        min_coord = -10_000_000
        max_coord = 10_000_000

        while len(points) < n:
            x = rng.randint(min_coord, max_coord)
            y = rng.randint(min_coord, max_coord)
            if (x, y) not in coords:
                coords.add((x, y))
                points.append((x, y))

        with open(filepath, "w") as f:
            f.write(f"{n}\n")
            for x, y in points:
                f.write(f"{x} {y}\n")

    print(f"Generated {num_datasets} closest pair datasets in {base_dir}")


def generate_multiplication_datasets(num_datasets=10, seed=42):
    digit_lengths = [150, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
    rng = random.Random(seed)
    base_dir = os.path.join(os.path.dirname(__file__), "datasets", "multiplication")

    for i in range(1, num_datasets + 1):
        dl = digit_lengths[i - 1]
        filename = f"input_{i:02d}.txt"
        filepath = os.path.join(base_dir, filename)

        first_digit = rng.randint(1, 9)
        remaining_digits = dl - 1
        num_str = str(first_digit)
        for _ in range(remaining_digits):
            num_str += str(rng.randint(0, 9))

        first_digit2 = rng.randint(1, 9)
        num_str2 = str(first_digit2)
        for _ in range(remaining_digits):
            num_str2 += str(rng.randint(0, 9))

        attempts = 0
        while num_str == num_str2 and attempts < 100:
            first_digit2 = rng.randint(1, 9)
            num_str2 = str(first_digit2)
            for _ in range(remaining_digits):
                num_str2 += str(rng.randint(0, 9))
            attempts += 1

        with open(filepath, "w") as f:
            f.write(f"{num_str}\n")
            f.write(f"{num_str2}\n")

    print(f"Generated {num_datasets} multiplication datasets in {base_dir}")


if __name__ == "__main__":
    generate_closest_pair_datasets()
    generate_multiplication_datasets()
    print("\nDataset generation complete.")