import os
from typing import List, Tuple, Dict
import re
import numpy as np
from z3 import *

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
            line = line.strip()
            if not line:
                continue
                
            lineElements = line.split()
            
            new_target = list(map(int, re.findall(r'\d+', lineElements[-1])))
            targetLength = len(new_target)
            
            # 2. Parse the button moves (the elements in the middle)
            button_elements = lineElements[1:-1]
            vs = []
            
            for element in button_elements:
                move = [0] * targetLength
                indices = list(map(int, re.findall(r'\d+', element)))
                for idx in indices:
                    if idx < targetLength:
                        move[idx] = 1
                vs.append(move)

            opt = Optimize()
            vv = []
            
            for i in range(len(vs)):
                v = Int(f"v_{i}")
                opt.add(v >= 0) 
                vv.append(v)

            for j in range(targetLength):
                column_sum = Sum([vs[i][j] * vv[i] for i in range(len(vs))])
                opt.add(column_sum == new_target[j])

            obj = Sum(vv)
            opt.minimize(obj)

            if opt.check() == sat:
                m = opt.model()
                current_line_total = 0
                for v in vv:
                    val = m[v]
                    if val is not None:
                        current_line_total += val.as_long()
                
                print(f"Solved line! Total presses for this machine: {current_line_total}")
                result += current_line_total
            else:
                print("No solution possible for this specific configuration.")
                
    return result
                
def largest_than_actual_target(target: List, current: List) -> bool:
    for t, c in zip(target, current):
        if(c > t):
            return True
    return False
                
if __name__ == "__main__":

    INPUT_FILENAME = "input.txt"
    ans = solve_from_file(INPUT_FILENAME)
    print(f"Solution is: {ans}")
