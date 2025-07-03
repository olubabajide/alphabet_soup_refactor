"""
Core functionality for the Alphabet Soup word-search solver.
"""
from typing import List, Tuple, Optional


def load_puzzle(filename: str) -> Tuple[List[List[str]], List[str]]:
    """
    Reads the input file and returns the character grid and list of words.

    :param filename: Path to the puzzle file
    :return: (grid, words)
    """
    with open(filename, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]

    rows, cols = map(int, lines[0].lower().split('x'))
    grid = [lines[i + 1].split() for i in range(rows)]
    words = lines[1 + rows:]
    return grid, words


def find_word(
    grid: List[List[str]], word: str
) -> Optional[Tuple[Tuple[int, int], Tuple[int, int]]]:
    """
    Finds `word` in `grid`, allowing horizontal, vertical, or diagonal,
    forwards or backwards.

    :param grid: 2D list of single-character strings
    :param word: Target word (spaces ignored)
    :return: ((start_row, start_col), (end_row, end_col)) or None
    """
    w = word.replace(' ', '')
    rows, cols = len(grid), len(grid[0])
    L = len(w)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]

    for forward in (True, False):
        pattern = w if forward else w[::-1]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != pattern[0]:
                    continue
                for dx, dy in directions:
                    end_i = i + dx * (L - 1)
                    end_j = j + dy * (L - 1)
                    if not (0 <= end_i < rows and 0 <= end_j < cols):
                        continue
                    if all(
                        grid[i + dx * k][j + dy * k] == pattern[k]
                        for k in range(L)
                    ):
                        return ((i, j), (end_i, end_j)) if forward else ((end_i, end_j), (i, j))
    return None