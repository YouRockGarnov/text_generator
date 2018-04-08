from trainer import Trainer

class InterfaceTrainer:
    def __init__(self, trainer: Trainer):
        self._trainer = trainer
        self._lower_case = False

    def interactive(self):
        filled_model = False
        filled_input_dir = False

        while(True):
            try:
                inp = input().split()
                for i in range(len(inp)):

                    if inp[i] == '--input-dir':
                        self._input_dir_file()
                        filled_input_dir = True

                    elif inp[i] == '--model':
                        self._model()
                        filled_model = True

                    elif inp[i] == '--lc':
                        self._lower_case == True

                    elif inp[i] == '--help':
                        self._help()

                    elif inp[i] == '--run':
                        if filled_input_dir and filled_model:
                            self._run()
                        else:
                            print('Fill --input-dir and --model, please!')

            except EOFError:
             return

    def _input_dir_file(self):
        self._input_file = input()

    def _model(self):
        self._model_path = input()

    def _help(self):
        pass

    def _run(self):
        self._trainer.put_file(self._input_file, self._lower_case)
        self._trainer.get_frequency_of_following()
        self._trainer.record_model_in_file(self._model_path)
