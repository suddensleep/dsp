import csv
import math

def read_data(data):
    """Returns a list of lists representing the rows of the csv file data.
    Additionally cleans up the underscores from the team names, turning them
    into spaces.
    
    Arguments: data is the name of a csv file (as a string)
    Returns: list of lists of cleaned strings
    """

    table = []
    with open(data, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            row[0] = row[0].replace('_', ' ')
            table.append(row)
    return table

def get_min_score_difference(parsed_data):
    """Returns the index of the team with the smallest difference
    between 'for' and 'against' goals.

    Arguments: parsed_data is a list of lists of cleaned strings
    Returns: integer row index
    """

    minDiff = 1000
    minI = -1
    for i in range(1,len(parsed_data)):
        teamDiff = get_team(i, parsed_data)
        if teamDiff < minDiff:
            minDiff = teamDiff
            minI = i
    return minI

def get_team(index_value, parsed_data):
    """Returns the difference between 'for' and 'against' goals
    for the team at the given row index.

    Arguments: index_value is an integer row index, parsed_data same as above
    Returns: positive integer representing goal difference
    """

    return abs(int(parsed_data[index_value][5]) - int(parsed_data[index_value][6]))

def main():
    footballTable = read_data('football.csv')
    minRow = get_min_score_difference(footballTable)
    print "The team with the smallest difference between 'for' and 'against' goals is", 
    print footballTable[minRow][0],
    print "with a difference of |" + footballTable[minRow][5] + "-" + footballTable[minRow][6] + "| =",
    print str(get_team(minRow, footballTable)) + '.'

if __name__ == '__main__':
    main()
