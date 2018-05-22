import json
import numpy


class Generator:
    def __init__(self):
        self._model = str()
        self._seed = ''
        self._length = 0
        self._path_to_output_file = ''
        self._frequency = None

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
            continuations = self._normalize(self._frequency[rec_word])

            # find some word from suitable pairs
            probability = list(continuations.values())
            choice = numpy.random.choice(len(probability), 1, p=probability)

            # choose word
            choiced_str = list(continuations)[choice]
            answer += choiced_str + ' '

            rec_word = choiced_str

        return answer

    # normalize the frequency relative to 1
    @staticmethod
    def _normalize(frequency: dict):
        full = sum(frequency.values())

        # return dict([(pair[0], pair[1] / mx) for pair in frequency.items()])
        # frequency = list(map(lambda neighbors: map(lambda x: x / mx, neighbors), frequency.values()))
        for item in frequency.items():
            frequency.update({item[0]: item[1] / full})
        return frequency

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
            return list(self._frequency.keys())[index]

    # return <number> word in pair
    @staticmethod
    def __word_of_pair(pair, number):
        return pair.split('-')[number - 1]
