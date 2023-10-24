import valid_parenthesis
import unittest


class ValidParenthesisTesting(unittest.TestCase):

    def testOrderedParenthesis(self):
        solution = valid_parenthesis.Solution()
        string = "([{}])"  # True
        self.assertEqual(solution.isValid(string), True)
        string = "()[]"  # True
        self.assertEqual(solution.isValid(string), True)
        string = "{()[]}"  # True
        self.assertEqual(solution.isValid(string), True)

    def testUnOrderedParenthesis(self):
        solution = valid_parenthesis.Solution()
        string = "()[]{"  # Fail
        self.assertEqual(solution.isValid(string), False)
        string = "}()[]{"  # Fail
        self.assertEqual(solution.isValid(string), False)


if __name__ == "__main__":
    unittest.main()



