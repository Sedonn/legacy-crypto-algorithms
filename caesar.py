from enum import Enum
from typing import Callable


class Lang(Enum):
    '''Class for language settings'''

    ru = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


class Caesar:
    '''Class for encoding and decoding strings with the Caesar cipher'''

    def __init__(self, lang_key: str, step: int) -> None:
        try:
            alphabet = Lang[lang_key].value
        except KeyError:
            raise KeyError('Invalid language key!')
        else:
            self._alphabet = alphabet
            self._alph_len = len(alphabet)
        self.step = step
        pass

    def __encode_char(self, index: int) -> str:
        '''Get encoded char by index by formula: Ei = (Ci + S) mod N, where N - alphabet length, S - step'''
        return self._alphabet[(index + self.step) % self._alph_len]

    def __decode_char(self, index: int) -> str:
        '''Get decoded char by index by formula: Di = Ci - S, S - step'''
        return self._alphabet[index - self.step]

    def __caesar(self, char: str, char_transform: Callable[[int], str]) -> str:
        '''Transform char with Caesar cipher by callable method'''
        index = self._alphabet.find(char)
        # Ignoring non-alphabet chars and symbols
        if index == -1:
            return char

        return char_transform(index)

    def encode(self, message: str) -> str:
        '''Encode message with Caesar cipher'''
        return ''.join(map(lambda x: self.__caesar(x, self.__encode_char), message))

    def decode(self, message: str) -> str:
        '''Decode message with Caesar cipher'''
        return ''.join(map(lambda x: self.__caesar(x, self.__decode_char), message))


caesar_en = Caesar('en', 5)
caesar_ru = Caesar('ru', 5)

print('Encoded:', caesar_en.encode('HELLO WORLD'))
print('Decoded:', caesar_en.decode('MJQQT BTWQI'))

print('Encoded:', caesar_ru.encode('ПРИВЕТ МИР'))
print('Decoded:', caesar_ru.decode('ФХНЗКЧ СНХ'))
