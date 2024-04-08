import sys
import pytest

from src.solutions.word_search import Solution

class TestClass:

    basic_board_setup = None

    @classmethod
    def setup_class(cls):
        print("Setting up before running test file: " + str(__file__))
        
        cls.basic_board_setup = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]

    @classmethod
    def teardown_class(cls):
        print("Tearing down after running test file: " + str(__file__))

        cls.basic_board_setup = None

    def test_basic_word_search(self):
        solution_instance = Solution()

        board = self.basic_board_setup
        target = "ABCCE"

        answer = solution_instance.exist(board, target)

        assert answer == True
