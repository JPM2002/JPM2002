# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# from typing import List, Optional

# class Solution:
#     def largestValues(self, root: Optional[TreeNode]) -> List[int]:
#         return []

# # Main function to run the test cases
# if __name__ == '__main__':
#     # Case 1
#     root1 = [1,3,2,5,3,None,9]
#     print("Case 1 Output:", Solution().largestValues(root1))  # Replace root1 with actual TreeNode structure

#     # Case 2
#     root2 = [1,2,3]
#     print("Case 2 Output:", Solution().largestValues(root2))  # Replace root2 with actual TreeNode structure:

#----------------------------------------------------------------------------------------------



from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val # Node value
        self.left = left # Left child
        self.right = right # Right child

# 1. Creating a Single Node
# -------------------------
# Single node tree
root = TreeNode(1)
print("Root value:", root.val)  # Output: 1

# 2. Creating a Tree with a Root and Two Children
# -----------------------------------------------
# Tree structure:
#      1
#     / \
#    2   3

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print("Root value:", root.val)  # Output: 1
print("Left child:", root.left.val)  # Output: 2
print("Right child:", root.right.val)  # Output: 3

# 3. Traversing a Binary Tree (In-Order Traversal)
# ------------------------------------------------
# Tree structure:
#      1
#     / \
#    2   3

def in_order_traversal(node):
    """
    Perform in-order traversal (Left, Root, Right) on the binary tree.
    """
    if node is not None:
        in_order_traversal(node.left)
        print(node.val, end=" ")
        in_order_traversal(node.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print("\nIn-Order Traversal:")
in_order_traversal(root)  # Output: 2 1 3

# 4. Building a Complete Binary Tree and Finding the Maximum Value
# ----------------------------------------------------------------
# Tree structure:
#         4
#       /   \
#      2     7
#     / \   / \
#    1   3 6   9

def find_max_value(node):
    """
    Find the maximum value in a binary tree.
    """
    if node is None:
        return float('-inf')  # Return negative infinity for null nodes

    # Get the maximum value in the left and right subtrees
    left_max = find_max_value(node.left)
    right_max = find_max_value(node.right)

    # Return the maximum value among the current node and its subtrees
    return max(node.val, left_max, right_max) 

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

print("\nMaximum value in the tree:", find_max_value(root))  # Output: 9

# 5. Adding Nodes Dynamically and Level Order Traversal
# -----------------------------------------------------
# Dynamically add nodes to create a binary tree from a list
def build_tree_from_list(values):
    """
    Build a binary tree from a list of values.
    `None` indicates no child for the current node.
    """
    if not values:
        return None

    # Create the root of the tree
    root = TreeNode(values[0])
    queue = deque([root])  # Queue to manage tree nodes during construction
    i = 1  # Index to iterate through the list

    while queue and i < len(values):
        current = queue.popleft()  # Get the next node to populate children

        # Add the left child
        if values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        # Add the right child
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root

# Level order traversal
def level_order_traversal(root):
    """
    Perform level-order traversal (breadth-first search) on the binary tree.
    """
    if not root:
        return []

    queue = deque([root])  # Queue to manage nodes during traversal
    result = []  # List to store the traversal order

    while queue:
        current = queue.popleft()  # Get the next node from the queue
        result.append(current.val)  # Add the node's value to the result list

        # Add the left and right children to the queue if they exist
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return result

# Example usage of dynamic tree building and traversal
tree_values = [1, 2, 3, 4, 5, None, 6]  # List representation of a binary tree
root = build_tree_from_list(tree_values)  # Build the binary tree

print("\nLevel Order Traversal:", level_order_traversal(root))  # Output: [1, 2, 3, 4, 5, 6]

