class Visioner:

    ALPHABET = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

    @staticmethod
    def __get_indices(message_char: str, message_char_index: int, key: str) -> tuple:
        return (Visioner.ALPHABET.find(message_char), Visioner.ALPHABET.find(key[message_char_index % len(key)]))

    @staticmethod
    def __encode_char(message_char: str, message_char_index: int, key: str) -> str:
        indices = Visioner.__get_indices(message_char, message_char_index, key)
        char_index = (indices[0] + indices[1]) % len(Visioner.ALPHABET)

        return Visioner.ALPHABET[char_index]

    @staticmethod
    def __decode_char(message_char: str, message_char_index: int, key: str) -> str:
        indices = Visioner.__get_indices(message_char, message_char_index, key)
        char_index = indices[0] - indices[1] + (len(Visioner.ALPHABET) if indices[0] - indices[1] < 0 else 0)

        return Visioner.ALPHABET[char_index]

    @staticmethod
    def encode(message: str, key: str) -> str:
        return ''.join(map(lambda x: Visioner.__encode_char(x[1], x[0], key), enumerate(message.replace(' ', ''))))

    @staticmethod
    def decode(message: str, key: str) -> str:
        return ''.join(map(lambda x: Visioner.__decode_char(x[1], x[0], key), enumerate(message.replace(' ', ''))))


# print(Visioner.encode('НЕКОТОРЫЕ ДАЖЕ УТВЕРЖДАЛИ ЧТО ЕДИНСТВЕННАЯ СТРАСТЬ ХОББИТОВ ЭТО ЕДА', 'МИР'))
# print(Visioner.decode('МЫЬМЪЭХЩРНДЬНЧЬИБЯЦРРЪСЭШНУДНТЮНУЫЙЛШЧВЧЩЛЯЕААРЛЭЕВОЧФЧЧЪ', 'МИР'))
