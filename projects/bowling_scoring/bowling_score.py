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
        inp = "X 7 / 7 2 9 / X X X 2 3 X 7 / 3"
        self.assertEqual(compute_score(inp), 171)
        inp = "X 7 / 7 2 9 / X X X 2 3 X X X X"
        self.assertEqual(compute_score(inp), 198)


def compute_score(uscore):
    uscore =  uscore.split()
    nexti = 0
    inclist = []

    for fakeindex in range(10):
        i = nexti
        item = uscore[i]
        if item == "X":
            nexti += 1
            if uscore[i+1] == "X":
                if uscore[i+2] == "X":
                    inc = 30
                elif uscore[i+2] in NUMBER:
                    inc = (20 + int(uscore[i+2]))
            elif uscore[i+1] in NUMBER:
                if uscore[i+2] in NUMBER:
                    inc = (10 + int(uscore[i+1]) + int(uscore[i+2]))
                elif uscore[i+2] == "/":
                    inc = 20
        elif item in NUMBER:
            nexti += 2
            if uscore[i+1] in NUMBER:
                inc = (int(item) + int(uscore[i+1]))
            elif uscore[i+2] == "X":
                inc = 20
            elif uscore[i+2] in NUMBER:
                inc = 10 + int(uscore[i+2])
        inclist.append(inc)

    return sum(inclist)


if __name__ == "__main__":
    unittest.main()
