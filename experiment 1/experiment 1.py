from nltk.tokenize import sent_tokenize, word_tokenize


def tokenize_text(text):
	"""Return sentence tokens and word/punctuation tokens for the input text."""
	sentence_tokens = sent_tokenize(text)
	word_tokens = word_tokenize(text)
	return sentence_tokens, word_tokens


def main():
	text = input("Enter a sentence or paragraph: ").strip()

	if not text:
		print("Please enter some text.")
		return

	sentence_tokens, word_tokens = tokenize_text(text)

	print("\nSentence tokens:")
	for number, sentence in enumerate(sentence_tokens, start=1):
		print(f"{number}. {sentence}")

	print("\nWord and punctuation tokens:")
	print(word_tokens)


if __name__ == "__main__":
	main()
