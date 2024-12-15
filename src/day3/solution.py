import re
from typing import List


def find_patterns(s: str) -> List[str]:

    pattern = r'mul\([0-9]{1,3}\,[0-9]{1,3}\)'

    return re.findall(pattern, s)

def find_regex_iter(s: str, pattern: str):
    return re.finditer(pattern, s)

def find_mults_iter(s: str):
    pattern = r'mul\([0-9]{1,3}\,[0-9]{1,3}\)|do\(\)|don\'t\(\)'
    return re.finditer(pattern, s)
    
def find_do_multipliers(s: str):
    pattern = r"do\(\)|don\'t\(\)"
    return re.finditer(pattern, s)

def perform_multiplications(mults: List[str]) -> int:
    total = 0
    for mult in mults:
        n1, n2 = mult.replace("mul", "").replace("(", "").replace(")", "").split(",")
        total += int(n1)*int(n2)

    return total



def parse_input(file_path: str) -> str:

    with open(file_path, 'r') as file:
        s = file.read()
        return re.sub(r'\n', '', s)


def part1():
    input_data = parse_input("data/day3.txt")
    found = find_patterns(input_data)
    return perform_multiplications(found)
    
def part2():
    input_data = parse_input("data/day3.txt")

    matches_all = find_regex_iter(input_data, r'mul\([0-9]{1,3}\,[0-9]{1,3}\)|do\(\)|don\'t\(\)')


    valid_mults = []
    is_most_recent_do = True

    for match in matches_all:
        val = match.group()
        if val.startswith("mul"):

            if is_most_recent_do:
                valid_mults.append(match.group())
            else:
                continue

        elif val == "do()":
            is_most_recent_do = True

        elif val == "don't()":
            is_most_recent_do = False

        else:
            print(f"WARN: Found weird group: {val}")

    return perform_multiplications(valid_mults)


if __name__ == "__main__":
    
    print(part1())
    print(part2())

