from math import ceil
import numpy as np


class PermutationCipher:
    '''
    Class for encoding and decoding strings with the Permutation cipher
    The cipher has two modes - horizontal and vertical
    Horizontal mode - chars of the message are record to matrix vertically and after encryption are reading horizontly
    Vertical mode - chars of the message are record to matrix horizontly and after encryption are reading vertically
    '''

    def __init__(self, vertical: bool = False) -> None:
        self._is_vertical = vertical
        pass

    def __create_char_matrix(self, message: str, key: str, col_len_equal_key: bool = False) -> np.ndarray:
        '''
        Create the matrix from message by length of key
        1. col_len_equal_key = False - a count of rows in matrix will be equal to length of key
        2. col_len_equal_key = True - a count of cols in matrix will be equal to length of key
        '''
        if not col_len_equal_key:
            row_count = len(key)
            col_count = ceil(len(message) / len(key))
        else:
            row_count = ceil(len(message) / len(key))
            col_count = len(key)
        # Create balancer with missing items for correct reshape
        shape = ((row_count * col_count) - len(message))
        balancer = np.full(shape, '_', dtype='U1')

        return np.array([*message, *balancer]).reshape(row_count, col_count)

    def __to_string(self, matrix: np.ndarray) -> str:
        '''Formate matrix to the string'''
        return ''.join(map(lambda x: ''.join(x), matrix))

    def encode(self, message: str, key: str) -> str:
        '''Rearrange a cols of the matrix by sequence indices of chars in sorted key appearing on the selected mode'''
        if self._is_vertical:
            # Creating a matrix with length of cols equal to length of key
            char_matrix = self.__create_char_matrix(
                message, key, col_len_equal_key=True)
        else:
            # Creating a matrix with length of rows equal to length of key and transpose it to vertical view of chars
            char_matrix = self.__create_char_matrix(message, key).T

        # Permutation cols
        char_matrix_encoded = char_matrix[:, np.argsort([*key])]

        if self._is_vertical:
            # Transpose matrix for vertical reading
            return self.__to_string(char_matrix_encoded.T)
        else:
            # Reading matrix horizontly
            return self.__to_string(char_matrix_encoded)

    def decode(self, message: str, key: str) -> str:
        '''
        Decode the message by back permutations
        To decode a matrix, it is necessary to find a sequence of indices, 
        which are such a sequence that bring back the sorted sequence of key chars
        to the original form of the key char sequence
        '''
        # Restore the matrix which are getted after encryption appear on the selected mode
        if self._is_vertical:
            char_matrix = self.__create_char_matrix(message, key).T
        else:
            char_matrix = self.__create_char_matrix(
                message, key, col_len_equal_key=True)

        # Finding the decode key
        sorted_key = np.sort([*key])
        decode_key = [int(*np.where(sorted_key == k_char)) for k_char in key]
        char_matrix_decoded = char_matrix[:, decode_key]

        if self._is_vertical:
            # Reading matrix horizontly
            return self.__to_string(char_matrix_decoded).replace('_', '')
        else:
            # Transpose matrix for vertical reading
            return self.__to_string(char_matrix_decoded.T).replace('_', '')


permutation_horizontal = PermutationCipher()
print('Encoded horizontally:', end=' ')
print(repr(permutation_horizontal.encode('WHAT THE BUATIFUL WORLD AROUND US', 'SUN')))
print('Decoded horizontally:', end=' ')
print(repr(permutation_horizontal.decode('DWA HTAAIRTFO UUTLNH DEW  OUBRSUL', 'SUN')))

permutation_vertical = PermutationCipher(vertical=True)
print('Encoded vertically:', end=' ')
print(repr(permutation_vertical.encode('ЧТО ЗА ЗАМЕЧАТЕЛЬНЫЙ МИР ВОКРУГ НАС', 'СОЛНЦЕ')))
print('Decoded vertically:', end=' ')
print(repr(permutation_vertical.decode('АЧНРУ_ОАЕ ОН МЛМКАТЗТЙВ Ч АЫ ГЗЕЬИРС', 'СОЛНЦЕ')))
