import nltk
nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()
import numpy as np

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower()) # to covert the word to lowercase

def bag_of_words(tokenize_sentence, all_words):
    tokenize_sentence = [stem(w) for w in tokenize_sentence]
    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx, w in enumerate(all_words):
        if w in tokenize_sentence:
            bag[idx] = 1.0
    return bag


# sentence = ["hello", "how", "are", "you"]
# words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
# bog = bag_of_words(sentence, words)
# print(bog)

# a = "How are you doing?"
# print(a)
# a = tokenize(a)
# print(a)

# word = ["Organize", "organizes", "organizing"]
# stemmed_words = [stem(w) for w in words]
# print(stemmed_words)