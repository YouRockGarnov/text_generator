import json
# from pymorphy2 import MorphAnalyzer as pm
from collections import defaultdict
import os


class Trainer:
    def __init__(self):
        self._frequency = defaultdict(lambda: defaultdict(int))
        self._words = list()

    # put a text in the file in the train system
    def put_file(self, name_of_dir: str, lower_case: bool):  # working
        for filename in os.listdir(name_of_dir):
            with open(name_of_dir + filename) as file:
                for line in file:
                    if line == '':
                        break

                    line = self._clear_of_not_char(line)

                    # if user set --ls (lower case)
                    if lower_case:
                        line = line.lower()

                    self._words += line.split()

                self._words.pop()

        print("Putting is done!")

    @staticmethod
    def _clear_of_not_char(s: str):  # working
        return ''.join(char for char in s if char.isalnum() or char == ' ')

    def get_frequency_of_following(self):
        # self._normalized_words = self._normalized(self._words)

        # write frequency of word pairs (when one word is after another)
        for (word1, word2) in list(zip(self._words, self._words[1:])):
            self._frequency[word1][word2] += 1

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
