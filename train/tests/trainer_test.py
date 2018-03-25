from train.trainer import Trainer
import random

class TrainerTest:
    def __init__(self):

    def test_put_file(self):
        name_of_file = 'train/test_put_file.txt'
        file = open(name_of_file, 'w')

        chars = '`1234567890-=qwertyuiop[]\asdfghjkl;\'zxcvbnm,./~!@#$%^&*()_+' \
                'QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>?\n\n\n\n\n        \t\t\t'

        file_input = str()
        for i in range(10000):
            file_input += random.choice(chars)



    def test_clear(self):
