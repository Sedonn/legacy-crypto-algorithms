from enum import Enum
from typing import Callable
import numpy as np


class Lang(Enum):
    '''Class for language settings.'''

    RU = {
        'alphabet': 'АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ',
        'col_count': 6
    }
    EN = {
        'alphabet': 'ABCDEFGHIKLMNOPQRSTUVWXYZ',
        'col_count': 5
    }


class PolybiusSquare:
    '''Class for encoding and decoding strings with the Polybius Square cipher.'''

    def __init__(self, lang_key: str, horizontal: bool = False) -> None:
        try:
            lang = Lang[lang_key.upper()].value
        except KeyError as lang_error:
            raise KeyError('Invalid language key!') from lang_error
        else:
            self._lang = lang

        self._alphabet_matrix = self.__create_alphabet_matrix()
        self._alphabet_matrix_t = self._alphabet_matrix.T
        self._is_horizontal = horizontal
        pass

    def __create_alphabet_matrix(self) -> np.ndarray:
        '''Creating the matrix from alphabet with specific count of cols setted by lang.'''
        return np \
            .array([*self._lang['alphabet']]) \
            .reshape((len(self._lang['alphabet']) // self._lang['col_count'], self._lang['col_count']))

    def __encode_char(self, matrix: np.ndarray, row_idx: int, col_idx: int) -> str:
        '''
        Transform a char from indices to right placed from it char.
        If it is placed in the end of a matrix row it is necessary to pick first element of row.
        '''
        return matrix[row_idx][(col_idx + 1) % self._lang['col_count']]

    def __decode_char(self, matrix: np.ndarray, row_idx: int, col_idx: int) -> str:
        '''Transform a char from indices to left placed from it char.'''
        return matrix[row_idx][col_idx - 1]

    def __get_char(self, char: int, char_transform: Callable[[np.ndarray, int, int], str]) -> str:
        '''
        Get char from alphabet matrix with options:
        1. is_horizontal = True - search of a chars is performed in rows.
        2. is_horizontal = False - search of a chars is performed in cols.
        '''
        if self._is_horizontal:
            char_indices = np.where(self._alphabet_matrix == char)
        else:
            char_indices = np.where(self._alphabet_matrix_t == char)

        # Return not changed char if it is specical char
        if not char_indices[0].size:
            return char

        row_idx, col_idx = tuple(*zip(char_indices[0], char_indices[1]))

        if self._is_horizontal:
            return char_transform(self._alphabet_matrix, row_idx, col_idx)
        else:
            return char_transform(self._alphabet_matrix_t, row_idx, col_idx)

    def __prettify(self, message: str) -> str:
        '''Prettify a message to compatibility with key matrix.'''
        return message.replace('Й', 'И').replace('Ё', 'Е').replace('J', 'I')

    def encode(self, message: str) -> str:
        '''Encode a message with the Polybius Square cipher.'''
        prettified_message = self.__prettify(message)

        return ''.join(map(lambda x: self.__get_char(x, self.__encode_char), prettified_message))

    def decode(self, message: str) -> str:
        '''Decode message with the Polybius Square cipher.'''
        return ''.join(map(lambda x: self.__get_char(x, self.__decode_char), message))


polybius_en_vertical = PolybiusSquare('en')
polybius_en_horizontal = PolybiusSquare('en', horizontal=True)

polybius_ru_vertical = PolybiusSquare('ru')
polybius_ru_horizontal = PolybiusSquare('ru', horizontal=True)

print('Encoded vertically en:',
      polybius_en_vertical.encode('HELLO WORLD'))
print('Decoded vertically en:',
      polybius_en_vertical.decode('NKQQT BTWQI'))

print('Encoded horizontally en:',
      polybius_en_horizontal.encode('HELLO WORLD'))
print('Decoded horizontally en:',
      polybius_en_horizontal.decode('IAMMP XPSME'))

print('Encoded vertically ru:',
      polybius_ru_vertical.encode('ПРИВЕТ МИР'))
print('Decoded vertically ru:',
      polybius_ru_vertical.decode('ХЦПИМШ ТПЦ'))

print('Encoded horizontally ru:',
      polybius_ru_horizontal.encode('ПРИВЕТ МИР'))
print('Decoded horizontally ru:',
      polybius_ru_horizontal.decode('РСКГАН ЖКС'))
