from typing import List
import sys


def is_safe(level: List[int], decreasing: bool) -> bool:

    if len(level) <= 1:
        return True
    else:
        curr_diff = level[0] - level[1]

        # The changes between entries must be at least 1, at most 3
        if abs(curr_diff) > 3 or abs(curr_diff) < 1:
            return False
        
        if decreasing and curr_diff < 0:
            return False
    
        if not decreasing and curr_diff > 0:
            return False
        
        return is_safe(level[1:], decreasing)
    
    # 1 2 7 8 9
def is_safe_w_tolerance(level: List[int], decreasing: bool, tolerance: int) -> bool:

    # if tolerance < 0:
    #     return False

    if len(level) <= 2:
        return True
    else:
        curr_diff = level[0] - level[1]

        # Global bool that tracks if something is wrong
        has_fault = False

        # The changes between entries must be at least 1, at most 3
        if abs(curr_diff) > 3 or abs(curr_diff) < 1:
            has_fault = True
        
        if decreasing and curr_diff < 0:
            has_fault = True
    
        if not decreasing and curr_diff > 0:
            has_fault = True

        if has_fault:
            if tolerance == 0:
                return False
            else:
                return is_safe_w_tolerance(level[1:], decreasing, tolerance=tolerance-1) or is_safe_w_tolerance([level[0]] + level[2:], decreasing, tolerance-1)
        else:
            return is_safe_w_tolerance(level[1:], decreasing, tolerance=tolerance)

def parse_input_file(file_path):
    result = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                nums = [int(num) for num in line.split()]
                result.append(nums)
    return result


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python solution.py <input-file>")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        levels = parse_input_file(input_file)
    except Exception as e:
        print(f"Error reading input file: {e}")
        sys.exit(1)

    # First question
    total_first = 0
    for level in levels:
        if is_safe(level, decreasing=True) or is_safe(level, decreasing=False):
            total_first += 1

    # Second question
    total_second = 0
    for level in levels:
        if is_safe_w_tolerance(level, decreasing=True, tolerance=1) or is_safe_w_tolerance(level, decreasing=False, tolerance=1):
            total_second += 1
    
    print(f"Q1: Total safe levels: {total_first}")
    print(f"Q2: Total safe levels: {total_second}")