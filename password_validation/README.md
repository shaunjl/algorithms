# Overview

This is a password validator. It will validate passwords from STDIN
according to the following specifications-

1. Have between 8 and 64 characters
2. Allow all ASCII characters and spaces
3. Not be a common password

# Prerequisites

Python 2.7+

# Download and start

1. Download the contents of this package
2. Ensure execute permission is granted for `validate_passwords.py`

Ensure things are working correctly on terminal via `python test_validator.py`
The output should be as follows-

```
t*sting1 -> Error: Invalid Characters
1q2w3e4r -> Error: Too Common
carter -> Error: Too Short
. -> Error: Too Short
a -> Error: Too Short
1234567 -> Error: Too Short
11111111111111111111111111111111111111111111111111111111111111111 -> Error: Too Long
..password -> Error: Too Common
1q2w3e4r -> Error: Too Common
carter -> Error: Too Short
.
----------------------------------------------------------------------
Ran 4 tests in 2.368s

OK
```

If this is the output you got, you can proceed to test passwords via the
`validate_passwords.py` script:

`cat <input_passwords_file> | ./validate_passwords.py <weak_passwords_file>`

Please note that the `input_passwords_file` and the `weak_passwords_file`
must be in the same directory as `validate_passwords.py`.


E.g., `cat input_passwords.txt | ./validate_passwords.py 10-million-password-list-top-1000000.txt`