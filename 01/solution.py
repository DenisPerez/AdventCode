import os

def solve_dial_puzzle(file_path):
    DIAL_SIZE = 100
    password = 0
    current_position = 50
    
    print(f"--- Starting Dial Lock Solver ---")
    print(f"Initial position: {current_position}")
    
    with open(file_path, "r") as file:
        for line_number, line in enumerate(file, 1):
            line = line.strip()
            if not line:
                continue

            direction = line[0].upper()
            move_amount = int(line[1:])

            net_move = move_amount 
            
            step = 1 if direction == 'R' else -1
            
            for _ in range(move_amount):
                # Move the dial one step
                current_position = (current_position + step) % DIAL_SIZE
                
                # Check if the new position is 0
                if current_position == 0:
                    password += 1
                    
            # Print the result of the completed rotation
            print(f"Rotation {line_number}: {direction}{move_amount}")
            print(f"  -> Final Position: {current_position}")
            print(f"  -> Total Zeros Counted So Far: {password}")
    print(f"\n--- End of Rotations ---")
    print(f"The final password (total times dial pointed at 0) is: {password}")
    return password

input_file_path = "input.txt" 
final_password = solve_dial_puzzle(input_file_path)