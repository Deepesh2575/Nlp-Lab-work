import re


def generate_regex(text):
	"""Create a regular-expression pattern that matches text literally."""
	# Characters such as ., *, +, ?, and [ have special meanings in regex.
	# re.escape() adds backslashes where needed so they match as plain text.
	return re.escape(text)


if __name__ == "__main__":
	# Get the text from the user. For example, entering "cat.1" keeps the
	# period literal instead of treating it as a regex wildcard.
	given_text = input("Enter text to convert to a regular expression: ")

	# Convert the text, then display the generated pattern.
	pattern = generate_regex(given_text)
	print("Generated regular expression:", pattern)

	# fullmatch succeeds only when the entire input string matches the pattern.
	if re.fullmatch(pattern, given_text):
		print("The pattern matches the given text exactly.")
