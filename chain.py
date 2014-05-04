import re
import random

words_after = {}
pattern = re.compile('[^\w\s]+')

with open("MACBETH.txt") as source_file:
    words = pattern.sub('', source_file.read()).split()
    #  Create a dictionary that maps each word to a list of words that follow it
    for i in xrange(1, len(words)):
        word = words[i-1]
        if word in words_after:
            words_after[word].append(words[i])
        else:
            words_after[word] = [words[i]]
#  starting with start word generate a sentence to whatever length (of words)
def generate_sentence(start, length):
    sentence = [start]
    count = 1
    word = start
    while word in words_after and count < length:
        word = random.choice(words_after[word])
        count += 1
        sentence.append(word)
    return ' '.join(sentence)

#  10 word long sentence starting with the word trifle
print generate_sentence('trifle', 10)