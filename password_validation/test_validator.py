#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from utils import get_weak_password_list
from validator import Validator


class TestNameGetter(unittest.TestCase):
    def setUp(self):
        weak_password_list = get_weak_password_list(debug_file_path='10-million-password-list-top-1000000.txt')
        self.validator = Validator(weak_password_list)

    def test_normal(self):
        acceptable_passwords = ['234234 1234234',
                                '#$LSGDF@#$']
        self._test_passwords(acceptable_passwords, expected_valid=True)

    def test_lengths(self):
        unacceptable_passwords = ['',
                                  'a',
                                  '1234567',
                                  '11111111111111111111111111111111111111111111111111111111111111111']
        acceptable_passwords = ['1111111111111111111111111111111111111111111111111111111111111111',
                                'SDLWTJ23']
        self._test_passwords(unacceptable_passwords, expected_valid=False)
        self._test_passwords(acceptable_passwords, expected_valid=True)

    def test_weak(self):
        unacceptable_passwords = ['password',
                                  '1q2w3e4r',
                                  'carter']
        acceptable_passwords = ['waverly!',
                                'lk234lkj23']
        self._test_passwords(unacceptable_passwords, expected_valid=False)
        self._test_passwords(acceptable_passwords, expected_valid=True)

    def test_chars(self):
        unacceptable_passwords = ['tésting1',
                                  '1q2w3e4r',
                                  'carter']
        self._test_passwords(unacceptable_passwords, expected_valid=False)

    def _test_passwords(self, passwords, expected_valid=True):
        for password in passwords:
            valid = self.validator.validate(password)
            if expected_valid:
                self.assertTrue(valid)
            else:
                self.assertFalse(valid)


if __name__ == '__main__':
    unittest.main()
