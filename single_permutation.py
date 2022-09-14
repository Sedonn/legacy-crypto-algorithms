from math import ceil

class SinglePermutation:

    @staticmethod
    def __create_char_matrix(message: str, key: str, step: int, row_count: int) -> list:
        char_matrix: list = [[*message[i:i+step]] for i in range(0, len(key) * row_count, step)]
        for row in char_matrix:
            if len(row) < step:
                row += [''] * (step - len(row))

        return char_matrix

    @staticmethod
    def __transpose(matrix: list) -> list:
        return [*map(lambda x: [*x], [*zip(*matrix)])]

    @staticmethod
    def encode(message: str, key: str) -> str:
        row_count: int = ceil(len(message) / len(key))

        char_matrix: list = SinglePermutation.__create_char_matrix(message, key, row_count, row_count) 
        for index, row in enumerate(char_matrix):
            row.insert(0, key[index])

        char_matrix.sort(key=lambda x: x[0])
        char_matrix = SinglePermutation.__transpose(char_matrix)[1:]

        return ''.join(map(lambda x: ''.join(x), char_matrix))

    @staticmethod
    def decode(message: str, key: str) -> str:
        row_count: int = ceil(len(message) / len(key))
        encoded_key: str = sorted(key)

        char_matrix: list = SinglePermutation.__create_char_matrix(message, key, len(key), row_count)
        char_matrix = SinglePermutation.__transpose(char_matrix)
        for index, row in enumerate(char_matrix):
            row.insert(0, encoded_key[index])

        decoded_char_matrix = []
        for key_char in key:
            decoded_char_matrix.append(*filter(lambda x: x[0] == key_char, char_matrix))

        return ''.join(map(lambda x: ''.join(x[1:]), decoded_char_matrix))

# print(SinglePermutation.encode('ПЕВЕЦ БЛЕСТЯЩЕ ИСПОЛНИЛ ХИТ', 'ФОМКА'))
# print(SinglePermutation.decode('ВЫЕУАЕЙНЗВК ИЫТ ЧАКО ЕЛИР ЛЬ ОНГМ', 'ФОМКА'))