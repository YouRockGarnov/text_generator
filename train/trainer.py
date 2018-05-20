import json
# from pymorphy2 import MorphAnalyzer as pm
import urllib
from collections import defaultdict


class Trainer:
    def __init__(self):
        self._frequency = defaultdict(int)
        self._words = list()

    # put a text in the file in the train system
    def put_file(self, name_of_file: str, lower_case: bool):  # working
        file = open(name_of_file, 'r')

        for line in file:
            if line == '':
                break

            line = self._clear_of_not_char(line)

            # if user set --ls (lower case)
            if lower_case:
                line = line.lower()

            self._words += line.split()

        print("Putting is done!")

    @staticmethod
    def put_site(url: str, lower_case: bool):
        response = urllib.urlopen('https://docs.python.org/2/howto/urllib2.html')
        html = response.read()

    @staticmethod
    def _clear_of_not_char(s: str):  # working
        return ''.join(char for char in s if char.isalnum() or char == ' ')

    def get_frequency_of_following(self):
        # self._normalized_words = self._normalized(self._words)

        # write frequency of word pairs (when one word is after another)
        for (word1, word2) in list(zip(self._words, self._words[1:])):
            s = word1 + '-' + word2
            self._frequency[s] += 1

    # set words in normal form
    @staticmethod
    def _normalized(words):
        answer = list()
        for word in words:
            print(morph.parse('plain'))
            answer.append(morph.parse(word)[0])

        return answer

    def record_model_in_file(self, name_of_file: str):
        json_f = open(name_of_file, 'w')
        json.dump(self._frequency, json_f)
