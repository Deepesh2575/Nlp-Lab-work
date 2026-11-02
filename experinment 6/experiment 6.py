"""Stem words using NLTK's Porter stemming algorithm."""

from nltk.stem import PorterStemmer


def stem_words(words):
	stemmer = PorterStemmer()
	return [stemmer.stem(word) for word in words]


if __name__ == "__main__":
	words = input("Enter words separated by spaces: ").split()
	for word, stem in zip(words, stem_words(words)):
		print(f"{word} -> {stem}")
