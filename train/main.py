from InterfaceTrainer import InterfaceTrainer
from trainer import Trainer
import urllib.request as url
import re

def main():
    itg = InterfaceTrainer(Trainer())
    itg.interactive()

def test():
    response = url.urlopen('https://docs.python.org/3/library/urllib.request.html#module-urllib.request')
    html = response.read()
    print(html)
    pattern = re.compile('<p>[\w\s<>/]+</p>')
    match = pattern.match('<p> lol <l> kek </l> ahah </p>')
    print(match.group())

    # tr.put_file('train/test.txt', True)
    # tr.get_frequency_of_following()
    # tr.record_model_in_file('mod.json')

main()