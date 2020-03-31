# Code reference is taken from https://courses.csail.mit.edu/6.006/fall11/rec/rec02.pdf
# Courtesy MIT OpenCourseWare

import sys
import math
import string
# The method processes the command-line arguments, and calls word frequencies for file
# for each document, then calls vector angle on the resulting lists.

# It seems like word frequencies for file
# is responsible for operation 1 (split each document into words) and operation 2 (count word frequencies),
# and then vector angle is responsible for operation 3 (compute dot product).


def main():
    filename_1 = "D1.txt" # sys.argv[1]
    filename_2 = "D2.txt" # sys.argv[2]
    # 7th Iteration: Instead of List, Dictionary is used. Sort Algorithm is removed.
    sorted_word_dict_1 = word_frequencies_for_file(filename_1)
    sorted_word_dict_2 = word_frequencies_for_file(filename_2)
    distance = vector_angle(sorted_word_dict_1, sorted_word_dict_2)
    print("The distance between the documents is: %0.6f (degrees)" % distance)

# The method below first calls read file, which returns a list of lines in the input file. We’ll omit
# the method code, because it is not particularly interesting, and we’ll assume that read file’s
# running time is proportional to the size of the input file. The input from read line is given
# to get words from line list, which computes operation 1 (split each document into
# words). After that, count frequency turns the list of words into a document vector (operation
# 2).

# 6th interation: The advantages of insertion sort are that it sorts in place, and it is simple to implement.
# However, its worst-case running time is O(N^2) for an N-element array. We’ll replace insertion
# sort with a better algorithm, merge sort. Merge sort is not in place, so we’ll need to modify
# word frequencies for file.

# Switching to merge sort improved the running time dramatically. 
# However, if we look at docDistance6th proﬁler output, we notice that merge is the function with the biggest runtime footprint. 
# Merge sort’s performance in practice is great, so it seems that the only way to make our code faster is to get rid of sorting altogether. 

# 7th iteration switches away from the sorted list representation of document vectors, 
# and instead uses the Python dictionary representation that was introduced in docDistance4th. 
# count frequency already used that representation internally, 
# so we only need to remove the code that converted the Python dictionary to a list.

# 8th iteration: At this point, all the algorithms in our solution are asymptotically optimal. 
# We can easily prove this, by noting that each of the 3 main operations runs in time proportional to its input size, 
# and each operation needs to read all its input to produce its output.
# However, there is still room for optimizing and simplifying the code.
# There is no reason to read each document line by line, and then break up each line into words.
# The last iteration processes reads each document into one large string, and breaks up the entire document into words at once. 
# Firstoff,read file is modiﬁed to return a single string, instead of an array of strings.
# Then, get words from line list is renamed to get words from file,and is simpliﬁed, because it doesn’t need to iterate over a list of lines anymore.
# Last, word frequencies for file is updated to reﬂect the renaming. 

def word_frequencies_for_file(filename):
    text = read_file(filename)
    word_list = get_words_from_text(text)
    freq_mapping = count_frequency(word_list)
    # 7th Iteration: Removed Merge Sort
    return freq_mapping

# 7th Iteration: merge sort function is removed.

# function to read file
def read_file(filename):
  fh = open(filename, encoding="utf8")
  try:
      # return fh.readlines()
      return fh.read()
  finally:
      fh.close()

# get words from line list calls get words from string for each line and
# combines the lists into one big list. Line 5 looks innocent but is a big performance killer, because
# using + to combine W/k lists of length k is O(W^2/k).

# get words from string takes one line in the input file and breaks it up into a list of
# words. TODO: line-by-line analysis. The running time is O(k), where k is the length of the line.

# 5th iteration simplifies get words from string that breaks up lines into words. First off,
# the standard library function string.translate is used for converting uppercase characters
# to lowercase, and for converting punctuation to spaces. Second, the split method on strings is
# used to break up a line into words.
translation_table = str.maketrans(string.punctuation + string.ascii_lowercase, " "*len(string.punctuation)+string.ascii_lowercase)

# Removed functions in 8th Iteration
def get_words_from_text(text):
    text = text.translate(translation_table)
    word_list = text.split()
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
    return D                # 7th Iteration: Conversion of dictionary items to list is removed.

# count frequency is the last function call in word frequencies for file. Next
# up, main calls vector angle, which performs operation 3, computing the distance metric.

def vector_angle(D1,D2):    # 7th Iteration: D1 D2 instead of L1 L2.
    numerator = inner_product(D1,D2)
    denominator = math.sqrt(inner_product(D1,D1)*inner_product(D2,D2))
    return math.degrees(math.acos(numerator/denominator))

# The method is a somewhat straightforward implementation of the distance metric
# arccos (L1·L2/|L1||L2|) = arccos (L1·L2/sqrt((L1 · L1)(L2 · L2)))
# and delegates to inner product for the hard work of computing cross products.

# 7th Iteration: D1 and D2 are dictionaries instead of lists (L1,L2)
def inner_product(D1,D2):
    sum = 0.0
    for key in D1: 
        if key in D2:
            sum += D1[key] * D2[key]
    return sum

# 3rd Iteration: The new implementation above runs in Θ(L1 + L2), where L1 and L2 are the lengths of the two
# document vectors. We observe that the running time for inner product (and therefore for
# vector angle) is asymptotically optimal, 
# because any algorithm that computes the inner product will have to read the two vectors, 
# and reading will take Ω(L1 + L2) time.

main()