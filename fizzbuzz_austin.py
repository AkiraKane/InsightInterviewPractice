"""
>>> fizzbuzz(1, 17)
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz
16
"""


def fizzbuzz(start_idx, end_idx):
    """ Fizz Buzz """

    for val in range(start_idx, end_idx):
        if val % 3 == 0 and val % 5 == 0:
            print "fizzbuzz"
        elif val % 3 == 0:
            print "fizz"
        elif val % 5 == 0:
            print "buzz"
        else:
            print val

if __name__ == "__main__":
    import doctest
    doctest.testmod()


