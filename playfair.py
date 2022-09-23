from enum import Enum
from typing import Callable

import numpy as np


class Lang(Enum):
    '''Class for language settings'''

    RU = {
        'alphabet': 'АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ',
        'insert_char': 'Х',
        'col_count': 6
    }
    EN = {
        'alphabet': 'ABCDEFGHIKLMNOPQRSTUVWXYZ',
        'insert_char': 'X',
        'col_count': 5
    }


class Bigrams:
    '''Class for creating bigrams'''

    def __init__(self, message: str) -> None:
        self.msg = message
        pass

    def __prettify(self) -> None:
        '''Prettify message to compatibility with key matrix'''
        self.msg = self.msg.replace('Й', 'И')\
            .replace('Ё', 'Е')\
            .replace('J', 'I')
        pass

    def slice(self) -> str:
        '''Creating string of bigrams - 'AABBCC' -> 'AA BB CC'''
        bigrams = [self.msg[i:i + 2] for i in range(0, len(self.msg), 2)]
        return ' '.join(bigrams)

    def prepare(self, insert_char: str):
        '''
        Prepare bigrams before encryption.
        Fill bigrams with inserting symbol at places where:
        1. Bigram has equal elements: AA BC -> AX AB C
        2. Bigram has only one element: AX AB C -> AX AB AX
        '''
        def insert_symbol(bigrams: str) -> str:
            result: str = ''
            for i in range(0, len(bigrams), 2):
                if i != len(bigrams) - 1:
                    if bigrams[i] == bigrams[i + 1]:
                        result += bigrams[i] + insert_char
                        # String of bigrams is changed and nessecary to check it from start
                        return insert_symbol(result + bigrams[i + 1:])
                    else:
                        result += bigrams[i:i + 2]
                else:
                    # One element could be only in the end of bigrams string
                    result += bigrams[i]
                    result += insert_char if len(result) % 2 != 0 else ''

            return result

        self.__prettify()
        self.msg = insert_symbol(self.msg)

        return self


class Playfair:
    '''Class for encoding and decoding strings with the Playfair cipher'''

    def __init__(self, lang_key: str) -> None:
        try:
            lang = Lang[lang_key.upper()].value
        except KeyError as lang_error:
            raise KeyError('Invalid language key!') from lang_error
        else:
            self._lang = lang

        self._bigrams = None
        self._key_matrix = None
        self._key_matrix_t = None

    def __create_key_matrix(self, key: str) -> np.ndarray:
        '''Creating the key matrix from key and alphabet'''
        key_matrix = key
        # Filling the matrix with alphabet chars without key chars
        for char in self._lang['alphabet']:
            if char not in key_matrix:
                key_matrix += char

        # Slice string to the matrix with specific count of cols
        return np.array([*key_matrix]).reshape((len(key_matrix) // self._lang['col_count'], self._lang['col_count']))

    def __find_bigram_in(self, matrix: np.ndarray, bigram: str, all_matrix: bool = False):
        '''
        Searching the bigram in matrix with options:
        1. all_matrix = False - search a bigram items which are placed in one row
        2. all_matrix = True  - search a bigram items through all matrix
        '''
        bigram0 = np.where(matrix == bigram[0])
        bigram0 = tuple(*zip(bigram0[0], bigram0[1]))

        bigram1 = np.where(matrix == bigram[1])
        bigram1 = tuple(*zip(bigram1[0], bigram1[1]))

        if all_matrix:
            return [bigram0, bigram1]

        return [bigram0, bigram1] if bigram0[0] == bigram1[0] else -1

    def __encode_char(self, matrix: np.ndarray, row_idx: int, col_idx: int) -> str:
        '''
        Transform a char from indices to right placed from it char
        If it placed in the end of a matrix row necessary to pick first element of row
        '''
        return matrix[row_idx][(col_idx + 1) % self._lang['col_count']]

    def __decode_char(self, matrix: np.ndarray, row_idx: int, col_idx: int) -> str:
        '''Transform a char from indices to left placed from it char'''
        return matrix[row_idx][col_idx - 1]

    def __playfair(self, key: str, char_transform: Callable[[np.ndarray, int, int], str]):
        '''
        Playfair algorithm
        Rule 2: If the chars appear on the same row, replace them with the chars to their immediate right respectively
        Rule 3: If the chars appear on the same column, replace them with the chars immediately below respectively
        Rule 4: If Rule 2-3 not find, replace chars with the chars on the same row respectively
        but at the other pair of corners of the rectangle defined by the original pair
        '''
        self._key_matrix = self.__create_key_matrix(key)
        self._key_matrix_t = self._key_matrix.T

        msg = ''
        for bigram in self._bigrams.split(' '):
            # Rule 2
            b_indices = self.__find_bigram_in(self._key_matrix, bigram)
            if b_indices != -1:
                msg += char_transform(
                    self._key_matrix, b_indices[0][0], b_indices[0][1])
                msg += char_transform(
                    self._key_matrix, b_indices[1][0], b_indices[1][1])
                continue

            # Rule 3
            b_indices = self.__find_bigram_in(self._key_matrix_t, bigram)
            if b_indices != -1:
                msg += char_transform(
                    self._key_matrix_t, b_indices[0][0], b_indices[0][1])
                msg += char_transform(
                    self._key_matrix_t, b_indices[1][0], b_indices[1][1])
                continue

            # Rule 4
            b_indices = self.__find_bigram_in(
                self._key_matrix, bigram, all_matrix=True)
            msg += self._key_matrix[b_indices[0][0], b_indices[1][1]]
            msg += self._key_matrix[b_indices[1][0], b_indices[0][1]]

        return msg

    def encode(self, text: str, key: str) -> str:
        '''Encode message with the Playfair cipher'''
        self._bigrams = Bigrams(text)\
            .prepare(self._lang['insert_char']).slice()

        return self.__playfair(key, self.__encode_char)

    def decode(self, text: str, key: str) -> str:
        '''Decode message with the Playfair cipher'''
        self._bigrams = Bigrams(text).slice()

        return self.__playfair(key, self.__decode_char)


playfair_en = Playfair('en')
playfair_ru = Playfair('ru')

print('Encoded en:', playfair_en.encode(
    'IDIOCYOFTENLOOKSLIKEINTELLIGENCE', 'WHEATSON'))
print('Decoded en:', playfair_en.decode(
    'KFFBBZFMWASPNVCFDUKDAGCEWPQDPNBSNE', 'WHEATSON'))

print('Encoded ru:', playfair_ru.encode('ПРИВЕТМИР', 'КЛАД'))
print('Decoded ru:', playfair_ru.decode('РСМБМОГМПЦ', 'КЛАД'))
