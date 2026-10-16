paragraph = """Python is easy ,  Python is powerful, and Python is fun.
Learning Python is fun because Python is everywhere."""

words = paragraph.lower().replace(",", "").replace(".", "").split()


text = paragraph.lower()
for ch in ".,!?":
    text = text.replace(ch, "")
words = text.split()


unique_words = set(words)
print("\nUnique words:", unique_words)
print("Total unique:", len(unique_words))


freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
print("\nFrequency:", freq)


top3 = sorted(freq.items(), key=lambda pair: pair[1], reverse=True)[:3]

print("\nTop 3 words:")
for word, count in top3:
    print(f"{word} -> {count}") 