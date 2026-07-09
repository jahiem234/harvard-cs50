text = input("Text: ")

letter = 0
word = 1
sentence = 0
punctuation = [".", "!", "?"]

for words in text:
    if (words == " "):
        word += 1

for x in range(len(text)):
    if (text[x].isalpha()):
        letter += 1

for x in range(len(text)):
    if (text[x] in punctuation):
        sentence += 1

L = (letter / word) * 100
S = (sentence / word) * 100

index = round((0.0588 * L) - (0.296 * S) - 15.8)

if (index >= 16):
    print("Grade 16+")
elif (index <= 1):
    print("Before Grade 1")
else:
    print("Grade " + str(index))

# count number of letters (any alphabet)
