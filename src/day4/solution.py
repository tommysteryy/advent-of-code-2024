from typing import List



def parse_input(path: str) -> List[List[str]]:

    list_of_lines = []

    # Open the file in read mode
    with open(path, 'r') as file:
        # Read each line in the file
        for line in file:
            # Print each line
            list_of_lines.append([c for c in line.strip()])

    return list_of_lines

def part1(grid: List[List[str]]):
    
    NROWS = len(grid)
    NCOLS = len(grid[0])

    def can_find(word: str, r: int, c: int, dr: int, dc: int) -> bool:

        if r in range(NROWS) and c in range(NCOLS):

            if len(word) == 1:
                if grid[r][c] == word:
                    return True
                else:
                    return False
            
            else:
                if grid[r][c] != word[0]:
                    return False
                else:
                    return can_find(word[1:], r+dr, c+dc, dr, dc)
                
        else:
            return False
    
    def words_found(r: int, c: int, word: str) -> int:

        directions = [
            [0, 1],     # right
            [0, -1],    # left
            [1, 0],     # down
            [-1, 0],    # up
            [1, 1],     # diag-down-right
            [1, -1],    # diag-down-left
            [-1, 1],    # diag-up-right
            [-1, -1]    # diag-up-left
        ]

        total = 0
        for dr, dc in directions:
            if can_find(word, r, c, dr, dc):
                total += 1

        return total


    result = 0
    for r in range(NROWS):
        for c in range(NCOLS):
            result += words_found(r, c, "XMAS")

    return result


def part2(grid: List[List[str]]):

    NROWS = len(grid)
    NCOLS = len(grid[0])

    def diagonal_is_m_and_s(r: int, c: int) -> bool:

        # the center "A" could only be one row from all edges
        if r in range(1, NROWS-1) and c in range(1, NCOLS-1):
            
            # Backslash direction:
            if (grid[r-1][c-1] + grid[r+1][c+1]) == "MS" or (grid[r-1][c-1] + grid[r+1][c+1]) == "SM":
                
                # forward slash directin:
                if (grid[r+1][c-1] + grid[r-1][c+1]) == "MS" or (grid[r+1][c-1] + grid[r-1][c+1]) == "SM":

                    return True
            

    def found_x_mas(r: int, c: int) -> bool:

        if r in range(NROWS) and c in range(NCOLS):

            if grid[r][c] == "A" and diagonal_is_m_and_s(r, c):

                return True

    count = 0
    for r in range(NROWS):
        for c in range(NCOLS):
            if found_x_mas(r, c):
                count += 1

    return count


    


if __name__ == "__main__":
    # Make this global so it's easier to access
    grid = parse_input("data/day4.txt")
    print(part1(grid))
    print(part2(grid))

