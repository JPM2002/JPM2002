"""
Problem: Find Largest Value in Each Tree Row
===========================================

Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

Examples:
---------

Example 1:
Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]

Example 2:
Input: root = [1,2,3]
Output: [1,3]

Constraints:
------------
1. The number of nodes in the tree will be in the range [0, 10^4].
2. -2^31 <= Node.val <= 2^31 - 1
"""

"""
Thought Process:
TODO - Add the thought process here


---------
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        """
        Approach: Level Order Traversal
        ===============================
        This approach uses a queue to traverse each level of the binary tree and find the maximum value at each level.

        Steps:
        ------
        1. Initialize an empty queue and add the root node to it.
        2. For each level, iterate through all nodes at that level:
            a. Track the maximum value encountered.
            b. Add the left and right children of the current node to the queue.
        3. Append the maximum value for the current level to the result list.
        4. Repeat until all levels are processed or the tree is empty.
        5. Return the result list.

        Time Complexity: O(n) - Each node is visited once.
        Space Complexity: O(n) - The queue stores nodes at each level.

        Parameters:
        -----------
        root : Optional[TreeNode]
            The root node of the binary tree.

        Returns:
        --------
        List[int]
            A list of the largest values in each tree row.
        """
        # Start your implementation here:

        return []

# Main function to run the test cases
if __name__ == '__main__':
    # Case 1
    root1 = [1,3,2,5,3,None,9]
    print("Case 1 Output:", Solution().largestValues(root1))  # Expected: [1, 3, 9]

    # Case 2
    root2 = [1,2,3]
    print("Case 2 Output:", Solution().largestValues(root2))  # Expected: [1, 3]

"""
Solution:
TODO - Add the solution implementation here
"""
