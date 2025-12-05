import os

def solve_from_file(filename="product_ids.txt"):

    matrix = []
    solution = 0

    with open(filename, 'r') as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip('\n')
            
            characters = list(line.split())

            matrix.append(characters)
    
    finalMatrix = []

    iterSolution = 1
    debugIdx = 0

    while iterSolution > 0:

        iterSolution = 0

        for row in range(len(matrix)):
            charString = matrix[row][0]
            finalRow = ''
            for col in range(len(charString)):
                c = matrix[row][0][col]
                if c == '.' or c == 'X':
                    finalRow += c
                    continue

                startSquare = (row - 1, col - 1)

                roolsOfPapers = 0

                for i in range(startSquare[0], startSquare[0] + 3):
                    for j in range(startSquare[1], startSquare[1] + 3):
                        if i == row and j == col:
                            continue
                        
                        newRow = i
                        newCol = j

                        if newRow < 0 or newRow >= len(matrix) or newCol < 0 or newCol >= len(matrix[newRow][0]):
                            continue
                        
                        if matrix[newRow][0][newCol] == '@':
                            roolsOfPapers += 1
                        
                if(roolsOfPapers < 4):
                    iterSolution += 1
                    finalRow += 'X'
                else:
                    finalRow += c
            finalMatrix.append([finalRow])
        
        solution += iterSolution
        matrix = finalMatrix.copy()
        finalMatrix = []

        # print(f"Iteration{'-'*8}")

        # print(iterSolution)
        # for i in range(len(finalMatrix)):
        #     for j in range(len(finalMatrix[i])):
        #         print(finalMatrix[i][j], end='')
        #     print() 

        # print(f"Ending iteration{'-'*8}")

    with open("output.txt", 'w') as outputFile:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                outputFile.write(matrix[i][j])
            outputFile.write('\n')

    print(f"Solution is: {solution}")

    
if __name__ == "__main__":
    INPUT_FILENAME = "input.txt"

    solve_from_file(INPUT_FILENAME)