"""
>>> from DataStruct import Node
>>> head = Node(1)
>>> head.append_data([2, 3, 4, 5, 6, 7])
>>> head.print_values()
1
2
3
4
5
6
7
>>> head = reverse_between(head, 1, 7)
>>> head.print_values()
7
6
5
4
3
2
1
"""


def reverse_between(head, m, n):
    """ Reverse Linked List II """

    if not head:
        return

    lag = n - m + 1

    if lag == 1:
        return head

    run_tail = head
    run_n = head
    while n > 0:
        run_n = run_n.next
        if n == m:
            run_tail = run_tail.next

        n -= 1

    run_m = run_tail.next

    for i in range(lag):

        temp_node = run_m.next
        run_m.next = run_n
        run_n = run_m
        if i == lag-1:
            break
        run_m = temp_node


    run_tail.next = run_m

    return head



