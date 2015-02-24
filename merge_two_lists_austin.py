"""
>>> from DataStruct import Node
>>> l1 = Node(5)
>>> l1.next = Node(8)
>>> l2 = Node(2)
>>> l2.next = Node(4)
>>> l2.next.next = Node(6)
>>> l2.next.next.next = Node(7)
>>> l2.next.next.next.next = Node(9)
>>> l3 = merge_two_lists(l1, l2)
>>> for i in range(7):
...     print l3.val
...     l3 = l3.next
2
4
5
6
7
8
9
"""


def merge_two_lists(l1, l2):
    """ Merge Two Sorted Lists """

    if l1 is None and l2 is None:
        return
    elif l1 is None:
        head = l2
        return head
    elif l2 is None:
        head = l1
        return head

    if l1.val < l2.val:
        head = l1
        l1 = l1.next
    else:
        head = l2
        l2 = l2.next

    curr_head = head
    while l1 or l2:
        if l1 and l2:
            if l1.val < l2.val:
                curr_head.next = l1
                l1 = l1.next
            else:
                curr_head.next = l2
                l2 = l2.next
        elif l1 and l2 is None:
            curr_head.next = l1
            l1 = l1.next
        elif l2 and l1 is None:
            curr_head.next = l2
            l2 = l2.next

        curr_head = curr_head.next

    return head