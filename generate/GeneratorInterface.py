import argparse
from train.generate import Generator

class GeneratorInterface:
    def __init__(self):
        self._parser = argparse.ArgumentParser(description='Generate text with loaded model')
        self._parser.add_argument('--model', type=str, default='model.json',
                                  dest='model', help='a path to the file where the model is located')

        self._parser.add_argument('--seed', type=str,
                                  dest='seed', default='')

        self._parser.add_argument('--length', type=str,
                                  dest='length', default=0)

        self._parser.add_argument('--output', type=str,
                                  dest='output_path', default='')

        # self._parser.add_argument('--run', action='store_true')

    def interactive(self):
        args = None

        while (True):
            try:
                inp = input().split()

                args = self._parser.parse_args(inp)
                self.run(args)

            except EOFError:
             return


    def run(self, args):
        gen = Generator()
        gen.set_length(args.length)
        gen.set_seed(args.seed)
        gen.set_model(args.model)

        # if args.output_path == ''

        gen.load_model_from_file(gen._model)
        self._print(gen.generate(), args.output_path)

    def _print(self, text, output_path):
        if output_path == '':
            print(text)
        else:
            file = open(output_path, 'w')
            file.write(text)
