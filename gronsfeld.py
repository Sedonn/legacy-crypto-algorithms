from itertools import cycle


class Gronsfeld:
    APLHABET = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    MODE_ENCODE = 'encode'
    MODE_DECODE = 'decode'

    @staticmethod
    def __get_char(index) -> str:
        if index >= len(Gronsfeld.APLHABET):
            return Gronsfeld.APLHABET[abs(len(Gronsfeld.APLHABET) - index)]
        else:
            return Gronsfeld.APLHABET[index]

    @staticmethod
    def __tranform_char(char: str, step: int, mode: str) -> str:
        index = Gronsfeld.APLHABET.find(char)
        if index != -1:
            if mode == Gronsfeld.MODE_DECODE:
                return Gronsfeld.__get_char(index - step)
            elif mode == Gronsfeld.MODE_ENCODE:
                return Gronsfeld.__get_char(index + step)
        else:
            return char

    @staticmethod
    def __prepare_message(message: str, key: str) -> list:
        return [(char, int(step)) for char, step in zip(message, cycle(key))]

    @staticmethod
    def encode_zip(message: str, key: str) -> str:
        return ''.join(map(lambda x: Gronsfeld.__tranform_char(x[0], x[1], Gronsfeld.MODE_ENCODE), Gronsfeld.__prepare_message(message, key)))

    @staticmethod
    def decode_zip(message: str, key: str) -> str:
        return ''.join(map(lambda x: Gronsfeld.__tranform_char(x[0], x[1], Gronsfeld.MODE_DECODE), Gronsfeld.__prepare_message(message, key)))


# GRONSFELD_MESSAGE = 'МАЛ КЛОП, ДА ВОНЮЧ'
# GRONSFELD_KEY = '5345621'

# print('Encoded:', Gronsfeld.encode_zip(GRONSFELD_MESSAGE, GRONSFELD_KEY))