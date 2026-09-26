# 9. Create a dictionary and count the frequency of each word in a sentence.
sentence = "python is easy and python is useful"
frequency = {}
for word in sentence.split():
    frequency[word] = frequency.get(word, 0) + 1
print(frequency)
