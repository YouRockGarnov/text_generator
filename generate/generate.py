import json
import numpy

class Generator:
    def __init__(self):
        self._model = str()
        self._seed = ''
        self._length = 0
        self._path_to_output_file = ''

    def load_model_from_file(self, path_to_file):
        json_f = open(path_to_file, 'r')
        self._frequency = json.load(json_f)

    def generate(self):
        rec_word = self._get_seed()
        answer = rec_word + ' '

        for i in range(self._length):
            continuations = self._normalize(self._find_all_pairs(rec_word))

            choice = numpy.random.choice(len(continuations), 1, continuations.values())#p=continuations.values())
            s =  list(continuations.keys())[choice]
            answer += self.__word_of_pair(s, 2) + ' '

            rec_word = self.__word_of_pair(s, 2)

        return answer

    def _normalize(self, frequency: dict):
        mx = max(frequency.values())

        return dict([ (pair[0], pair[1] / mx) for pair in frequency.items() ])

    def set_length(self, le):
        self._length = int(le)

    def set_seed(self, val):
        self._seed = val

    def set_model(self, val):
        self._model = val

    def _get_seed(self):
        if self._seed != '':
            return self._seed
        else:
            index = numpy.random.choice(len(self._frequency), 1)
            return self.__word_of_pair(list(self._frequency.keys())[index], 1)

    def __word_of_pair(self, pair, number):
        return pair.split('-')[number - 1]

    def _find_all_pairs(self, word: str):
        keys = self._frequency.keys()

        answer = dict()
        for pair in keys:
            first_word = pair.split('-')[0]

            if first_word == word:
                answer[pair] = self._frequency[pair]

        return answer


    '''
    def _find_all_continuations(self):
        # keys = self._frequency.keys()

        keys = self._frequency.keys()
        answer = dict()
        for s in keys:
            pair = s.split('-')

            if answer.get(pair[0]) == None:
                answer[pair[0]] = [pair[1]]
            else:
                answer[pair[0]].append(pair[1])

        return answer
    '''