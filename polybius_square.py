from enum import Enum
from typing import Callable
import numpy as np


class Lang(Enum):
    '''Class for language settings'''

    ru = {
        'alphabet': 'АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ',
        'col_count': 6
    }
    en = {
        'alphabet': 'ABCDEFGHIKLMNOPQRSTUVWXYZ',
        'col_count': 5
    }


class PolybiusSquare:
    '''Class for encoding and decoding strings with the Polybius Square cipher'''

    def __init__(self, lang_key: str, horizontal: bool = False) -> None:
        try:
            lang = Lang[lang_key].value
        except KeyError:
            raise KeyError('Invalid language key!')
        else:
            self._lang = lang

        self._alphabet_matrix = self.__create_alphabet_matrix()
        self._alphabet_matrix_T = self._alphabet_matrix.T
        self._is_horizontal = horizontal
        pass

    def __create_alphabet_matrix(self) -> np.ndarray:
        '''Creating the matrix from alphabet with specific count of cols setted by lang'''
        return np \
            .array([*self._lang['alphabet']]) \
            .reshape((len(self._lang['alphabet']) // self._lang['col_count'], self._lang['col_count']))

    def __encode_char(self, matrix: np.ndarray, row_idx: int, col_idx: int) -> str:
        '''
        Transform a char from indices to right placed from it char
        If it placed in the end of a matrix row necessary to pick first element of row
        '''
        return matrix[row_idx][(col_idx + 1) % self._lang['col_count']]

    def __decode_char(self, matrix: np.ndarray, row_idx: int, col_idx: int) -> str:
        '''Transform a char from indices to left placed from it char'''
        return matrix[row_idx][col_idx - 1]

    def __get_char(self, char: int, char_transform: Callable[[np.ndarray, int, int], str]) -> str:
        '''
        Get char from alphabet matrix with options:
        is_horizontal = True - searching of a chars is performed in rows
        is_horizontal = False - searching of a chars is performed in cols
        '''
        if self._is_horizontal:
            char_indices = np.where(self._alphabet_matrix == char)
        else:
            char_indices = np.where(self._alphabet_matrix_T == char)

        # Return not changed char if it specical char
        if not char_indices[0].size:
            return char

        row_idx, col_idx = tuple(*zip(char_indices[0], char_indices[1]))

        if self._is_horizontal:
            return char_transform(self._alphabet_matrix, row_idx, col_idx)
        else:
            return char_transform(self._alphabet_matrix_T, row_idx, col_idx)

    def __prettify(self, message: str) -> str:
        '''Prettify message to compatibility wih key matrix'''
        return message.replace('Й', 'И').replace('Ё', 'Е').replace('J', 'I')

    def encode(self, message: str) -> str:
        '''Encode message with Polybius Square cipher'''
        prettified_message = self.__prettify(message)

        return ''.join(map(lambda x: self.__get_char(x, self.__encode_char), prettified_message))

    def decode(self, message: str) -> str:
        '''Decode message with Polybius Square cipher'''
        return ''.join(map(lambda x: self.__get_char(x, self.__decode_char), message))


polybius_en_vertical = PolybiusSquare('en')
polybius_en_horizontal = PolybiusSquare('en', horizontal=True)

polybius_ru_vertical = PolybiusSquare('ru')
polybius_ru_horizontal = PolybiusSquare('ru', horizontal=True)

print('Encoded with vertical and en:',
      polybius_en_vertical.encode('HELLO WORLD'))
print('Decoded with vertical and en:',
      polybius_en_vertical.decode('NKQQT BTWQI'))

print('Encoded with horizontal and en:',
      polybius_en_horizontal.encode('HELLO WORLD'))
print('Decoded with horizontal and en:',
      polybius_en_horizontal.decode('IAMMP XPSME'))

print('Encoded with vertical and ru:',
      polybius_ru_vertical.encode('ПРИВЕТ МИР'))
print('Decoded with vertical and ru:',
      polybius_ru_vertical.decode('ХЦПИМШ ТПЦ'))

print('Encoded with horizontal and ru:',
      polybius_ru_horizontal.encode('ПРИВЕТ МИР'))
print('Decoded with horizontal and ru:',
      polybius_ru_horizontal.decode('РСКГАН ЖКС'))