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
