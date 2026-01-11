import os
from typing import List, Tuple, Dict
import math

def writeToFile(outputFileName: str, lines: list, h: int, w: int):
    with open(outputFileName, 'w') as f:
        for row in range(h):
            for col in range(w):
                f.write(lines[row][col])
            f.write('\n')

def out_of_bounds(w, h, x, y):
    return x < 0 or x >= w or y < 0 or y >= h

def rectangle_area(p1, p2):
    return (abs(p2[0] - p1[0]) + 1) * (abs(p2[1] - p1[1]) + 1)

def is_inside(x, y, red_tiles):
    # Ray Casting Algorithm for Rectilinear Polygons
    inside = False
    for i in range(len(red_tiles)):
        p1 = red_tiles[i]
        p2 = red_tiles[(i + 1) % len(red_tiles)]
        
        # Check if point is ON an edge (important for rectangles touching the wall)
        if (p1[0] == p2[0] == x and min(p1[1], p2[1]) <= y <= max(p1[1], p2[1])) or \
           (p1[1] == p2[1] == y and min(p1[0], p2[0]) <= x <= max(p1[0], p2[0])):
            return True

        # Standard Ray Casting
        if ((p1[1] > y) != (p2[1] > y)) and \
           (x < (p2[0] - p1[0]) * (y - p1[1]) / (p2[1] - p1[1]) + p1[0]):
            inside = not inside
    return inside

def is_rectangle_valid(p1, p2, red_tiles):
    x_min, x_max = min(p1[0], p2[0]), max(p1[0], p2[0])
    y_min, y_max = min(p1[1], p2[1]), max(p1[1], p2[1])

    # 1. The center must be inside (to ensure the rectangle isn't entirely outside)
    if not is_inside((x_min + x_max) / 2, (y_min + y_max) / 2, red_tiles):
        return False

    # 2. No polygon segment can cross the INTERIOR of the rectangle
    for i in range(len(red_tiles)):
        v1 = red_tiles[i]
        v2 = red_tiles[(i + 1) % len(red_tiles)]
        
        # If it's a vertical polygon segment
        if v1[0] == v2[0]:
            vx = v1[0]
            vy_start, vy_end = min(v1[1], v2[1]), max(v1[1], v2[1])
            # Does this vertical line cut through the rectangle's x-range?
            if x_min < vx < x_max:
                # Does it overlap with the rectangle's y-range?
                if not (vy_end <= y_min or vy_start >= y_max):
                    return False
        
        # If it's a horizontal polygon segment
        elif v1[1] == v2[1]:
            vy = v1[1]
            vx_start, vx_end = min(v1[0], v2[0]), max(v1[0], v2[0])
            # Does this horizontal line cut through the rectangle's y-range?
            if y_min < vy < y_max:
                # Does it overlap with the rectangle's x-range?
                if not (vx_end <= x_min or vx_start >= x_max):
                    return False
                    
    return True

def solve_from_file(filename: str) -> int:
    red_tiles = []
    with open(filename, "r") as f:
        for line in f:
            if line.strip():
                red_tiles.append(tuple(map(int, line.strip().split(','))))

    max_area = 0

    for i in range(len(red_tiles)):
        for j in range(i + 1, len(red_tiles)):
            p1, p2 = red_tiles[i], red_tiles[j]
            
            area = (abs(p2[0] - p1[0]) + 1) * (abs(p2[1] - p1[1]) + 1)
            if area <= max_area:
                continue
                
            if is_rectangle_valid(p1, p2, red_tiles):
                max_area = area
                
    return max_area

if __name__ == "__main__":

    INPUT_FILENAME = "input.txt"
    ans = solve_from_file(INPUT_FILENAME)
    print(f"Solution is: {ans}")
