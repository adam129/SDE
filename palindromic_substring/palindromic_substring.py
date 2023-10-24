# Given a string s, return the longest palindromic substring in s.

# Any symbols, duplicated letters

def createHashmapFromString(string):
    letter_count = {}
    for letter in string.lower():
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1
    return letter_count


def showPalindromicFromLetters(string):
    half_palindrome = []
    dict_count_letters = createHashmapFromString(string)
    for key, value in dict_count_letters.items():
        if value < 2:
            continue
        if value % 2 == 1:
            value -= 1
        half_palindrome.extend([key] * int(value / 2))
    half_palindrome.extend(half_palindrome[::-1])
    print("".join(half_palindrome))


# def palindromeSubstring(string):
#     if len(string) % 2 == 0:
#         start, end = int(len(string)/2) - 1
#     else:
#         start, end = int(len(string) / 2 - 0.5)
#
#     while start > 0 and end < len(string):


if __name__ == "__main__":
    s = "salaaSa"
    showPalindromicFromLetters(s)
