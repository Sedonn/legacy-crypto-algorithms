class Caesar:
    APLHABET = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    MODE_ENCODE = 'encode'
    MODE_DECODE = 'decode'

    @staticmethod
    def __get_char(index) -> str:
        if index >= len(Caesar.APLHABET):
            return Caesar.APLHABET[abs(len(Caesar.APLHABET) - index)]
        else:
            return Caesar.APLHABET[index]

    @staticmethod
    def __tranform_char(char: str, step: int, mode: str) -> str:
        index = Caesar.APLHABET.find(char)
        if index != -1:
            if mode == Caesar.MODE_DECODE:
                return Caesar.__get_char(index - step)
            elif mode == Caesar.MODE_ENCODE:
                return Caesar.__get_char(index + step)
        else:
            return char

    @staticmethod
    def encode(message: str, step: int) -> str:
        return ''.join(map(lambda x: Caesar.__tranform_char(x, step, Caesar.MODE_ENCODE), message))

    @staticmethod
    def decode(message: str, step: int) -> str:
        return ''.join(map(lambda x: Caesar.__tranform_char(x, step, Caesar.MODE_DECODE), message))


# CAESAR_MESSAGE = 'ЧКОВЙЦЦЧМЧ ЫЩС МЧНЙ ПНЬЫ'
# print('Decoded:', Caesar.decode(CAESAR_MESSAGE, 9))