from trainer import Trainer
import argparse

class InterfaceTrainer:
    def __init__(self, trainer: Trainer):
        self._trainer = trainer
        self._lower_case = False
        self._parser = argparse.ArgumentParser(description='Train model with loaded text')

        self._parser.add_argument('--input-dir', type=str,
                                  dest='input_path', default='')

        self._parser.add_argument('--model', type=str,
                                  dest='model', default='')

        self._parser.add_argument('--lc', action='store_true',
                                  dest='lower_case', default=False)

        self._parser.add_argument('--load-site', type=str,
                                  dest='site_file', default='')

    def interactive(self):
        args = None

        while (True):
            try:
                inp = input().split()

                args = self._parser.parse_args(inp)
                self._run(args)

            except EOFError:
             return

    def _input_dir_file(self):
        self._input_file = input()

    def _model(self):
        self._model_path = input()

    def _help(self):
        pass

    def _run(self, args):
        if args.input_path != '':
            self._trainer.put_file(args.input_path, args.lower_case)
        else:
            sel

        self._trainer.get_frequency_of_following()
        self._trainer.record_model_in_file(args.model)
