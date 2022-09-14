from math import ceil
from itertools import permutations

class VercticalPermutation:
    
    @staticmethod
    def __create_char_matrix(message: str, key: str, step: int, row_count: int) -> list:
        char_matrix: list = [[*message[i:i+step]] for i in range(0, len(key) * row_count, step)]
        for row in char_matrix:
            if len(row) < step:
                row += ['-'] * (step - len(row))

        return char_matrix

    @staticmethod
    def __transpose(matrix: list) -> list:
        return [*map(lambda x: [*x], [*zip(*matrix)])]

    @staticmethod
    def __create_combinations(key: str) -> list:
        NUMBERS: set = set(map(lambda x: str(x), range(1, 10)))

        known_numbers: set = set(filter(str.isdigit, key))
        unknown_numbers_count: int = len([*filter(lambda x: x == 'X', key)])
        combination_numbers: set = NUMBERS.difference(known_numbers)

        combinations: list = [''.join(p) for p in permutations(combination_numbers, unknown_numbers_count)]
        keys = []
        for combination in combinations:
            full_key = key
            for value in combination:
                full_key = full_key.replace('X', value, 1)
            
            keys.append(full_key)

        return keys

    @staticmethod
    def encode(message: str, key: str) -> str:
        row_count: int = ceil(len(message) / len(key))
        char_matrix: list = VercticalPermutation.__create_char_matrix(message, key, len(key), row_count)
        char_matrix.insert(0, [*key])

        char_matrix = VercticalPermutation.__transpose(char_matrix)
        char_matrix.sort(key = lambda x: x[0])

        return ''.join(map(lambda x: ''.join(x[1:]), char_matrix))

    @staticmethod
    def __decode_matrix(char_matrix: list, key: str) -> str:
        char_matrix = VercticalPermutation.__transpose(char_matrix)
        char_matrix.insert(0, sorted(key))
        char_matrix = VercticalPermutation.__transpose(char_matrix)

        decoded_char_matrix = []
        for key_char in key:
            decoded_char_matrix.append(*filter(lambda x: x[0] == key_char, char_matrix))

        decoded_char_matrix = VercticalPermutation.__transpose(decoded_char_matrix)[1:]

        return ''.join(map(lambda x: ''.join(x), decoded_char_matrix))

    @staticmethod
    def decode(message: str, key: str) -> list:
        row_count: int = ceil(len(message) / len(key))
        char_matrix: list = VercticalPermutation.__create_char_matrix(message, key, row_count, row_count)

        decoded_messages: list = []
        for combination in VercticalPermutation.__create_combinations(key):
            decoded_messages.append({
                'text': VercticalPermutation.__decode_matrix(char_matrix[:], combination).replace('_', ' '),
                'key': combination
            })

        return decoded_messages


# decoded_messages = VercticalPermutation.decode('П_Я__М_КВ_ТВУОНХЛТДНООКИСЛ__ИНВА_УООЛОЕМИМЗЫС_ОЗГ_ИЛКАИ.А,ЕЕНА,ТО_ЯОС_РИ_ЗВ_ТТЕДР_ШЕВ_ДМОЛ__ЙО_ДВ_', '1XX4XX7')
# for msg in decoded_messages:
#     print('Сообщение: ', msg['text'], '\nКлюч: ', msg['key'])