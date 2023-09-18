import string

def word_frequency(sentence):
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    sentence = sentence.lower()
    words = sentence.split()

    words_count = {}
    for word in words:
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1

    return words_count

sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
