import sys

from leetcode.src.solutions.wordsearch import Solution


class TestClass:
    def __init__(self):
        self.basic_board_setup = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]

    def test_basic_word_search(self):
        solution_instance = Solution()
        print(solution_instance)

