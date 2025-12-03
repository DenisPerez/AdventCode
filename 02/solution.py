import os

def is_invalid_id_part_two(n):
    s = str(n)
    length = len(s)

    if s[0] == '0':
        return False

    for L in range(1, length // 2 + 1):
        
        if length % L == 0:
            
            base_sequence = s[:L]
            
            repetition_count = length // L
            
            reconstructed_s = base_sequence * repetition_count
            
            if reconstructed_s == s:
                return True
                
    return False


def solve_gift_shop(puzzle_input):
    total_sum_of_invalid_ids = 0

    ranges = [r.strip() for r in puzzle_input.split(',')]
    
    for r in ranges:
        if not r:
            continue

        try:
            start_str, end_str = r.split('-')
            start_id = int(start_str)
            end_id = int(end_str)
        except ValueError:
            continue

        for current_id in range(start_id, end_id + 1):
            if is_invalid_id_part_two(current_id):
                total_sum_of_invalid_ids += current_id

    return total_sum_of_invalid_ids


def solve_from_file(filename="product_ids.txt"):
    with open(filename, 'r') as file:
        puzzle_input = file.read().strip()  

    final_sum = solve_gift_shop(puzzle_input)
    
    print(f"The sum of all invalid IDs is: {final_sum}")
if __name__ == "__main__":
    INPUT_FILENAME = "input.txt"
    
    solve_from_file(INPUT_FILENAME)