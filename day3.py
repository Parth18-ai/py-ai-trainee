

sentence = input("Enter any sentence-")

vowels = "aeiou"
vowel_count = 0 

for letter in sentence.lower():
    if letter in vowels:
        vowel_count = vowel_count + 1 

words = sentence.split()
word_count = len(words)

reversed_sentence = sentence[::-1]

clean = ""
for letter in sentence.lower():
    if letter.isalnum():          
        clean = clean + letter

is_palindrome = (clean == clean[::-1])

# Show results
print("Vowels:", vowel_count)
print("Words:", word_count)
print("Reversed snetence:", reversed_sentence)
print("Palindrome:", is_palindrome)