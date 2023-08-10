import re
userInput = input("Enter some text: ")

words = userInput.split()
vocabulary = {}
for word in words:
    word = re.sub(r'[^\w\s]', '', word)
    vocabulary[word] = vocabulary.get(word, 0) + 1
if "" in vocabulary:
    del vocabulary[""]
print(f"Total words in the dictionary: {len(vocabulary.keys())}")
vocabulary = dict(sorted(vocabulary.items()))
for i in vocabulary:
    print(f"{i} :{vocabulary[i]}")