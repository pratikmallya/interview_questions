"""
Filesystem path normalization

e.g: /usr/local/lib/../foo/./bar.so -> /usr/local/foo/bar.so
"""
import unittest
from functools import reduce


class TestAlg(unittest.TestCase):
    def test_case_1(self):
        string = " /usr/local/lib/../foo/./bar.so"
        self.assertEqual(
            norm_filepath(string), "/usr/local/foo/bar.so")
        self.assertEqual(
            norm_filepath("../../../"), None)
        self.assertEqual(
            norm_filepath("/usr/../../../"), None)
        self.assertEqual(
            norm_filepath("usr/local/lib/"), None)


def norm_filepath(filepath):
    tokens = filepath.strip().split('/')
    res = []

    if tokens[0] != '':
        return None

    for item in tokens:
        if item == '..':
            try:
                res.pop()
            except IndexError:
                return None
        elif item == '.':
            pass
        else:
            res.append(item)

    res = reduce(lambda x, y: x + '/' + y, res)
    return res

if __name__ == "__main__":
    unittest.main()
