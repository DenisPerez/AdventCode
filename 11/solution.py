import os
from typing import List, Tuple, Dict
from collections import deque

def writeToFile(outputFileName: str, lines: list, h: int, w: int):
    with open(outputFileName, 'w') as f:
        for row in range(h):
            for col in range(w):
                f.write(lines[row][col])
            f.write('\n')

def solve_from_file(filename: str) -> int:
    result = 0
    graph = {}
    start = 'svr'
    end = 'out'
    in_degree = {}
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
                
            node, adj = line.split(':')
            adj = list(adj.split())

            if node not in in_degree:
                in_degree[node] = 0

            for neighbor in adj:
                if neighbor not in in_degree:
                    in_degree[neighbor] = 0
                in_degree[neighbor] += 1
                if(neighbor not in graph):
                    graph[neighbor] = []

            graph[node] = adj
    
    ways = {}

    for node in in_degree.keys():
        ways[node] = {'none': 0, 'dac_only': 0, 'fft_only': 0, 'both': 0}

    ways[start]['none'] = 1

    queue = deque(d for d in graph if in_degree[d] == 0)

    while queue:

        node = queue.popleft()

        for neighbor in graph[node]:
            match neighbor:
                case 'dac':
                    ways[neighbor]['dac_only'] += ways[node]['none']
                    ways[neighbor]['dac_only'] += ways[node]['dac_only']
                    ways[neighbor]['both']     += ways[node]['fft_only']
                    ways[neighbor]['both']     += ways[node]['both']
                case 'fft':
                    ways[neighbor]['fft_only'] += ways[node]['none']
                    ways[neighbor]['fft_only'] += ways[node]['fft_only']
                    ways[neighbor]['both']     += ways[node]['dac_only']
                    ways[neighbor]['both']     += ways[node]['both']
                case _:
                    ways[neighbor]['none'] += ways[node]['none']
                    ways[neighbor]['dac_only'] += ways[node]['dac_only']
                    ways[neighbor]['fft_only'] += ways[node]['fft_only']
                    ways[neighbor]['both'] += ways[node]['both']
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return ways[end]['both']

if __name__ == "__main__":

    INPUT_FILENAME = "input.txt"
    ans = solve_from_file(INPUT_FILENAME)
    print(f"Solution is: {ans}")
