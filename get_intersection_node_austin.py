"""
>>> from DataStruct import Node
>>> headC = Node(4)
>>> headC.next = Node(5)
>>> headC.next.next = Node(6)
>>> headA = Node(2)
>>> headA.next = Node(3)
>>> headA.next.next = headC
>>> headB = Node(1)
>>> headB.next = Node(2)
>>> headB.next.next = Node(3)
>>> headB.next.next.next = headC
>>> intersectNode = get_intersection_node(headA, headB)
>>> print intersectNode.val
4
>>> headA.next.next = None
>>> intersectNode = get_intersection_node(headA, headB)
>>> print intersectNode
None
"""


def get_intersection_node(headA, headB):
    """ Intersection of Two Linked Lists """

    # scan through for intersection and length of each linked list
    cnt_a = 0
    cnt_b = 0
    node_a = headA
    node_b = headB

    while node_a or node_b:
        if node_a == node_b:
            return node_a

        if node_a:
            node_a = node_a.next
            cnt_a += 1

        if node_b:
            node_b = node_b.next
            cnt_b += 1

    a_leads_by = cnt_b - cnt_a

    # scan through for intersection by delaying the start through the
    # shorter linked list
    cnt_a = 0
    cnt_b = 0
    node_a = headA
    node_b = headB
    while node_a or node_b:
        if node_a == node_b:
            return node_a

        if a_leads_by > 0:
            # a leads b so have a wait
            if cnt_a >= a_leads_by and node_a:
                node_a = node_a.next

            if node_b:
                node_b = node_b.next

            cnt_a += 1
            cnt_b += 1

        else:
            # b leads a so have b wait
            if node_a:
                node_a = node_a.next

            if cnt_b >= -a_leads_by and node_b:
                node_b = node_b.next

            cnt_a += 1
            cnt_b += 1


if __name__ == "__main__":
    import doctest
    doctest.testmod()

