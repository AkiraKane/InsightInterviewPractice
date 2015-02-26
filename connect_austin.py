

def is_leaf(node):
    return node.left is None and node.right is None


def funnel(left, right, first_pass=True):
    if left.next is None:
        print "{} next is: {}".format(left.val, right.val)
        left.next = right

    if is_leaf(left) or is_leaf(right):
        return

    if left.right and right.left:
        funnel(left.right, right.left, first_pass)

    if not first_pass:
        if left.left and right.left:
            funnel(left.left, right.left, first_pass)

        if left.right and right.right:
            funnel(left.right, right.right, first_pass)

        if left.left and right.right:
            funnel(left.left, right.right, first_pass)


def connect(root):
    """ Populating Next Right Pointers In Each Node """

    def build(root, first_pass=True):
        if not root or is_leaf(root):
            return

        if first_pass:
            if root.left and root.right:
                funnel(root.left, root.right, first_pass)
                build(root.left, first_pass)
                build(root.right, first_pass)
        else:
            if not root.left:
                build(root.right, first_pass)
            elif not root.right:
                build(root.left, first_pass)
            else:
                funnel(root.left, root.right, first_pass)
                build(root.left, first_pass)
                build(root.right, first_pass)

    build(root, True)
    build(root, False)



from DataStruct import TreeNode
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.left.left = TreeNode(8)
root.left.left.right = TreeNode(9)
#root.left.right.left = TreeNode(10)
#root.left.right.right = TreeNode(11)
root.right.left.left = TreeNode(12)
#root.right.left.right = TreeNode(13)
#root.right.right.left = TreeNode(14)
root.right.right.right = TreeNode(15)
connect(root)
print "level 1: val: {}".format(root.val)
print "       : next: {}\n".format(root.next)
print "level 2: val: {}".format([root.left.val,
                                 root.right.val])
print "       : next: {}\n".format([root.left.next.val,
                                    root.right.next])
print "level 3: val: {}".format([root.left.left.val,
                                 root.left.right.val,
                                 root.right.left.val,
                                 root.right.right.val])
print "       : next: {}\n".format([root.left.left.next.val,
                                    root.left.right.next.val,
                                    root.right.left.next.val,
                                    root.right.right.next])
print "level 4: val: {}".format([root.left.left.left.val,
                                 root.left.left.right.val,
                                 #root.left.right.left.val,
                                 #root.left.right.right.val,
                                 root.right.left.left.val,
                                 #root.right.left.right.val,
                                 #root.right.right.left.val,
                                 root.right.right.right.val])
print "       : next: {}\n".format([root.left.left.left.next.val,
                                    root.left.left.right.next.val,
                                    #root.left.right.left.next.val,
                                    #root.left.right.right.next.val,
                                    root.right.left.left.next.val,
                                    #root.right.left.right.next,
                                    #root.right.right.left.next.val,
                                    root.right.right.right.next])
