import re
import random

words_after = {}
pattern = re.compile('[^\w\s]+')
with open("MACBETH.txt") as source_file:
    words = pattern.sub('', source_file.read()).split()

    for i in xrange(1, len(words)):
        word = words[i-1]
        if word in words_after:
            words_after[word].append(words[i])
        else:
            words_after[word] = [words[i]]

def generate_sentence(start, length):
    sentence = [start]
    count = 0
    word = start
    while word in words_after and count <= length:
        word = random.choice(words_after[word])
        count += 1
        sentence.append(word)
    return ' '.join(sentence)
    
print generate_sentence('trifle', 10)