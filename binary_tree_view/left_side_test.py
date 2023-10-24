import unittest
from binary_tree_view import left_side_binary_tree as lf


class LeftSideTesting(unittest.TestCase):
    def test_binary_tree_null(self):
        self.assertIsNone(lf.leftSideView(None, 0))  # add assertion here

    def test_Nodes(self):
        root = lf.Node(1)
        root.left = lf.Node(2)
        root.right = lf.Node(3)
        root.right.right = lf.Node(4)
        self.assertIsNone(root.right.left)
        self.assertIsNone(root.left.right)


if __name__ == '__main__':
    unittest.main()
