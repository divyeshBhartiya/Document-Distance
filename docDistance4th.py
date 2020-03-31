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
    insertion_sort(freq_mapping)
    return freq_mapping

# 3rd Iteration: insertion sort function
def insertion_sort(A):
    for j in range(len(A)):
        key = A[j]
        i = j-1
        while i>-1 and A[i]>key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
    return A


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

# The 4th iteration addresses count frequency, which is the biggest time consumer at the
# moment. The new implementation uses Python dictionaries. The dictionaries are implemented using
# hash tables, which will be presented in a future lecture. The salient feature of hash tables is that
# 6.006 Intro to Algorithms Recitation 2 September 14, 2011
# inserting an element using dictionary[key] = value and looking up an element using
# dictionary[key] both run in O(1) expected time.
# Instead of storing the document vector under construction in a list, the new implementation
# uses a dictionary. The keys are the words in the document, and the value are the number of times
# each word appears in the document. Since both insertion (line 5) and lookup (line 7) take O(1)
# time, building a document vector out of W words takes O(W) time.

def count_frequency (word_list):
    D = {}
    for new_word in word_list:
        if new_word in D:
            D[new_word] = D[new_word]+1
        else:
            D[new_word] = 1
    return list(D.items())

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
    i = 0
    j = 0
    while i<len(L1) and j<len(L2):
        # L1[i:] and L2[j:] yet to be processed
        if L1[i][0] == L2[j][0]:
            # both vectors have this word
            sum += L1[i][1] * L2[j][1]
            i += 1
            j += 1
        elif L1[i][0] < L2[j][0]:
            # word L1[i][0] is in L1 but not L2
            i += 1
        else:
            # word L2[j][0] is in L2 but not L1
            j += 1
    return sum

# 3rd Iteration: The new implementation above runs in Θ(L1 + L2), where L1 and L2 are the lengths of the two
# document vectors. We observe that the running time for inner product (and therefore for
# vector angle) is asymptotically optimal, 
# because any algorithm that computes the inner product will have to read the two vectors, 
# and reading will take Ω(L1 + L2) time.

main()