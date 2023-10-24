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


def leftSide(root_node, level):
    global max_level_left
    global left_outline_array

    if level == 0:
        if root_node is None:
            print("Binary tree is empty")
            return

        left_outline_array.append([level, root_node.data])

    if root_node is None:
        return

    if max_level_left < level:
        left_outline_array.append([level, root_node.data])
        max_level_left = level

    leftSide(root_node.left, level + 1)
    leftSide(root_node.right, level + 1)


def rightSide(root_node, level):
    global max_level_right

    if level == 0:
        if root_node is None:
            return

    if root_node is None:
        return

    if max_level_right < level:
        print([level, root_node.data])
        max_level_right = level

    rightSide(root_node.right, level + 1)
    rightSide(root_node.left, level + 1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root = Node(2)
    root.left = Node(7)
    root.right = Node(9)
    root.right.right = Node(11)
    root.right.right.left = Node(16)
    root.right.right.right = Node(19)

    left_outline_array = []
    max_level_left = 0
    leftSide(root, 0)

    for element in left_outline_array[::-1]:
        print(element)

    max_level_right = 0
    rightSide(root, 0)