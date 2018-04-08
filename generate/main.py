from generate import Generator
from GeneratorInterface import GeneratorInterface


def main2():
    g = Generator()
    g.load_model_from_file('../model.json')
    g.set_length(10)
    print(g.generate())

def main():
    g = GeneratorInterface()
    g.interactive()



main()
