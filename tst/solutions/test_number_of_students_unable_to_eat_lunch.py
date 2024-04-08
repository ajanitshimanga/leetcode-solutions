from src.solutions.number_of_students_unable_to_eat_lunch import Solution

class TestClass:

    basic_students_setup = None
    basic_sandwiches_setup = None

    @classmethod
    def setup_class(cls):
        print("Setting up before running test file: " + str(__file__))
        
        cls.basic_students_setup = [[1,1,0,0], [1,1,1,0,0,1]]
        cls.basic_sandwiches_setup = [[0,1,0,1], [1,0,0,0,1,1]]

    @classmethod
    def teardown_class(cls):
        print("Tearing down after running test file: " + str(__file__))

        cls.basic_students_setup = None
        cls.basic_sandwiches_setup = None

    def test_basic_count_starved_students(self):
        solution_instance = Solution()

        expectedAnswerList = [0, 3]

        for i in range(len(self.basic_students_setup)):
            students = self.basic_students_setup[i]
            sandwiches = self.basic_sandwiches_setup[i]
            actual = solution_instance.countStudents(students, sandwiches)
            assert expectedAnswerList[i] == actual
