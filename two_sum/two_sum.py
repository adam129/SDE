# Given an array of integers nums and an integer target, return indices of the two numbers
# such that they add up to target.
#
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
#
# You can return the answer in any order.

def findTwoSum(array, target):
    '''
    Function that takes as input an int array and a target value and checks
    if the sum of two elements in the array is equal to the target value and print their index.

    If more than two elements are equal to the target, don't print their index.

    :param array:
    :param target:
    :return:
    '''
    if len(array) < 1:
        print("Array empty")
        return 4

    array.sort()
    start_target = end_target = None
    start = 0
    end = len(array) - 1
    while start < end:
        if array[start] + array[end] == target:
            if array[start] == array[end]:
                print("Same elements.")
                return 2
            else:
                if start_target is None:
                    start_target = start
                    end_target = end
                    start += 1
                    end -= 1
                else:
                    print("More than one solution found.")
                    return 3

        elif array[start] + array[end] > target:
            end -= 1
        else:
            start += 1

    if start >= end and start_target is not None:
        print("Index of the values are: {0} and {1}".format(start_target, end_target))
        return [start_target, end_target]
    else:
        print("Pair not found")
        return 1


if __name__ == '__main__':
    target_sum = 11
    num_array = [1, 4, 6, 9, 8, 12, 5]
    findTwoSum(num_array, target_sum)

