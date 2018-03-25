from InterfaceTextGenerator import InterfaceTextGenerator
from trainer import Trainer

def main():

    itg = InterfaceTextGenerator(Trainer())
    itg.interactive()


    tr = Trainer()

    #tr.put_file('train/test.txt', True)
   # tr.get_frequency_of_following()
    #tr.record_model_in_file('mod.json')

main()