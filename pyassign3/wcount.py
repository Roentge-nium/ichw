#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Zhao Jingliang"
__pkuid__  = "1700011787"
__email__  = "Roentgenium@pku.edu.cn"
"""

import sys
import collections
from urllib.request import urlopen


def remain_alpha(strings):
    all_words = ''
    for charact in strings:
        if charact.isalpha():
            all_words += charact
        else:
            all_words += ' '
    return all_words


def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line.
    """
    lower_words = lines.lower()
    only_words = remain_alpha(lower_words)
    words = only_words.split()
    words_dic = collections.Counter(words)
    topn_dic = dict(words_dic.most_common(topn))
    for key in topn_dic:
        space_number = 15 - len(key) - len(str(topn_dic[key]))
        print(key + ' ' * space_number + str(topn_dic[key]))

if __name__ == '__main__':

    if len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will out\
        put top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)
