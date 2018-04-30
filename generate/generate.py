import json
import numpy


class Generator:
    def __init__(self):
        self._model = str()
        self._seed = ''
        self._length = 0
        self._path_to_output_file = ''

    # load frequency from file
    def load_model_from_file(self, path_to_file):
        json_f = open(path_to_file, 'r')
        self._frequency = json.load(json_f)

    # generate a text which has the length = self.length and based on the model
    def generate(self):
        rec_word = self._get_seed()
        answer = rec_word + ' '

        # generate length words
        for i in range(self._length):
            continuations = self._normalize(self._find_all_pairs(rec_word))

            # choose some word from suitable pairs
            choice = numpy.random.choice(len(continuations), 1, continuations.values())
            s = list(continuations.keys())[choice]
            answer += self.__word_of_pair(s, 2) + ' ' # second word in s + ' '

            rec_word = self.__word_of_pair(s, 2)  # get second word from s

        return answer

    # normalize the frequency relative to 1
    @staticmethod
    def _normalize(frequency: dict):
        mx = max(frequency.values())

        return dict([(pair[0], pair[1] / mx) for pair in frequency.items()])

    def get_length(self):
        return self._length

    def set_length(self, le):
        self._length = int(le)

    length = property(get_length, set_length)

    def get_seed(self):
        return self._seed

    def set_seed(self, val):
        self._seed = val

    seed = property(get_seed, set_seed)

    def get_model(self):
        return self._model

    def set_model(self, val):
        self._model = val

    model = property(get_model, set_model)

    def _get_seed(self):
        if self._seed != '':
            return self._seed
        else:
            index = numpy.random.choice(len(self._frequency), 1)
            return self.__word_of_pair(list(self._frequency.keys())[index], 1)

    # return <number> word in pair
    @staticmethod
    def __word_of_pair(pair, number):
        return pair.split('-')[number - 1]

    # return dict of pairs which meet with <word> in the model
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