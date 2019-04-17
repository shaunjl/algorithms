#!/usr/bin/env python

from utils import get_weak_password_list
from validator import Validator


def main():
    weak_password_list = get_weak_password_list()
    validator = Validator(weak_password_list)

    while True:
        try:
            password = input()
        except EOFError:
            break
        validator.validate(password)


if __name__ == '__main__':
    main()
