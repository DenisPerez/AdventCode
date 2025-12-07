import os
from typing import List

def solve_from_file(filename):

    idsList = []
    ingredients = []

    solution = 0

    with open(filename, 'r') as file:
        lines = file.readlines()
        ingIdx = 0

        for idx in range(len(lines)):

            if(lines[idx] == '\n'):
                ingIdx = idx + 1
                break

            line = lines[idx].strip('\n')
            
            idRange = tuple(map(int, line.split('-')))

            Insert_Sorted(idsList, idRange)

        for igIdx in range(ingIdx, len(lines)):
            line = lines[igIdx].strip('\n')
            ingredients.append(int(line))

    merged_List = Merge_Intervals(idsList)

    for idMerge in merged_List:
        solution += (idMerge[1] - idMerge[0] + 1)
    

    # for ingredient in ingredients:
    #     for idRange in merged_List:
    #         if(idRange[0] <= ingredient <= idRange[1]):
    #             print(f"Ingredient {ingredient} is fresh because it falls into range {idRange}")
    #             solution += 1
    #             break

    # print(f"IDs List: {idsList}")
    # print(f"Ingredients: {ingredients}")
    # print(f"Merged List: {merged_List}")

    print(f"Solution is: {solution}")

def Insert_Sorted(idsList, idRange):
    N = len(idsList) - 1

    for idx in range(N, -1, -1):
        currentRange = idsList[idx]

        if(idRange[0] >= currentRange[0]):
            idsList.insert(idx + 1, idRange)
            return
    
    idsList.insert(0, idRange)

def Merge_Intervals(idsList) -> List[tuple]:
    N = len(idsList)

    if(N <= 1):
        return

    mergedList = []
    currentRange = idsList[0]

    for idx in range(1, N):
        nextRange = idsList[idx]

        if(currentRange[1] >= nextRange[0]):
            currentRange = (currentRange[0], max(currentRange[1], nextRange[1]))
        else:
            mergedList.append(currentRange)
            currentRange = nextRange

    mergedList.append(currentRange)

    return mergedList

if __name__ == "__main__":
    INPUT_FILENAME = "input.txt"

    solve_from_file(INPUT_FILENAME)