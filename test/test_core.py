

import pytest
from alphabet_soup.core import load_puzzle, find_word


def test_load_and_find(tmp_path):
    content = """
3x3
A B C
D E F
G H I
ABC
AEI
"""
    p = tmp_path / "puzzle.txt"
    p.write_text(content.strip())

    grid, words = load_puzzle(str(p))
    assert grid == [['A','B','C'], ['D','E','F'], ['G','H','I']]
    assert words == ['ABC', 'AEI']

    assert find_word(grid, 'ABC') == ((0, 0), (0, 2))
    assert find_word(grid, 'AEI') == ((0, 0), (2, 2))
