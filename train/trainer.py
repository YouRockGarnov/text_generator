import json


class Trainer:
    def __init__(self):
        self._frequency = dict()
        self._words = list()

    def put_file(self, name_of_file: str, lower_case: bool): # working
        file = open(name_of_file, 'r')

        while True:
            try:
                s = file.readline()
                if s == '':
                    break

                s = self._clear_of_not_char(s)

                if lower_case:
                    s = s.lower()

                self._words += s.split()

            except EOFError:
                break

        print("Putting is done!")

    def _clear_of_not_char(self, s: str): # working
        return ''.join(char for char in s if char.isalnum() or char == ' ')

    def get_frequency_of_following(self):

        for i in range(len(self._words) - 1):
            word1 = self._words[i]
            word2 = self._words[i + 1]

            s = word1 + '-' + word2
            if(self._frequency.get(s) == None):
                self._frequency[s] = 1
            else:
               self._frequency[s] += 1

    def record_model_in_file(self, name_of_file: str):
        json_f = open(name_of_file, 'w')
        json.dump(self._frequency, json_f)
