from graphviz import Digraph

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def visualize_tree(root):
    """
    Generate a visual representation of a binary tree using Graphviz.
    """
    def add_edges(graph, node, parent_name=None):
        if not node:
            return
        node_name = str(node.val)
        graph.node(node_name, str(node.val))
        if parent_name:
            graph.edge(parent_name, node_name)
        add_edges(graph, node.left, node_name)
        add_edges(graph, node.right, node_name)

    # Initialize the Digraph
    graph = Digraph()
    add_edges(graph, root)
    return graph

# Create the binary tree
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

# Visualize the tree
graph = visualize_tree(root)
graph.render("binary_tree", format="png", view=True)  # Save and open the tree diagram
