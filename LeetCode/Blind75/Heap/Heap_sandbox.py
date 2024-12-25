# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        return []

# Main function to run the test cases
if __name__ == '__main__':
    # Case 1
    root1 = [1,3,2,5,3,None,9]
    print("Case 1 Output:", Solution().largestValues(root1))  # Replace root1 with actual TreeNode structure

    # Case 2
    root2 = [1,2,3]
    print("Case 2 Output:", Solution().largestValues(root2))  # Replace root2 with actual TreeNode structure
