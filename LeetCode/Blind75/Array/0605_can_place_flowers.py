#TODO: Need to redo is

"""
Problem: Can Place Flowers
===========================

You have a long flowerbed in which some plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array `flowerbed` containing 0's and 1's, where `0` means empty and `1` means not empty, and an integer `n`, return `True` if `n` new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule, and `False` otherwise.

Examples:
---------

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False

Constraints:
------------
1. `1 <= flowerbed.length <= 2 * 10^4`
2. `flowerbed[i]` is `0` or `1`.
3. There are no two adjacent flowers in the initial `flowerbed`.
4. `0 <= n <= flowerbed.length`.
"""

"""
Thought Process:
- Traverse the flowerbed array.
- Check if a flower can be planted in each position based on its neighbors.
- Plant the flower if possible, decrease `n`, and ensure no rule is violated.
- Stop early if `n` reaches 0.
---------

"""

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True

        return n <= 0

        """
        Approach: Greedy Placement
        ==========================
        - Traverse the flowerbed list.
        - Identify empty spots (`0`) where flowers can be planted based on the rules.
        - Adjust `flowerbed` as flowers are planted, reducing `n` with each successful planting.
        - Return `True` if all `n` flowers can be planted, `False` otherwise.

        Parameters:
        -----------
        flowerbed : List[int]
            A list representing the flowerbed with `0` for empty and `1` for planted.
        n : int
            Number of flowers to plant.

        Returns:
        --------
        bool
            `True` if `n` flowers can be planted, `False` otherwise.
        """
        pass


# Main function to run the test cases
if __name__ == '__main__':
    # Example 1
    flowerbed1 = [1, 0, 0, 0, 1]
    n1 = 1
    print("Example 1 Output:", Solution().canPlaceFlowers(flowerbed1, n1))

    # Example 2
    flowerbed2 = [1, 0, 0, 0, 1]
    n2 = 2
    print("Example 2 Output:", Solution().canPlaceFlowers(flowerbed2, n2))

    # Example 3
    flowerbed3 = [0, 0, 1, 0, 0]
    n3 = 2
    print("Example 3 Output:", Solution().canPlaceFlowers(flowerbed3, n3))

"""
Solution:
- The logic involves iterating through the array and checking neighboring plots to determine if a flower can be planted without violating the rules.
- If all flowers are successfully planted, return True; otherwise, return False.
"""
