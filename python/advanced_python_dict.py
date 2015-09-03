"""This program creates two different dictionaries describing the 
faculty list from faculty.csv.

John Gilling
"""

from advanced_python_regex import *

def make_first_grouped_dict(fac):
    """Creates and returns a dictionary with keys as the last name 
    of the faculty member, and values as a list of the details of the
    faculty members with that last name.

    Arguments: fac is a list of lists returned by read_data
    Returns: a dictionary (keys = last names, values = lists (of lists) 
    of details for each faculty member with the given last name
    """

    by_last = {}
    for row in fac[1:]:
        key = row[0].split()[-1]
        by_last.setdefault(key, []).append([row[1], row[2], row[3]])
    return by_last

def make_second_grouped_dict(fac):
    """Creates and returns a dictionary with keys as tuples representing 
    the first and last names of the faculty member, and values as a list
    of the details of the faculty members with that exact name.

    Arguments: fac is a list of lists returned by read_data
    Returns: a dictionary (keys = tuples (first, last), values = lists
    of details for each faculty member with the given first and last names
    """

    by_full = {}
    for row in fac[1:]:
        name = row[0].split()
        key = (' '.join(name[:-1]), name[-1])
        by_full.setdefault(key, []).extend([row[1], row[2], row[3]])
    return by_full

def print_by_alpha(d):
    """Prints the first three entries of an alphabetically sorted version 
    of the dictionary passed in.

    Arguments: d is a dictionary with keys as strings
    Returns: None
    """
    d_as_list = []
    for key, val in d.items():
        d_as_list.append((key, val))
    d_as_list.sort()
    print d_as_list[:3], '\n'

def print_by_last_name(d):
    """Prints the first three entries of an alphabetically sorted (by last
    name) version of the dictionary passed in.

    Arguments: d is a dictionary with keys as tuples
    Returns: None
    """

    d_as_list = []
    for key, val in d.items():
        d_as_list.append((key, val))
    d_as_list.sort(key = lambda x: x[0][1])
    print d_as_list[:3], '\n'

def main():
    faculty = read_data('faculty.csv')
    get_degree_hist(faculty)
    get_title_hist(faculty)
    dict1 = make_first_grouped_dict(faculty)
    print "\nHere's the first few entries in dictionary 1:"
    print_by_alpha(dict1)
    dict2 = make_second_grouped_dict(faculty)
    print "\nHere's the first few entries in dictionary 2, sorted by first name:"
    print_by_alpha(dict2)
    print "\nHere's the first few entries in dictionary 2, sorted by last name:"
    print_by_last_name(dict2)

if __name__ == '__main__':
    main()
