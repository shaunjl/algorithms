class Validator:
    def __init__(self, weak_passwords):
        self.weak_passwords = weak_passwords

    def validate(self, password):
        """
        applies all validation tests, stopping on the first failed test
        """
        valid = self._validate_chars(password)
        if not valid:
            return False
        valid = self._validate_pass_len(password)
        if not valid:
            return False
        valid = self._validate_not_weak(password)
        if not valid:
            return False
        return True

    def _validate_chars(self, password):
        ascii_low = 0
        ascii_high = 127
        new_pass = ''
        valid = True
        for char in password:
            char_num = ord(char)
            if ascii_low <= char_num <= ascii_high:
                new_pass += char
            else:
                valid = False
                new_pass += '*'
        if not valid:
            Validator._print_err(new_pass, 'Invalid Characters')
        return valid

    def _validate_pass_len(self, password):
        pass_len = len(password)
        valid = True
        if pass_len < 8:
            Validator._print_err(password, 'Too Short')
            valid = False
        elif pass_len > 64:
            Validator._print_err(password, 'Too Long')
            valid = False
        return valid

    def _validate_not_weak(self, password):
        if password in self.weak_passwords:
            Validator._print_err(password, 'Too Common')
            return False
        return True

    @staticmethod
    def _print_err(password, err_msg):
        print('{} -> Error: {}'.format(password, err_msg))
