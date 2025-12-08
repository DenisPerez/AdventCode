import os
from typing import List


def solve_from_file(filename: str) -> int:
    with open(filename, "r") as f:
        lines = [line.rstrip("\n") for line in f if line.strip() != ""]

    if not lines:
        return 0

    width = max(len(line) for line in lines)
    grid = [line.ljust(width) for line in lines]

    height = len(grid)
    op_row_idx = height - 1          # bottom row = operators
    op_row = grid[op_row_idx]

    def is_separator(col: int) -> bool:
        return all(grid[r][col] == " " for r in range(height))

    total = 0
    col = width - 1 

    while col >= 0:
        ch = op_row[col]

        if ch not in "+*":
            col -= 1
            continue

        op = ch

        start = col
        while start > 0 and not is_separator(start - 1):
            start -= 1

        end = col
        while end < width - 1 and not is_separator(end + 1):
            end += 1

        numbers: List[int] = []
        for c in range(end, start - 1, -1):
            digits = [
                grid[r][c]
                for r in range(op_row_idx)
                if grid[r][c].isdigit()
            ]
            if digits:
                numbers.append(int("".join(digits)))

        if not numbers:
            col = start - 1
            continue

        if op == "+":
            value = sum(numbers)
        elif op == "*":
            value = 1
            for n in numbers:
                value *= n

        total += value

        col = start - 1

    return total


if __name__ == "__main__":
    INPUT_FILENAME = "input.txt"
    ans = solve_from_file(INPUT_FILENAME)
    print(f"Solution is: {ans}")
