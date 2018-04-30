from InterfaceTrainer import InterfaceTrainer
from trainer import Trainer


def main_train():
    itg = InterfaceTrainer(Trainer())
    itg.interactive()


main_train()
