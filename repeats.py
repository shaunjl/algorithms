def find_repeats(letters):
	last_letter = None
	longest_repeat = 1
	longest_repeat_letter = None
	curr_repeats = 1
	for letter in letters:
		if letter == last_letter:
			curr_repeats += 1
			if curr_repeats > longest_repeat:
				longest_repeat = curr_repeats
				longest_repeat_letter = letter
		else:
			curr_repeats = 1
		last_letter = letter
	if not longest_repeat_letter:
		return letters[0] if letters else letters
	return longest_repeat_letter * longest_repeat 

tests = ['hhhhssd', 'sshhhhh', 's', '', 'abcde', 'hhss', 'dddddd']

for test in tests:
	print(find_repeats(test))