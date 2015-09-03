""" This program reads the file faculty.csv, a table of the Biostats
Faculty List at UPenn, and uses regular expressions to analyze the data.

John Gilling
"""

import csv
import re

def read_data(data):
    """Returns a list of lists representing the rows of the csv file data.
    
    Arguments: data is the name of a csv file (as a string)
    Returns: list of lists of strings
    """

    table = []
    with open(data, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            table.append(row)
    return table

def get_degree_hist(parsed_data):
    """Returns a histogram dictionary of the different degrees 
    and their frequencies. Uses regular expressions to remove
    inconsistencies with dots (i.e. 'Ph.D.' vs 'PhD', etc.).

    Arguments: parsed_data is a list of lists returned by read_data
    Returns: dictionary with degrees as keys and frequencies as values
    """
    
    degree_hist = {}
    for row in parsed_data:
        if row[1] == ' degree' or row[1] == '0':
            continue
        row[1] = row[1].split()
        for i in range(len(row[1])):
            row[1][i] = re.sub(r'\.', r'', row[1][i])
            degree_hist[row[1][i]] = 1 + degree_hist.get(row[1][i], 0)
    return degree_hist

def get_title_hist(parsed_data):
    """Returns a histogram dictionary of the different titles and
    their frequencies. Uses regular expressions to remove the redundant
    'of Biostatistics' from each title (and in fact fixes a typo as well!).
    
    Arguments: parsed_data is a list of lists returned by read_data
    Returns: dictionary with titles as keys and frequencies as values
    """

    title_hist = {}
    for row in parsed_data:
        if row[2] == ' title':
            continue
        row[2] = re.sub(r' (is|of) Biostatistics', r'', row[2])
        title_hist[row[2]] = 1 + title_hist.get(row[2], 0)
    return title_hist

def get_email_list(parsed_data):
    """Returns a list of email addresses for the faculty. Uses 
    regular expressions to check that each email address fits a 
    valid string pattern.

    Arguments: parsed_data is a list of lists returned by read_data
    Returns: list of email addresses
    """

    email_list = []
    for row in parsed_data:
        if row[3] == ' email':
            continue
        if re.search(r'\w@\w', row[3]):
            email_list.append(row[3])
    return email_list

def get_domains(email_list):
    """Returns a set of unique domains for the email addresses in
    email_list. Uses regular expressions to strip the local-part
    and the @ symbol.
    
    Arguments: email_list is a list of strings representing email addresses
    Returns: a set of strings representing the unique domains represented
    """

    domain_list = []
    for email in email_list:
        domain_list.append(re.sub(r'.+@', r'', email))
    return set(domain_list)

def main():
    faculty = read_data('faculty.csv')
    print '\nHere is a histogram of the degree types and frequencies:'
    print get_degree_hist(faculty)
    print '\nHere is a histogram of the titles and frequencies:'
    print get_title_hist(faculty)
    emails = get_email_list(faculty)
    print '\nHere is a list of the email addresses:'
    print emails
    domains = get_domains(emails)
    print '\nHere is a set of the unique ' + str(len(domains)) +' domain names of the emails:'
    print domains, '\n'
    print faculty

if __name__ == '__main__':
    main()
