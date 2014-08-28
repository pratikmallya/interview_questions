"""
Jumble Sort:

Given an array of mixed integers and strings, sort the array, so that the
strings and integers remain in the same relative place (i.e. if the first
element of array was int, it will remain int. But, it will be sorted, so
it will be the smallest int).
e.g.
input = "2 3 10 dehra dun apple wookie 78 9"
output = [2, 3, 9, 'apple', 'dehra', 'dun', 'wookie', 10, 78]

"""
import unittest


class TestAlg(unittest.TestCase):
    def test_basics(self):
        arr = "2 3 10 dehra dun apple wookie 78 9"
        res = jumble_sort(arr)
        self.assertEqual(
            res,
            [2, 3, 9, 'apple', 'dehra', 'dun', 'wookie', 10, 78]
        )


def jumble_sort(arr):
    arr = arr.strip().split()
    int_ind = list(map(is_int, arr))
    int_arr = [int(item) for item in arr if is_int(item)]
    char_arr = [item for item in arr if not is_int(item)]

    int_arr.sort(reverse=True)
    char_arr.sort(reverse=True)

    for i, item in enumerate(int_ind):
        if item:
            int_ind[i] = int_arr.pop()
        else:
            int_ind[i] = char_arr.pop()

    return int_ind


def is_int(item):
    try:
        int(item)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    unittest.main()
