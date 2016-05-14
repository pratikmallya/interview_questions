"""
Problem: A certain event is recorded by a function record_hit. We wish
to have a function get_hits that will get all the hits recorded in the past
5 minutes, accurate to the second. Write both record_hit and get_hits.

Answer: The key to the solution is the statement "accurate to the second".
This allows us to group all events that occur within a second into one bin.
Another key is the limited window: we are only interested in the events
that occur in the past 300 seconds. If we use a bin, its size would be 300
and its count would contain the number of hits.
"""
import time
from collections import defaultdict
import unittest

hits = defaultdict(int)


class TestGetHits(unittest.TestCase):

    def test_in_window(self):
        hits = defaultdict(int)
        record_hit(1)
        record_hit(1)
        record_hit(1)

        self.assertEqual(get_hits(20), 3)

    def test_outside_window(self):
        hits = defaultdict(int)
        record_hit(1)
        record_hit(1)
        record_hit(1)

        self.assertEqual(get_hits(305), 0)


def record_hit(time_t=None):
    if time_t is None:
        time_t = int(time.time())
    else:
        time_t = int(time_t)

    hits[time_t] += 1
    # clean up
    for key in hits.keys():
        if time_t - key > 300:
            del hits[key]


def get_hits(time_t=None):
    """Returns the number of times that record_hit was called
       in the last 5 minutes, accurate to the second"""
    if time_t is None:
        time_t = int(time.time())
    else:
        time_t = int(time_t)

    count = 0

    for key in hits.keys():
        if time_t - key < 300:
            count += hits[key]
        else:
            del hits[key]
    return count

if __name__ == "__main__":
    unittest.main()
