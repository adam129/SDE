def longestPalindromeFrom(s: str):
    longest_substring = ""

    for i in range(len(s)):
        # Odd number
        longest_substring = palindromeCheck(i, i, s, longest_substring)
        # Even number
        longest_substring = palindromeCheck(i, i + 1, s, longest_substring)

    return longest_substring


def palindromeCheck(start, end, string, substring):
    while start > 0 and end < len(string) and string[start] == string[end]:
        if len(string[start:end + 1]) > len(substring):
            substring = string[start:end + 1]
        start -= 1
        end += 1
    return substring


if __name__ == "__main__":
    string_to_test = "osdfkaposdfposadpaoooooooapkfodspfksdpopiiiiiiiifaskdpfodkfposadpooooooopfkosdfpksodfsd"
    print(longestPalindromeFrom(string_to_test))
