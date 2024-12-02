"""
Problem: Kids With the Greatest Number of Candies
=================================================

There are `n` kids with candies. You are given an integer array `candies`, where each `candies[i]` represents the number of candies the `i`th kid has, and an integer `extraCandies`, denoting the number of extra candies that you have.

Return a boolean array `result` of length `n`, where `result[i]` is `True` if, after giving the `i`th kid all the `extraCandies`, they will have the greatest number of candies among all the kids, or `False` otherwise.

Note that multiple kids can have the greatest number of candies.

Examples:
---------

Example 1:
Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [True,True,True,False,True] 
Explanation:
- If you give all `extraCandies` to Kid 1, they will have `2 + 3 = 5` candies, which is the greatest among the kids.
- If you give all `extraCandies` to Kid 2, they will have `3 + 3 = 6` candies, which is the greatest among the kids.
- If you give all `extraCandies` to Kid 3, they will have `5 + 3 = 8` candies, which is the greatest among the kids.
- If you give all `extraCandies` to Kid 4, they will have `1 + 3 = 4` candies, which is not the greatest among the kids.
- If you give all `extraCandies` to Kid 5, they will have `3 + 3 = 6` candies, which is the greatest among the kids.

Example 2:
Input: candies = [4,2,1,1,2], extraCandies = 1
Output: [True,False,False,False,False] 
Explanation: 
- Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.

Example 3:
Input: candies = [12,1,12], extraCandies = 10
Output: [True,False,True]

Constraints:
------------
1. `n == candies.length`
2. `2 <= n <= 100`
3. `1 <= candies[i] <= 100`
4. `1 <= extraCandies <= 50`
"""

"""
Thought Process:
TODO - Add the thought process here

---------
"""

def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    """
    Approach: Simple Comparison
    ============================
    For each kid, check if their candies plus the `extraCandies` is greater than or equal to the maximum candies any kid currently has. If it is, the result for that kid is `True`, otherwise it is `False`.

    Steps:
    ------
    1. Determine the maximum number of candies any kid currently has.
    2. For each kid, calculate the total candies they would have if given all `extraCandies`.
    3. Compare this total to the maximum number of candies.
    4. Append `True` to the result if the total is greater than or equal to the maximum, otherwise append `False`.

    Time Complexity: O(n) - We iterate through the list of candies twice: once to find the maximum and once to compute the results.
    Space Complexity: O(n) - The output list `result` has the same size as the input list `candies`.

    Parameters:
    -----------
    candies : List[int]
        The list of integers representing the number of candies each kid has.
    extraCandies : int
        The number of extra candies available.

    Returns:
    --------
    List[bool]
        A boolean list where `result[i]` is `True` if the `i`th kid can have the greatest number of candies, or `False` otherwise.
    """
    # Start your implementation here:
    # max_number = []
    # max_base = max(candies)
    # for candy in candies:
    #     new_max = candy + extraCandies
    #     if new_max >= max_base:
    #         max_number.append(True)
    #     else:
    #         max_number.append(False)
    # return max_number


    # Better Implementation

    # maxCandies = max(candies)
    # return [ curnum + extraCandies >= maxCandies for curnum in candies]





# Main function to run the test cases
if __name__ == '__main__':
    # Example 1
    candies1 = [2, 3, 5, 1, 3]
    extraCandies1 = 3
    print("Example 1 Output:", kidsWithCandies(candies1, extraCandies1))  # Expected: [True, True, True, False, True]

    # Example 2
    candies2 = [4, 2, 1, 1, 2]
    extraCandies2 = 1
    print("Example 2 Output:", kidsWithCandies(candies2, extraCandies2))  # Expected: [True, False, False, False, False]

    # Example 3
    candies3 = [12, 1, 12]
    extraCandies3 = 10
    print("Example 3 Output:", kidsWithCandies(candies3, extraCandies3))  # Expected: [True, False, True]

"""
Solution:

# max_candies = max(candies)

# result = []
# for candy in candies:
#     result.append(candy + extraCandies >= max_candies)

# return result
"""
