"""
Problem: Reverse Vowels of a String
===================================

Given a string `s`, reverse only all the vowels in the string and return it.

The vowels are `'a', 'e', 'i', 'o', 'u'`, and they can appear in both lower and upper cases, more than once.

Examples:
---------

Example 1:
Input: s = "IceCreAm"
Output: "AceCreIm"
Explanation:
- The vowels in `s` are `['I', 'e', 'e', 'A']`.
- On reversing the vowels, `s` becomes "AceCreIm".

Example 2:
Input: s = "leetcode"
Output: "leotcede"

Constraints:
------------
1. `1 <= s.length <= 3 * 10^5`
2. `s` consists of printable ASCII characters.
"""

"""
Thought Process:
- Identify the positions of vowels in the string.
- Reverse the order of the vowels while keeping the rest of the characters unchanged.
- Use a two-pointer approach for efficiency:
  - Place one pointer at the beginning and another at the end of the string.
  - Move the pointers toward each other, swapping vowels as they are encountered.

---------
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        Approach: Two-Pointer Technique
        ===============================
        - Use two pointers, one starting at the beginning (`left`) and the other at the end (`right`) of the string.
        - Check if the character at each pointer is a vowel:
          - If both are vowels, swap them and move the pointers closer.
          - If only one is a vowel, move the non-vowel pointer toward the center.
        - Continue until the pointers meet.

        Time Complexity: O(n) - Each character is visited at most once.
        Space Complexity: O(n) - A new list is created to store the modified string.

        Parameters:
        -----------
        s : str
            The input string.

        Returns:
        --------
        str
            The string with vowels reversed.
        """
        vowels = set('aeiouAEIOU')  # Define vowels for quick lookup
        s_list = list(s)  # Convert string to list for mutable operations
        left, right = 0, len(s_list) - 1

        while left < right:
            # Move left pointer until a vowel is found
            while left < right and s_list[left] not in vowels:
                left += 1
            # Move right pointer until a vowel is found
            while left < right and s_list[right] not in vowels:
                right -= 1
            # Swap vowels
            if left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1

        return ''.join(s_list)  # Convert list back to string


# Main function to run the test cases
if __name__ == '__main__':
    # Example 1
    s1 = "IceCreAm"
    print("Example 1 Output:", Solution().reverseVowels(s1))  # Expected: "AceCreIm"

    # Example 2
    s2 = "leetcode"
    print("Example 2 Output:", Solution().reverseVowels(s2))  # Expected: "leotcede"

    # Example 3
    s3 = "aA"
    print("Example 3 Output:", Solution().reverseVowels(s3))  # Expected: "Aa"

"""
Solution:
- Use two pointers and a set of vowels for quick lookup.
- Iterate through the string and reverse vowels in place.
- Return the modified string.
"""
