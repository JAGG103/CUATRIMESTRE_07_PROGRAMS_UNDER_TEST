def longest_common_subsequence(a, b):
    if not a or not b:
        return ''

    elif a[0] == b[0]:
        return a[0] + longest_common_subsequence(a[1:], b[1:])

    else:
        return max(
            longest_common_subsequence(a, b[1:]),
            longest_common_subsequence(a[1:], b),
            key=len
        )

# if __name__ == "__main__":
#     str1 = ["!", "P", "S", "A", ")", "r", "$", "~", "E", "{", "r"]
#     str1 = "".join(str1)
#     str2 = ["u", "k", "S", "A", ")", "r", "$", "~", "E", "{", "W"]
#     str2 = "".join(str2)
#     r = longest_common_subsequence(str1,str2)
#     print(r)
#     pass

"""
Longest Common Subsequence


Calculates the longest subsequence common to the two input strings. (A subsequence is any sequence of letters in the same order
they appear in the string, possibly skipping letters in between.)

Input:
    a: The first string to consider.
    b: The second string to consider.

Output:
    The longest string which is a subsequence of both strings. (If multiple subsequences of equal length exist, either is OK.)

Example:
    >>> longest_common_subsequence('headache', 'pentadactyl')
    'eadac'
"""
