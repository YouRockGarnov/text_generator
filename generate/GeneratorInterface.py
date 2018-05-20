import argparse
from generate import Generator


class GeneratorInterface:
    def __init__(self):
        self._parser = argparse.ArgumentParser(description='Generate text with loaded model')
        self._parser.add_argument('--model', type=str, default='model.json',
                                  dest='model', help='a path to the file where the model is located')

        self._parser.add_argument('--seed', type=str,
                                  dest='seed', default='', help='a start word in a generated text')

        self._parser.add_argument('--length', type=str,
                                  dest='length', default=0, help='length of a generated text')

        self._parser.add_argument('--output', type=str,
                                  dest='output_path', default='a path to output file')

        self._parser.add_argument('--exit', action='store_true',
                                  dest='exit', default=False,
                                  help='if --exit exists then the program will end after these commands')

    def interactive(self):
        args = None

        while (True):
            try:
                inp = input().split()

                args = self._parser.parse_args(inp)
                self.run(args)

                if args.exit:
                    return

            except EOFError:
                return

    # run generator
    def run(self, args):
        gen = Generator()
        gen.length = args.length
        gen.seed = args.seed
        gen.model = args.model

        gen.load_model_from_file(gen._model)
        self._print(gen.generate(), args.output_path)

    # print a generated text in an output file
    @staticmethod
    def _print(text, output_path):
        if output_path == '':
            print(text)
        else:
            file = open(output_path, 'w')
            file.write(text)
