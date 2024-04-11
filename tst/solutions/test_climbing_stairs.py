from src.solutions.climbing_stairs import Solution

class TestClass:

    basic_num_stairs = None

    @classmethod
    def setup_class(cls):
        print("Setting up before running test file: " + str(__file__))

        cls.basic_num_stairs = [i for i in range(2,9)]

    @classmethod
    def teardown_class(cls):
        print("Tearing down after running test file: " + str(__file__))

        cls.basic_num_stairs = None

    def test_basic_count_starved_students(self):
        solution_instance = Solution()

        expectedAnswerList = [2,3,5,8,13,21,34]

        for i in range(len(self.basic_num_stairs)):
            num_ways = self.basic_num_stairs[i]
            actual = solution_instance.climbStairs(num_ways)
            assert expectedAnswerList[i] == actual
