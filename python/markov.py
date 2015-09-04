"""Originally conceived as a solution to Exercise 13.8 (part 3) in Robert Downey's 
book 'Think Python', this program has been reworked to answer the optional Metis 
prework problem on Markov chains. Part of this reworking included comparing my 
solution to the one posted on Robert's site, and adopting some of his techniques.
Making the markov_map and prefix variables global, for example, was a stroke of
genius on HIS part, not on mine. As such, I'll include his copyright info at the
bottom of this file.

Note: the syntax for running this file is simply:

$ python markov.py

rather than the requested syntax. I had another version that would pull arguments 
from the command line, but decided to implement this in a more 'hard-coded' way 
instead because I found the mashing-up of romance and sci-fi too good not to share.
Hope you enjoy a good English/Martian love story! 

John Gilling
"""

import string
import random

markov_map = {}
prefix = ()

def read_book(filename, order = 2):
    """This function reads the book located at the given filename, 
    and creates a markov_map dictionary with the given prefix length.

    Arguments: filename is a string, order is an integer
    Returns: None
    """

    fin = open(filename)
    skip_header(fin)
    for line in fin:
        for word in line.strip().split():
            process_word(word, order)
        
def skip_header(file):
    """This sketchy little function is a bit of a workaround for
    skipping the Project Gutenberg headers for the specific books 
    'Emma' by Jane Austen and 'A Princess of Mars' by Edgar Rice 
    Burroughs. It is a bit of a quick fix, since each PG book has
    different header information. To be developed further.
    
    Arguments: file is a file object
    Returns: None
    """

    for line in file:
        if line.startswith('*END*THE SMALL PRINT!') or line.startswith('*** START OF THIS PROJECT GUTENBERG EBOOK A PR'):
            break

def process_word(s, order):
    """Takes a string and a desired prefix length, and appends it 
    to the suffix list (values) for the current prefix (keys) in markov_map.
    Additionally, this function calls shift to change the current 
    prefix to the next prefix.
    
    Arguments: s is a string, order is an int
    Returns: None
    """

    global prefix
    if len(prefix) < order:
        prefix += (s,)
        return

    markov_map.setdefault(prefix, []).append(s)
    prefix = shift(prefix, s)

def shift(prefix, word):
    """Word is added to the end of the tuple, and the first 
    element of the tuple is popped off.

    Arguments: prefix is a tuple, word is a string
    Returns: new tuple to be assigned to the global variable prefix
    """

    return prefix[1:] + (word,)

def make_chain(length):
    """Writes a story of 'length' words using the markov_map as a guide. 
    The starting words are chosen at random, and the remainder of the story 
    is chosen one word at a time, each new word being based on the probability 
    that it will follow the tuple of words currently stored in 'start'.

    Arguments: length is an int
    Returns: None
    """
    
    start = random.choice(markov_map.keys())
    for i in range(length):
        suffixes = markov_map.get(start, None)
        if suffixes == None:
            make_chain(n-i)
            return
        word = random.choice(suffixes)
        print word,
        start = shift(start, word)

if __name__ == '__main__':
    """Creates a 'mashup' of Emma and A Princess of Mars.
    """
    
    read_book('emma.txt', 2)
    prefix = ()
    read_book('aprincessofmars.txt', 3)
    prefix = ()
    make_chain(100)


"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""
