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

            else:
                # blank found, write only words upto blank
                yield "{}\n".format(current_line[:last_blank])
                index += last_blank + 1  # extra index to skip blank


if __name__ == "__main__":
    main()
