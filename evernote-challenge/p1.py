"""
Problem Statement
=================

Implement a circular buffer of size N. Allow the caller to append, remove 
and list the contents of the buffer. Implement the buffer to achieve maximum
performance for each of the operations.

The new items are appended to the end and the order is retained i.e. elements 
are placed in increasing order of their insertion time. When the number of 
elements in the list elements exceeds the defined size, the older elements 
are overwritten.

There are four types of commands.

"A" n - Append the following n lines to the buffer. If the buffer is full 
        they replace the older entries.

"R" n - Remove first n elements of the buffer. These n elements are the ones
        that were added earliest among the current elements.

"L" - List the elements of buffer in order of their inserting time.

"Q" - Quit.

Your task is to execute commands on circular buffer.

Input format
============

First line of input contains N , the size of the buffer.

A n - append the following n lines to the buffer.

R n - remove first n elements of the buffer.

L - list the buffer.

Q - Quit.

Output format
=============

Whenever L command appears in the input, print the elements of buffer in order
of their inserting time. Element that was added first should appear first.

Sample Input
============

10
A 3
Fee
Fi
Fo
A 1
Fum
R 2
L
Q

Sample Output
=============

Fo
Fum

Constraints
===========
1. 0 <= N <= 10000
2. Number of removing elements will <= number of elements presents in circular 
   buffer.
3. Total number of commands <= 50000.
4. Total number of characters in input <= 20000000.

Notes
=====
* what does circular here mean? It simply means that if your buffer is full
  and you add more elements, the elements in the beginning will be replaced.
  BUT, when you remove elements, they will still be the earliest elements. i.e.
  you have to keep track of which element is the earliest one added, as well as
  the last one added. Because the last one added is the one that you will use
  to determine which elements to return.

* my first idea is to subclass deque. But does python stdlib provide other 
  stuff to create something custom?

* actually, a deque is exactly what solves this problem. A deque with maxlen

* should I read the entire input into a string or something, or should I 
  simply read 

"""

import unittest
from collections import deque 
class cbuffer(deque):
    """Specialized deque class for implementing circular buffer"""
    def __init__(self, iterable=None, maxlen=None):
        super(cbuffer, self).__init__(iterable, maxlen)

    @classmethod
    def readMax(cls, filename):
        """create the class using the input file.
        """
        with open(filename, 'r') as o:
            _maxlen = int(o.readline())
            if _maxlen < 0 or _maxlen > 10000:
                raise ValueError('maxlen outside defined range')
        return cls([], _maxlen) 

    def runFile(self, filename):
        with open(filename, 'r') as o:
            while True:
                line = o.readline()
                if line.strip() == 'Q':
                    return 
                elif line.split()[0] == 'A':
                    _numlines = int(line.split()[1])
                    for i in range(_numlines):
                        item = o.readline().strip()
                        self.append(item)
                elif line.split()[0] == 'R':
                    _numlines = int(line.split()[1])
                    for i in range(_numlines):
                        self.popleft()
                elif line.split()[0] == 'L':
                    for item in self:
                        print(item, end=' ')
                else:
                    pass


class TestBuffer(unittest.TestCase):
    """Tests for operations on the buffer"""

    def setUp(self):
        """"""
        self.maxlen = 10
        self.testarray = [
            "Hey!",
            "How's it",
            "going? Are you",
            "all right? doing",
            "ok?"
        ]
        self.testarray2 = [
            "ok?",
            "NO",
            "6",
            "7",
            "8",
            "9"
        ]
        self.testarray3 = [
            "Hey!",
            "How's it",
            "going? Are you",
            "all right? doing",
            "ok?",
            "NO",
            "6",
            "7",
            "8",
            "9"
        ]
        self.buf = cbuffer(self.testarray, self.maxlen)
        
    def test_buffer(self):
        # basic sanity tests for buffer
        self.assertEqual(self.buf.maxlen, self.maxlen)
        for i, item in enumerate(self.buf):
            self.assertEqual(self.testarray[i], item)
        self.assertEqual(self.buf.pop(), self.testarray[-1])
        self.buf.extend(self.testarray2)
        for i, item in enumerate(self.buf):
            self.assertEqual(self.testarray3[i], item)
        self.buf.append("more")
        self.assertEqual("more", self.buf[-1])
        self.assertEqual("How's it", self.buf[0])
        left_elem = self.buf.popleft()
        self.assertEqual(left_elem, "How's it")

        self.buf2 = cbuffer.readMax('p1-inp.txt')
        self.buf2.runFile('p1-inp.txt')

if __name__ == "__main__":
    #unittest.main()
    input_file = input()
    buf = cbuffer.readMax(input_file)
    buf.runFile(input_file)
