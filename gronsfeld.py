from enum import Enum
from itertools import cycle
from typing import Callable


class Lang(Enum):
    '''Class for language settings'''
    ru = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


class Gronsfeld:
    '''Class for encoding and decoding strings with the Gronsfeld cipher'''

    def __init__(self, lang_key: str) -> None:
        try:
            alphabet = Lang[lang_key].value
        except KeyError:
            raise KeyError('Invalid language key!')
        else:
            self._aplhabet = alphabet
            self._alph_len = len(alphabet)
        pass

    def __encode_char(self, index: int, step: int) -> str:
        '''Get encoded char by index by formula: Ei = (Ci + S) mod N, where N - alphabet length, S - step'''
        return self._aplhabet[(index + step) % self._alph_len]

    def __decode_char(self, index: int, step: int) -> str:
        '''Get decoded char by index by formula: Di = Ci - S, S - step'''
        return self._aplhabet[index - step]

    def __gronsfeld(self, char: str, step: int, char_transform: Callable[[int, int], str]) -> str:
        '''Transform char with Gronsfeld cipher by callable method'''
        index = self._aplhabet.find(char)
        # Ignoring non-alphabet chars and symbols
        if index == -1:
            return char

        return char_transform(index, step)

    def __prepare_message(self, message: str, key: str) -> list:
        '''Create list of tuples which contain chars and its own indices'''
        return [(char, int(step)) for char, step in zip(message, cycle(str(key)))]

    def encode(self, message: str, key: str) -> str:
        '''Encode message with Gronsfeld cipher'''
        prepared_message = self.__prepare_message(message, key)

        return ''.join(map(lambda x: self.__gronsfeld(x[0], x[1], self.__encode_char), prepared_message))

    def decode(self, message: str, key: str) -> str:
        '''Decode message with Gronsfeld cipher'''
        prepared_message = self.__prepare_message(message, key)

        return ''.join(map(lambda x: self.__gronsfeld(x[0], x[1], self.__decode_char), prepared_message))


gronsfeld_en = Gronsfeld('en')
gronsfeld_ru = Gronsfeld('ru')

print('Encoded:', gronsfeld_en.encode('HELLO WORLD', 1234))
print('Decoded:', gronsfeld_en.decode('IGOPP ZSSNG', 1234))

print('Encoded:', gronsfeld_ru.encode('ПРИВЕТ МИР', 1234))
print('Decoded:', gronsfeld_ru.decode('РТЛЖЖФ РЙТ', 1234))
