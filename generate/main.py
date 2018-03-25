from generate import Generator


def main():
    g = Generator()
    g.load_model_from_file('../model.json')
    g.set_length(10)
    print(g.generate())

main()
