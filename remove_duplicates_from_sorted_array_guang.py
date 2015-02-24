def testRemoveDuplicates():
    case_1 = [1, 1, 4, 5, 6, 6, 6]
    case_2 = [3, 9, 10]
    assert removeDuplicates(case_1) == 4
    # assert case_1 == [1, 4, 5, 6]
    assert removeDuplicates(case_2) == 3
    # assert case_2 == [3, 9, 10]


def removeDuplicates(A):
    """
    for each element in the list do
        if the current element is the same as last element in new list
            do nothing
        else
            append the current element to new list
    """
    new_list = []
    for ind, val in enumerate(A):
        if ind == 0:
            new_list.append(val)
        if ind > 0:
            if val != new_list[-1]:
                new_list.append(val)
    print(new_list)
    return(len(new_list))


def betterRemoveDuplicates(A):
    """
    """


testRemoveDuplicates()
