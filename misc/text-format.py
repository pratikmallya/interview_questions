"""
Format the characters in the stdin by the given number of spaces
Python 3

Assumptions:
============
* if a word is greater than width, it will NOT be split across the
  lines. Instead, the entire word will be printed out
* the line to be read is not larger than available main memory
* input is formatted correctly (no blank lines etc)

"""

import sys
import unittest


class TestAlg(unittest.TestCase):

    def setUp(self):
        self.texts = [
            "The quick brown fox jumps over the lazy dog.",
            "Sheikh Mujibur Rahman (Bengali: শেখ মুজিবুর রহমান Shekh "
            "Mujibur Rôhman), (17 March 1920 – 15 August 1975) was a "
            "preeminent Bengali nationalist leader of Bangladesh.[1] He "
            "headed the Awami League and was the first President of "
            "Bangladesh during the Bangladesh Liberation War, and later "
            "became Prime Minister in independent Bangladesh. He is "
            "popularly referred to as Sheikh Mujib (shortened as Mujib "
            "or Mujibur, not Rahman), with the honorary title of "
            "Bangabandhu (বঙ্গবন্ধু Bôngobondhu, 'Friend of Bengal'). "
            "His eldest daughter, Sheikh Hasina, is the present leader "
            "of the Awami League and the current Prime Minister of "
            "Bangladesh. As a student political leader, Mujib rose in "
            "Bengali politics and within ranks of the Awami League. An "
            "advocate of socialism, he became popular for his opposition "
            "to the ethnic and institutional discrimination against "
            "Bengalis, who comprised the majority of Pakistan's "
            "population."
            ]

        self.text60 = [
            "Sheikh Mujibur Rahman (Bengali: শেখ মুজিবুর রহমান Shekh",
            "Mujibur Rôhman), (17 March 1920 – 15 August 1975) was a",
            "preeminent Bengali nationalist leader of Bangladesh.[1] He",
            "headed the Awami League and was the first President of",
            "Bangladesh during the Bangladesh Liberation War, and later",
            "became Prime Minister in independent Bangladesh. He is",
            "popularly referred to as Sheikh Mujib (shortened as Mujib",
            "or Mujibur, not Rahman), with the honorary title of",
            "Bangabandhu (বঙ্গবন্ধু Bôngobondhu, 'Friend of Bengal').",
            "His eldest daughter, Sheikh Hasina, is the present leader",
            "of the Awami League and the current Prime Minister of",
            "Bangladesh. As a student political leader, Mujib rose in",
            "Bengali politics and within ranks of the Awami League. An",
            "advocate of socialism, he became popular for his opposition",
            "to the ethnic and institutional discrimination against",
            "Bengalis, who comprised the majority of Pakistan's",
            "population.",
            ]

    def test_border(self):

        width = 10000000
        for text in self.texts:
            line = get_lines(text, width).send(None)
            self.assertEqual(line, "{}\n".format(text))

        width = 1
        line = get_lines(self.texts[0], width).send(None)
        self.assertEqual(line, "The\n")

    def test_sanity(self):

        for width in (i for i in range(50, 1000)):
            for text in self.texts:
                for line in get_lines(text, width):
                    self.assertTrue(len(line) <= width)

        for index, line in enumerate(get_lines(self.texts[1], 60)):
            self.assertEqual(line, "{}\n".format(self.text60[index]))


def main():

    with open(sys.argv[1], 'r') as o:
        while True:
            width = o.readline()
            text = o.readline()

            if width == '':
                # reached EOF
                break

            lines = get_lines(text, int(width))
            sys.stdout.writelines(lines)


def get_lines(text, width):
    """Return a generator that yields a new line in every iteration"""

    index = 0

    while True:

        current_line = text[index:index+width]

        if index + width > len(text):
            yield "{}\n".format(current_line)
            break
        if current_line == '':
            # reached the end of text
            break
        else:
            last_blank = current_line.rfind(' ')
            if last_blank == -1:
                # no blank in current line, write whole word
                word_end_index = text[index:].find(' ')

                if word_end_index == -1:
                    # if last word in text
                    current_line = text[index:]
                    index += len(current_line)
                else:
                    current_line = text[index:index+word_end_index]
                    index += word_end_index + 1  # extra index to skip blank

                yield "{}\n".format(current_line)
                continue

            else:
                # blank found, write only words upto blank
                yield "{}\n".format(current_line[:last_blank])
                index += last_blank + 1  # extra index to skip blank


if __name__ == "__main__":
    unittest.main()
