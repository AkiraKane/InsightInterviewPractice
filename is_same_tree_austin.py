"""
>>> from DataStruct import TreeNode
>>> p = TreeNode(3)
>>> p.left = TreeNode(9)
>>> p.right = TreeNode(20, left=TreeNode(15), right=TreeNode(7))
>>> q = TreeNode(3)
>>> q.left = TreeNode(9)
>>> q.right = TreeNode(20, left=TreeNode(15), right=TreeNode(7))
>>> is_same_tree(p, q)
True
>>> q = TreeNode(3)
>>> q.left = TreeNode(2)
>>> q.right = TreeNode(20, left=TreeNode(15), right=TreeNode(7))
>>> is_same_tree(p, q)
False
>>> q = TreeNode(3)
>>> q.left = TreeNode(9)
>>> q.right = TreeNode(20, left=TreeNode(15))
>>> is_same_tree(p, q)
False
"""


def is_same_tree(p, q):
    """ Same Tree """

    if not p and not q:
        return True
    else:
        if p and q:
            if p.val != q.val:
                return False
            else:
                return is_same_tree(p.left, q.left) and \
                       is_same_tree(p.right, q.right)
        else:
            return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()