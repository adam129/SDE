import unittest
import two_sum


class TwoSumTesting(unittest.TestCase):

    def testSumIsPresent(self):
        array = [1,4,8,6]
        target = 10
        self.assertEqual(two_sum.findTwoSum(array, target), [1, 2])

    def testMoreThanOneSum(self):
        array = [1,9,6,4]
        target = 10
        self.assertEqual(two_sum.findTwoSum(array, target), 3)

    def testSumNotFound(self):
        array = [1, 2, 4, 8]
        target = 20
        self.assertEqual(two_sum.findTwoSum(array, target), 1)

    def testSumSameElement(self):
        array = [1, 3, 7, 7, 19]
        target = 14
        self.assertEqual(two_sum.findTwoSum(array, target), 2)

    def testArrayEmpty(self):
        array = []
        target = 14
        self.assertEqual(two_sum.findTwoSum(array, target), 4)


if __name__ == "__main__":
    unittest.main()