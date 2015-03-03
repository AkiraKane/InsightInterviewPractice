"""
>>> from DataStruct import Node
>>> head = Node(1)
>>> head.next = Node(2)
>>> head.next.next = Node(3)
>>> head.next.next.next = Node(4)
>>> head.next.next.next.next = Node(5)
>>> head = remove_nth_from_end(head, 5)
>>> print head.val, head.next.val, head.next.next.val, head.next.next.next.val
"""


def remove_nth_from_end(head, n):
    """ Remove Nth Node From the End of List """

    if head is None:
        return

    cnt = 0
    node_del = head
    node_search = head
    while node_search.next is not None:
        node_search = node_search.next
        if cnt == n:
            node_del = node_del.next
        else:
            cnt += 1

    if cnt == n:
        node_del.next = node_del.next.next
    else:
        head = head.next

    return head