from enum import Enum
from typing import Callable


class Lang(Enum):
    '''Class for language settings.'''

    RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    EN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


class Visioner:
    '''Class for encoding and decoding strings with the Visioner cipher.'''

    def __init__(self, lang_key: str) -> None:
        try:
            alphabet = Lang[lang_key.upper()].value
        except KeyError as lang_error:
            raise KeyError('Invalid language key!') from lang_error
        else:
            self._alphabet: str = alphabet
            self._alph_len = len(self._alphabet)
        pass

    def __encode_char(self, char_index: int, key_index: int) -> str:
        '''Get a encoded char by index by formula: Ei = (Ci + Ki) mod N, where N - alphabet length.'''
        return self._alphabet[(char_index + key_index) % self._alph_len]

    def __decode_char(self, char_index: int, key_index: int) -> str:
        '''Get a decoded char by index by formula: Di = Ci - Ki, where N - alphabet length.'''
        return self._alphabet[char_index - key_index]

    def __get_indices(self, index: int, char: str, key: str) -> tuple:
        '''Find indices of a char and a key char in alphabet'''
        char_alph_index = self._alphabet.find(char)
        if char_alph_index == -1:
            return -1

        return (char_alph_index, self._alphabet.find(key[index % len(key)]))

    def __visioner(self, index: int, char: str, key: str, char_transform: Callable[[int, int], str]) -> str:
        '''Transform char with Visioner cipher by callable method.'''
        indices = self.__get_indices(index, char, key)
        # Ignoring non-alphabet chars and symbols
        if indices == -1:
            return char

        return char_transform(*indices)

    def encode(self, message: str, key: str) -> str:
        '''Encode message with Visioner cipher.'''
        return ''.join(map(lambda x: self.__visioner(x[0], x[1], key, self.__encode_char), enumerate(message)))

    def decode(self, message: str, key: str) -> str:
        '''Decode message with Visioner cipher.'''
        return ''.join(map(lambda x: self.__visioner(x[0], x[1], key, self.__decode_char), enumerate(message)))


visioner_en = Visioner('en')
print('Encoded en:', end=' ')
print(visioner_en.encode('WHAT THE BUATIFUL WORLD AROUND US', 'SUN'))
print('Decoded en:', end=' ')
print(visioner_en.decode('OBNL GZY TONLCSMF OIEDX SLBMHQ OF', 'SUN'))

visioner_ru = Visioner('ru')
print('Encoded ru:', end=' ')
print(visioner_ru.encode('ЧТО ЗА ЗАМЕЧАТЕЛЬНЫЙ МИР ВОКРУГ НАС', 'СОЛНЦЕ'))
print('Decoded ru:', end=' ')
print(visioner_ru.decode('ИБЪ ЮЕ ЦЛЪЫЬСБРЩТТМШ ЪЯХ РЪШЖШФ ЩНЗ', 'СОЛНЦЕ'))
