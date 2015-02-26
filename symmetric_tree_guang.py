# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        """
        BFS: in each level, do comparison on the list of node values with its .reverse()
        """
        # special case of {}
        if root is None:
            return True

        reached_bottom = False
        current_nodes = [root]
        current_nodes_vals = [root.val]

        while reached_bottom is False:
            current_nodes_vals_reverse = current_nodes_vals[:]
            current_nodes_vals_reverse.reverse()
            if current_nodes_vals_reverse != current_nodes_vals:
                return False

            # update next nodes and vals
            next_nodes = []
            next_nodes_vals = []
            for node in current_nodes:
                if node.left is not None:
                    next_nodes.append(node.left)
                    next_nodes_vals.append(node.left.val)
                else:
                    next_nodes_vals.append(None)
                if node.right is not None:
                    next_nodes.append(node.right)
                    next_nodes_vals.append(node.right.val)
                else:
                    next_nodes_vals.append(None)
            current_nodes = next_nodes[:]
            current_nodes_vals = next_nodes_vals[:]
            if len(current_nodes) == 0:
                reached_bottom = True
        return True
