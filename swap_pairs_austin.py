"""
>>> from DataStruct import Node
>>> head = Node(1)
>>> head.next = Node(2)
>>> head.next.next = Node(3)
>>> head.next.next.next = Node(4)
>>> head.next.next.next.next = Node(5)
>>> head = swap_pairs(head)
>>> print head.val, head.next.val, head.next.next.val, head.next.next.next.val, head.next.next.next.next.val
2 1 4 3 5
"""


def swap_pairs(head):
    """ Swap Nodes in Pairs """

    if not head:
        return

    if head.next is None:
        return head

    curr_tail = head
    curr_head = curr_tail.next
    next_head = curr_head.next

    curr_head.next = curr_tail
    curr_tail.next = next_head
    prev_node = curr_tail

    head = curr_head
    print prev_node, prev_node.next

    while prev_node.next is not None and prev_node.next.next is not None:
        curr_tail = prev_node.next
        curr_head = curr_tail.next
        next_head = curr_head.next

        prev_node.next = curr_head

        curr_head.next = curr_tail
        curr_tail.next = next_head
        prev_node = curr_tail

    return head
