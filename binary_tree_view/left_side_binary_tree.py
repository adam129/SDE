# Given a binary tree, print the left view (the tree saw from the left prospective)
# --> view
# L0               *2
# L1            *7       9
# L2                       *11
# L3                   *16      19

class Node:

    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def leftSideView(root_node, level):
    global max_level

    if level == 0:
        if root_node is None:
            print("Binary tree is empty")
            return None

        print("Level {0} , node: {1}".format(level, root_node.data))

    if root_node is None:
        return

    if max_level < level:
        print("Level {0} , node: {1}".format(level, root_node.data))
        max_level = level

    leftSideView(root_node.left, level + 1)
    leftSideView(root_node.right, level + 1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = Node(2)
    root.left = Node(7)
    root.right = Node(9)
    root.right.right = Node(11)
    root.right.right.left = Node(16)
    root.right.right.right = Node(19)

    max_level = 0
    leftSideView(root, 0)





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
