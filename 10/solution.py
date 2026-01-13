import os
from typing import List, Tuple, Dict
import re

def writeToFile(outputFileName: str, lines: list, h: int, w: int):
    with open(outputFileName, 'w') as f:
        for row in range(h):
            for col in range(w):
                f.write(lines[row][col])
            f.write('\n')

def solve_from_file(filename: str) -> int:
    result = 0
    with open(filename, "r") as f:
        for line in f:
            # print(line)
            lineElements = line.strip().split()
            targetString = lineElements.pop(0)

            target = [0] * len(targetString)

            for c_idx in range(len(targetString)):

                if(c_idx == 0 or c_idx == len(targetString)):
                    continue

                c = targetString[c_idx]

                if c == '.':
                    target[c_idx] = 0
                elif(c == '#'):
                    target[c_idx] = 1

            target.pop(0)
            target.pop(-1)
                
            joltages = lineElements.pop(-1)

            targetLength = len(target)

            allowedMoves = []

            for e in lineElements:
                move = [0] * targetLength

                inLineMoves = list(map(int, re.findall(r'\d', e)))

                for idx in range(targetLength):
                    move[idx] = 1 if (idx in inLineMoves) else 0
                
                allowedMoves.append(move)

            # print(f'Target: {target}')
            # print(f'Moves: {allowedMoves}')
            # print(f'Joltages: {joltages}')
            # print()

            q = [[0] * len(target)]

            visited = []
            level = 0
            solution_find = False

            while q:
                level_size = len(q)

                # print(f"Processing Level {level}: {q}")

                for _ in range(level_size):
                    
                    curr = q.pop(0)

                    # print(curr, target, curr == target)

                    if(curr == target):
                        solution_find = True
                        break

                    for move in allowedMoves:
                        next_curr = XOR(curr, move)

                        if(next_curr not in visited):
                            visited.append(next_curr)
                            q.append(next_curr)

                if(solution_find): 
                    break

                level += 1

            # print(f"Result for target {target} is {level}")
            # print()
            result += level
    return result
                
def XOR(A: List, B: List) -> List:
    return [a ^ b for a,b in zip(A, B)]
                
if __name__ == "__main__":

    INPUT_FILENAME = "input.txt"
    ans = solve_from_file(INPUT_FILENAME)
    print(f"Solution is: {ans}")
