import os
from typing import List

def solve_from_file(filename):

    operations = ['-', '+', '*', '/']
    operationList = []

    operands = []

    rightMostOperands = []

    solution = 0

    firstLine = True

    with open(filename, 'r') as file:
        lines = file.readlines()

        for idx in range(len(lines)):

            line = lines[idx].strip().split(' ')
            if(line[0] in operations):
                line = list(filter(None, line))
                idxp = 0
                elements = len(operands[0][0])

                for idxp in range(len(line)):
                    operands[idxp].append(line[idxp])
                break

            
            intLine = []

            for val in line:
                if(val.isdigit()):
                    intLine.append(val)

            for nIdx in range(len(intLine)):

                currentVal = intLine[nIdx]

                if(firstLine):
                    operands.append([[currentVal], len(currentVal)])
                    continue

                operands[nIdx][0].append(currentVal)
                operands[nIdx][1] = max(operands[nIdx][1], len(currentVal))
            if(idx == 0 and firstLine):
                firstLine = False

        print(operands)

        for problem in operands:
            solution += solve_from_problem(problem[0], problem[1], problem[2])

    print(f"Solution is: {solution}")

def solve_from_problem(operandList, maxLenght, operand):

    N = maxLenght if operand == '+' else maxLenght + 1
    startVal = 0 if operand == '+' else 1
    cutList = 1 if operand == '+' else -1
    solution = 0 if operand == '+' else 1
    extractedList = []

    for idx in range(startVal, N):

        extractedVal = ''

        for s in operandList:
            if((len(s) >= idx and operand == '*')
               or (len(s) > idx and operand == '+')):
                extractedVal += s[(cutList) * idx]
        extractedList.append(int(extractedVal))
        
        solution = solution + int(extractedVal) if operand == '+' else solution * int(extractedVal)
        print(extractedVal, solution)


    print(f'{extractedList} = {solution}')
    print(f'{'-' * 8}')
    return solution

if __name__ == "__main__":
    INPUT_FILENAME = "input.txt"

    solve_from_file(INPUT_FILENAME)