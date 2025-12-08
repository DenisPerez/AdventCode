import os
from typing import List

def writeToFile(outputFileName: str, lines: list, h: int, w: int):
    with open(outputFileName, 'w') as f:
        for row in range(h):
            for col in range(w):
                f.write(lines[row][col])
            f.write('\n')

def solve_from_file(filename: str) -> int:
    totalSplits = 0
    lines = []
    Spos = (-1,-1)

    with open(filename, "r") as f:

        fileLines = f.readlines()

        for idx in range(len(fileLines)):
            line = fileLines[idx].strip()

            if(line == ""):
                continue

            splitedLine = list(line)

            lines.append(splitedLine)

            if('S' in splitedLine):
                Spos = (idx, splitedLine.index('S'))

    w, h = max(len(line) for line in lines), len(lines)

    queue = [(Spos[0] + 1, Spos[1])]

    while len(queue) > 0:

        currentPair = queue.pop()
        currentR, currentC = currentPair[0], currentPair[1]

        if(inBound(currentR, currentC, w, h)):

            nextRPosition, nextCPosition = currentR + 1, currentC

            if(inBound(nextRPosition, nextCPosition, w, h)):
                nextValue = lines[nextRPosition][nextCPosition]

                if(nextValue == '^'):
                    queue.append((nextRPosition, nextCPosition - 1))
                    queue.append((nextRPosition, nextCPosition + 1))
                    totalSplits += 1
                elif (nextValue == '.'):
                    queue.append((nextRPosition, nextCPosition))
                lines[currentR][currentC] = '|'

    writeToFile('output.txt', lines, h, w)

    return totalSplits

def inBound(row, column, w, h) -> bool:
    return not(row < 0 or row > w or column < 0 or column > h) 

if __name__ == "__main__":
    INPUT_FILENAME = "input.txt"
    ans = solve_from_file(INPUT_FILENAME)
    print(f"Solution is: {ans}")
