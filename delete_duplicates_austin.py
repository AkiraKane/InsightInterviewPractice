"""
>>> from DataStruct import Node
>>> head = Node(1)
>>> head.next = Node(1)
>>> head.next.next = Node(2)
>>> head.next.next.next = Node(3)
>>> head.next.next.next.next = Node(3)
>>> head = delete_duplicates(head)
>>> print head.val, head.next.val, head.next.next.val, head.next.next.next
1 2 3 None
"""


def delete_duplicates(head):
    """ Remove Duplicates from Sorted List """

    if not head:
        return

    curr_head = head
    search = head
    while search:
        if curr_head.val != search.val:
            curr_head.next = search
            curr_head = search
        search = search.next

    curr_head.next = None
    return head