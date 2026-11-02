from collections import Counter
import re


# Common stop words are removed during the basic NLP preprocessing step.
STOP_WORDS = {
	"a", "an", "and", "are", "as", "at", "be", "by", "for", "from",
	"has", "he", "in", "is", "it", "of", "on", "that", "the", "this",
	"to", "was", "were", "will", "with", "you",
}


def analyze_text(text):
	"""Tokenize, normalize, and count meaningful words and characters."""
	# Tokenization and case normalization are standard NLP preprocessing steps.
	tokens = re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", text.casefold())
	words = [token for token in tokens if token not in STOP_WORDS]
	characters = Counter(character for character in text.casefold() if character.isalpha())

	return Counter(words), characters


text = input("Enter text: ").strip()
word_frequencies, character_frequencies = analyze_text(text)

print("\nMost frequent words (excluding stop words):")
if word_frequencies:
	for word, count in word_frequencies.most_common():
		print(f"{word}: {count}")
else:
	print("No meaningful words found.")

print("\nCharacter frequencies:")
for character, count in character_frequencies.most_common():
	print(f"{character}: {count}")

print(f"\nTotal words: {len(re.findall(r'[A-Za-z]+(?:\'[A-Za-z]+)?', text))}")
print(f"Unique words: {len(word_frequencies)}")
print(f"Total alphabetic characters: {sum(character_frequencies.values())}")
