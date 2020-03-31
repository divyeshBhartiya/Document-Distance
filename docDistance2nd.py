# Code reference is taken from https://courses.csail.mit.edu/6.006/fall11/rec/rec02.pdf
# Courtesy MIT OpenCourseWare

import sys
import math

# The method processes the command-line arguments, and calls word frequencies for file
# for each document, then calls vector angle on the resulting lists.

# It seems like word frequencies for file
# is responsible for operation 1 (split each document into words) and operation 2 (count word frequencies),
# and then vector angle is responsible for operation 3 (compute dot product).


def main():
    filename_1 = "D1.txt" # sys.argv[1]
    filename_2 = "D2.txt" # sys.argv[2]
    sorted_word_list_1 = word_frequencies_for_file(filename_1)
    sorted_word_list_2 = word_frequencies_for_file(filename_2)
    distance = vector_angle(sorted_word_list_1, sorted_word_list_2)
    print("The distance between the documents is: %0.6f (degrees)" % distance)

# The method below first calls read file, which returns a list of lines in the input file. We’ll omit
# the method code, because it is not particularly interesting, and we’ll assume that read file’s
# running time is proportional to the size of the input file. The input from read line is given
# to get words from line list, which computes operation 1 (split each document into
# words). After that, count frequency turns the list of words into a document vector (operation
# 2).

def word_frequencies_for_file(filename):
    line_list = read_file(filename)
    word_list = get_words_from_line_list(line_list)
    freq_mapping = count_frequency(word_list)
    return freq_mapping

# function to read file
def read_file(filename):
  fh = open(filename, encoding="utf8")
  try:
      return fh.readlines()
  finally:
      fh.close()

# get words from line list calls get words from string for each line and
# combines the lists into one big list. Line 5 looks innocent but is a big performance killer, because
# using + to combine W/k lists of length k is O(W^2/k).

def get_words_from_line_list(line_list):
    word_list = []
    for line in line_list:
        words_in_line = get_words_from_string(line)
        word_list.extend(words_in_line) # 2nd Interation: Replacing + with extend yields a 30% runtime improvement.
    return word_list

# get words from string takes one line in the input file and breaks it up into a list of
# words. TODO: line-by-line analysis. The running time is O(k), where k is the length of the line.

def get_words_from_string(line):
    word_list = []
    character_list = []
    for c in line:
        if c.isalnum():
            character_list.append(c)
        elif len(character_list) > 0:
            word = "".join(character_list)
            word = word.lower()
            word_list.append(word)
            character_list = []
    if len(character_list) > 0:
            word = "".join(character_list)
            word = word.lower()
            word_list.append(word)
    return word_list

# The output of get words from line list is a list of words, like [’a’, ’cat’,
# ’in’, ’a’, ’bag’]. word frequencies from file passes this output to count frequency,
# which turns it into a document vector that counts the number of occurrences of each word, and
# looks like [[’a’, 2], [’cat’, 1], [’in’, 1], [’bag’, 1]].

def count_frequency (word_list):
    L = []
    for new_word in word_list:
        for entry in L:
            if new_word == entry[0]:
                entry[1] = entry[1] + 1
                break
        else:
            L.append([new_word,1])
    return L

# The implementation above builds the document vector by takes each word in the input list and
# looking it up in the list representing the under-construction document vector. In the worst case of
# a document with all different words, this takes O(W^2 × l) time, where W is the number of words
# in the document, and l is the average word length.            

# count frequency is the last function call in word frequencies for file. Next
# up, main calls vector angle, which performs operation 3, computing the distance metric.

def vector_angle(L1,L2):
    numerator = inner_product(L1,L2)
    denominator = math.sqrt(inner_product(L1,L1)*inner_product(L2,L2))
    return math.degrees(math.acos(numerator/denominator))

# The method is a somewhat straightforward implementation of the distance metric
# arccos (L1·L2/|L1||L2|) = arccos (L1·L2/sqrt((L1 · L1)(L2 · L2)))
# and delegates to inner product for the hard work of computing cross products.

def inner_product(L1,L2):
    sum = 0.0
    for word1, count1 in L1:
        for word2, count2 in L2:
            if word1 == word2:
                sum += count1 * count2
    return sum

main()