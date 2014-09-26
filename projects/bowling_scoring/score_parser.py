"""
Scoring system and jargon is described at:

[0]: http://bowling.about.com/od/rulesofthegame/a/bowlingscoring.htm

Design an engine that can compute the score for a bowling game.

Input:
    * incrementally, the state of each throw. Since the score
      computation depends on future throws, unless all throws are
      given, the final score cannot be computed.
    * constraints: the input string can have a maximum of 20
      characters. This is if each frame is an open frame.
      Maximum number of throws is 10 + 2, if the last one is 21.
      This is when all are open frames but the last throw is a
      strike. That gives 2 more chances at the end.
    * to make this as human-parsable as possible, the state of the
      game will be represented as its represented on paper. If a human
      can read it, so can a machine :-)

Output:
    * The display board as shown in [0], updated as more information
      streams in.

Notes:
    * You can represent the state by a list of characters that the user
      obtained on throws.
    * first, write a function that accepts a string of scores of any lenght,
      validates that its a valid string and then computes a score string.
    * its pretty clear that the engine that computes the score is a state
      machine.

    * language of the machine:

      X X X
      X X number
      X number number
      X number /

      number number
      number / X
      number / number

"""
import unittest


NUMBER = "0123456789"


class TestAlg(unittest.TestCase):

    def test_1(self):
        sp = ScoreParser()
        inp = "X 7 / 7 2 9 / X X X 2 3 X 7 / 3".split()
        sp.read_stream(inp)
        self.assertEqual(sp.score, 171)
        inp = "X 7 / 7 2 9 / X X X 2 3 X X X X".split()
        sp.read_stream(inp)
        self.assertEqual(sp.score, 198)
        inp = "X 7 / 7 2".split()
        sp.read_stream(inp)
        self.assertEqual(sp.score, 46)

    def test_update(self):
        sp = ScoreParser()
        # test all valid token paths:
        # X X X
        inp = "XXX"
        for token in inp:
            result = sp.update(token)
        self.assertEqual(result, 30)
        # X X number
        for i in range(10):
            inp = "XX{}".format(i)
            for token in inp:
                result = sp.update(token)
            self.assertEqual(result, 20+i)
        # X number number
        for i in range(10):
            for j in range(10):
                inp = "X{}{}".format(i, j)
                for token in inp:
                    result = sp.update(token)
                self.assertEqual(result, 10+i+j)

        # X number /
        for i in range(10):
            inp = "X{}/".format(i)
            for token in inp:
                result = sp.update(token)
            self.assertEqual(result, 20)

        # number number
        for i in range(10):
            for j in range(10):
                inp = "{}{}".format(i, j)
                for token in inp:
                    result = sp.update(token)
                self.assertEqual(result, i+j)
        # number / X
        for i in range(10):
            inp = "{}/X".format(i)
            for token in inp:
                result = sp.update(token)
            self.assertEqual(result, 20)

        # number / number
        for i in range(10):
            for j in range(10):
                inp = "{}/{}".format(i, j)
                for token in inp:
                    result = sp.update(token)
                self.assertEqual(result, 10+j)


class ScoreParser(object):
    """Class to consume input and spit out score"""

    # pre-create the computation tree
    tree = {"X": {"X": {"X": 30}}}
    for i in range(10):
        tree["X"]["X"][str(i)] = 20 + i
        tree["X"][str(i)]={"/": 20}
        tree[str(i)] = {"/": {"X": 20}}
        for j in range(10):
            tree["X"][str(i)][str(j)] = 10 + i + j
            tree[str(i)][str(j)] = i+j
            tree[str(i)]["/"][str(j)] = 10+j

    # pre-compute next-token
    next_token = {"X": 1}
    for i in range(10) :
        next_token[str(i)] = 2


    def __init__(self):
        self.reset()

    def update(self, token):
        if isinstance(self._state[token], dict):
            self._state = self._state[token]
            return None
        else:
            result = self._state[token]
            self._state = self.tree
            return result

    def _compute_scores(self):
        self._scores = []
        i = 0
        while i < len(self._buf):
            for j in range(3):
                result = self.update(self._buf[i+j])
                if result is not None:
                    self._scores.append(result)
                    break
            i += self.next_token[self._buf[i]]
            if len(self._scores) > 9:
                break

    def read_stream(self, stream):
        self.reset()
        for token in stream:
            self._buf.append(token)

    def read(self, token):
        self._buf.append(token)

    @property
    def scores(self):
        self._compute_scores()
        return self._scores

    @property
    def score(self):
        self._compute_scores()
        return sum(self._scores)

    def reset(self):
        self._state = self.tree
        self._scores = []
        self._buf = []


if __name__ == "__main__":
    unittest.main()
