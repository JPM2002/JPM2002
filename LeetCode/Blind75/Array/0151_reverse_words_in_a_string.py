"""
Problem: Reverse Words in a String
===================================

Given an input string `s`, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in `s` will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that `s` may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

Examples:
---------

Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello world  "
Output: "world hello"

Example 3:
Input: s = "a good   example"
Output: "example good a"

Constraints:
------------
1. `1 <= s.length <= 10^4`
2. `s` contains English letters (upper-case and lower-case), digits, and spaces `' '`.
3. There is at least one word in `s`.

Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?
"""

"""
Thought Process:
1. Trim leading and trailing spaces from the input string manually.
2. Identify individual words manually by iterating through the string.
3. Reverse the list of words using a custom method.
4. Reconstruct the reversed string from the reversed list of words, ensuring there is only one space between words.

---------
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Approach:
        =========
        - Trim leading and trailing spaces manually.
        - Identify words manually by iterating through the string.
        - Reverse the identified words.
        - Reconstruct the string with a single space separating the words.

        Time Complexity: O(n) - Linear traversal of the string.
        Space Complexity: O(n) - Temporary storage for words and the final result.

        Parameters:
        -----------
        s : str
            The input string containing words and spaces.

        Returns:
        --------
        str
            A string of words in reverse order, separated by a single space.
        """
        space = " "
        for i in range(s):
            
            pass
        pass


# Main function to run the test cases
if __name__ == '__main__':
    # Example 1
    s1 = "the sky is blue"
    print("Example 1 Output:", Solution().reverseWords(s1))  # Expected: "blue is sky the"

    # Example 2
    s2 = "  hello world  "
    print("Example 2 Output:", Solution().reverseWords(s2))  # Expected: "world hello"

    # Example 3
    s3 = "a good   example"
    print("Example 3 Output:", Solution().reverseWords(s3))  # Expected: "example good a"

"""
Solution:
- Manually iterate through the string to extract words.
- Reverse the words and reconstruct the string with a single space separating them.
"""
