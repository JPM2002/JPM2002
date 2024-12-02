"""
Problem: Greatest Common Divisor of Strings
===========================================

For two strings `s` and `t`, we say "t divides s" if and only if `s = t + t + ... + t` (i.e., `t` is concatenated with itself one or more times).

Given two strings `str1` and `str2`, return the largest string `x` such that `x` divides both `str1` and `str2`.

Examples:
---------

Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Explanation: "ABC" divides both "ABCABC" and "ABC".

Example 2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Explanation: "AB" divides both "ABABAB" and "ABAB".

Example 3:
Input: str1 = "LEET", str2 = "CODE"
Output: ""
Explanation: There is no string that divides both "LEET" and "CODE".

Constraints:
------------
1. 1 <= str1.length, str2.length <= 1000
2. str1 and str2 consist of English uppercase letters.
"""

"""
Thought Process:
TODO - Add the thought process here

---------
"""

def gcd(a: int, b: int) -> int:
    """
    Helper function to calculate the Greatest Common Divisor (GCD) of two numbers using
    the Euclidean Algorithm.

    Parameters:
    -----------
    a : int
        First integer.
    b : int
        Second integer.

    Returns:
    --------
    int
        The greatest common divisor of a and b.
    """
    while b:
        a, b = b, a % b
    return a

def gcdOfStrings(str1: str, str2: str) -> str:
    """
    Approach: Greatest Common Divisor (GCD)
    ========================================
    If a string `x` is a divisor of both `str1` and `str2`, then `str1` and `str2` must be equal to 
    `x` repeated a certain number of times. The largest such string `x` is determined as follows:

    Steps:
    ------
    1. Check if `str1 + str2` is equal to `str2 + str1`. If not, return an empty string because
       the strings cannot share a common divisor.
    2. Find the greatest common divisor (GCD) of the lengths of `str1` and `str2`.
    3. Return the prefix of `str1` up to the GCD length as the GCD of the strings.

    Time Complexity: O(n + m) - Where n and m are the lengths of `str1` and `str2` respectively.
    Space Complexity: O(1) - Only a few variables are used.

    Parameters:
    -----------
    str1 : str
        The first input string.
    str2 : str
        The second input string.

    Returns:
    --------
    str
        The largest string that divides both `str1` and `str2`.
    """
    if str1 + str2 != str2 + str1:
        return ""
    gcd_length = gcd(len(str1), len(str2))
    return str1[:gcd_length]


# Main function to run the test cases
if __name__ == '__main__':
    # Example 1
    str1_1 = "ABCABC"
    str2_1 = "ABC"
    print("Example 1 Output:", gcdOfStrings(str1_1, str2_1))  # Expected: "ABC"

    # Example 2
    str1_2 = "ABABAB"
    str2_2 = "ABAB"
    print("Example 2 Output:", gcdOfStrings(str1_2, str2_2))  # Expected: "AB"

    # Example 3
    str1_3 = "LEET"
    str2_3 = "CODE"
    print("Example 3 Output:", gcdOfStrings(str1_3, str2_3))  # Expected: ""

"""
Solution:

# # If the concatenations str1 + str2 and str2 + str1 are not equal, there is no common divisor.
# if str1 + str2 != str2 + str1:
#     return ""

# # Find the GCD of the lengths of str1 and str2
# gcd_length = gcd(len(str1), len(str2))

# # Return the prefix of str1 up to the GCD length
# return str1[:gcd_length]
"""
