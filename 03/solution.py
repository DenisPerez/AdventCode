import os

def solve_from_file(filename="product_ids.txt"):

    file = open(filename, 'r')
    lines = list(file.readlines())
    solution = 0

    for line in lines:
        line = line.strip()
        N = len(line)
        joltage = 0
        stack = []
        for idx in range(N):
            while len(stack) > 0 and stack[-1] < line[idx] and len(stack) + (N - idx) > 12:
                stack.pop()
            stack.append(line[idx])

        joltage = int(''.join(stack[:12]))
        print(f"In {line}, the largest joltage is {joltage}")
        solution += joltage
    print(f'The Solution is: {solution}')
    
if __name__ == "__main__":
    INPUT_FILENAME = "input.txt"

    solve_from_file(INPUT_FILENAME)