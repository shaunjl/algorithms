import sys
import os
import csv


def get_weak_password_list(debug_file_path=None):
    """
    :arg debug_file_path: if provided, will use file path provided instead of script argument
    return: a set of weak passwords from 1st script argument, which is a filename in provided directory
    """
    def get_file_path():
        if debug_file_path:
            file_name = debug_file_path
        else:
            args = sys.argv
            if len(args) != 2:  # 1 for script, one for weak password list
                exit('Usage is as follows: python password_validator.py <weak_password_list.txt>')
            file_name = args[1]

        abs_path = os.path.abspath(__file__)
        dir_name = os.path.dirname(abs_path)

        return os.path.join(dir_name, file_name)

    file_path = get_file_path()
    weak_passwords = set()  # using a set to get O(1) insertion and lookup
    with open(file_path) as f_obj:
        csv_file = csv.reader(f_obj, delimiter='\n')
        for password_line in csv_file:
            weak_passwords.add(password_line[0])

    return weak_passwords
