import os

import certifi
import nltk
from nltk import pos_tag, word_tokenize
from nltk.stem import WordNetLemmatizer


def lemmatize_text(text):
	"""Tokenize text and return each word with its POS-aware lemma."""
	lemmatizer = WordNetLemmatizer()
	wordnet_pos = {"J": "a", "V": "v", "N": "n", "R": "r"}
	tagged_words = pos_tag(word_tokenize(text))
	return [
		(word, lemmatizer.lemmatize(word, wordnet_pos.get(tag[0], "n")))
		for word, tag in tagged_words
	]


if __name__ == "__main__":
	# Use a maintained CA bundle for HTTPS downloads when no custom bundle is set.
	os.environ.setdefault("SSL_CERT_FILE", certifi.where())

	for resource in (
		"punkt",
		"punkt_tab",
		"averaged_perceptron_tagger",
		"averaged_perceptron_tagger_eng",
		"wordnet",
		"omw-1.4",
	):
		if not nltk.download(resource, quiet=True):
			raise RuntimeError(f"Failed to download NLTK resource: {resource}")

	text = input("Enter words or a sentence to lemmatize: ")
	for word, lemma in lemmatize_text(text):
		print(f"{word} -> {lemma}")
