
with open("paragraph.txt", "r") as f:
    text = f.read()


lines = text.splitlines()
num_lines = len(lines)
num_words = len(text.split())
num_chars = len(text)

with open("summary.txt", "w") as f:
    f.write(f"Lines: {num_lines}\n")
    f.write(f"Words: {num_words}\n")
    f.write(f"Characters: {num_chars}\n")

print("Summary saved to summary.txt")
