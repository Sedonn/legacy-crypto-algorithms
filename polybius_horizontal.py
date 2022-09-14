class Polybius:
    ALPHABET = [
        ['А', 'Б', 'В', 'Г', 'Д', 'Е'],
        ['Ж', 'З', 'И', 'К', 'Л', 'М'],
        ['Н', 'О', 'П', 'Р', 'С', 'Т'],
        ['У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш'],
        ['Щ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
    ]
    ENCODE_MODE = 1
    DECODE_MODE = -1

    @staticmethod
    def __get_char(char: str, mode: int) -> str:
        for row_index, row in enumerate(Polybius.ALPHABET):
            for col_index, col in enumerate(row):
                if col.find(char) != -1:
                    if mode == Polybius.ENCODE_MODE:
                        return Polybius.ALPHABET[row_index][0] if col_index > 4 else Polybius.ALPHABET[row_index][col_index + 1]
                    elif mode == Polybius.DECODE_MODE:
                        return Polybius.ALPHABET[row_index][col_index - 1]
        return char

    @staticmethod
    def __prettify(message: str) -> str:
        return message.replace('Й', 'И').replace('Ё', 'Е').replace('Й', 'И')

    @staticmethod
    def encode(message: str) -> str:
        return ''.join(map(lambda x: Polybius.__get_char(x, Polybius.ENCODE_MODE), Polybius.__prettify(message)))

    @staticmethod
    def decode(message: str) -> str:
        return ''.join(map(lambda x: Polybius.__get_char(x, Polybius.DECODE_MODE), Polybius.__prettify(message)))


# print('Зашифрованный текст:', Polybius.encode('ПРИВЕТ МИР'))
# print('Расшифрованный текст:', Polybius.decode('РСКГАН ЖКС'))
