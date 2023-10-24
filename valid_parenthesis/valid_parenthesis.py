class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        parentheses_hashmap = {")": "(",
                               "]": "[",
                               "}": "{"
                            }
        test_string = s[0]
        for index in range(1, len(s)):  # O(len(s))
            if s[index] not in parentheses_hashmap:
                test_string = test_string + s[index]
                continue
            elif test_string[len(test_string) - 1] == parentheses_hashmap[s[index]]:
                test_string = test_string[:len(test_string) - 1]
            else:
                return False

        if len(test_string) == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    solution = Solution()

    string = "([{}])"  # True
    print(solution.isValid(string))
