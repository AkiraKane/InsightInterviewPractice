"""
>>> from DataStruct import Node
>>> head = Node(1)
>>> head.next = Node(2)
>>> head.next.next = Node(3)
>>> head.next.next.next = Node(4)
>>> head.next.next.next.next = Node(5)
>>> head = rotate_right(head, 5)
>>> print head.val, head.next.val, head.next.next.val, head.next.next.next.val, head.next.next.next.next.val
"""


def rotate_right(head, k):
    if head is None:
        return

    node_tail = head
    node_new_tail = head
    cnt = 0
    len = 0

    while node_tail.next is not None:
        node_tail = node_tail.next
        if cnt == k:
            node_new_tail = node_new_tail.next
        else:
            cnt += 1
        len += 1

    if cnt != len:
        node_tail.next = head
        new_head = node_new_tail.next
        node_new_tail.next = None
        head = new_head

    return head