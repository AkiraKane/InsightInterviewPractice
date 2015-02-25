class Solution:
    # @param root, a tree node
    # @return an integer

    def minDepth(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        elif root.right is None:
            return 1 + self.minDepth(root.left)
        elif root.left is None:
            return 1 + self.minDepth(root.right)
        else:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
