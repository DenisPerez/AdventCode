import os
from typing import List, Tuple, Dict
import math

def writeToFile(outputFileName: str, lines: list, h: int, w: int):
    with open(outputFileName, 'w') as f:
        for row in range(h):
            for col in range(w):
                f.write(lines[row][col])
            f.write('\n')

def distance(p1: tuple, p2: tuple) -> float:
    d = math.sqrt(math.pow(p1[0] - p2[0], 2) + 
                    math.pow(p1[1] - p2[1], 2) +
                    math.pow(p1[2] - p2[2], 2))
    
    return d

def find(parent:List, x:int) -> int:

    if(parent[x] != x):
        parent[x] = find(parent, parent[x])
        
    return parent[x]

def union(parent:List, x, y):
    parent[find(parent, y)] = find(parent, x)

def solve_from_file(filename: str) -> int:
    nodes = []

    with open(filename, "r") as f:

        fileLines = f.readlines()

        for idx in range(len(fileLines)):
            line = fileLines[idx].strip()

            line = tuple(map(int,line.split(',')))

            nodes.append(line)

    all_edges = []

    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            d = distance(nodes[i], nodes[j])
            edge = (d, i, j)
            all_edges.append(edge)

    all_edges.sort(key=lambda x : x[0])

    # for edge in all_edges:
    #     print(edge)

    parent = [x for x in range(len(nodes))]
    size = [1] * len(nodes)

    N = 1000
    K = 3

    successfull_merges = 0
    target_merges = len(nodes) - 1
    prod = 0
    
    for edge in all_edges:

        d, x, y = edge

        parent_x = find(parent, x)
        parent_y = find(parent, y)

        if(parent_x != parent_y):

            successfull_merges += 1

            union(parent, parent_x, parent_y)

            if(successfull_merges == target_merges):
                prod = nodes[x][0] * nodes[y][0]
                break

            # print(f"Union between ({x}, Coordinates: {nodes[x]}) and ({y}, Coordinates: {nodes[y]}), it: {i}")
            # print(parent)
            # print(size)
            # print(8*'-')

    size.sort(reverse=True)
    
    return prod

if __name__ == "__main__":

    INPUT_FILENAME = "input.txt"
    ans = solve_from_file(INPUT_FILENAME)
    print(f"Solution is: {ans}")
