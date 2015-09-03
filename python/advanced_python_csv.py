"""This program writes the email list from Part I of the Advanced Python
Exercise into a new csv file called 'emails.csv'.

John Gilling
"""

from advanced_python_regex import *

def write_csv(emails, file):
    """Writes a list of emails into the file, one per row.
    
    Arguments: emails is a list of email addresses, 
    file is a string representing a file name
    Returns: None
    """

    with open(file, 'wb') as csvfile:
        email_writer = csv.writer(csvfile)
        for email in emails:
            email_writer.writerow([email])


def main():
   email_list = get_email_list(read_data('faculty.csv'))
   write_csv(email_list, 'emails.csv')

if __name__ == '__main__':
    main()
