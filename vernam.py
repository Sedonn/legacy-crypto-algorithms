import binascii
import itertools


class Vernam:

    @staticmethod
    def __xor_str(message: str, key: str) -> str:
        def __xor(first: str, second: str) -> str:
            return chr(ord(first) ^ ord(second))

        return ''.join([__xor(m_char, k_char) for m_char, k_char in zip(message, itertools.cycle(key))])

    @staticmethod
    def encode(message: str, key: str) -> str:
        message = Vernam.__xor_str(message, key)
        return binascii.hexlify(message.encode()).decode(encoding='utf-8')

    @staticmethod
    def decode(message: str, key: str) -> str:
        message = binascii.unhexlify(message.encode()).decode(encoding='utf-8')
        return Vernam.__xor_str(message, key)

# ENCODED_MESSAGE = 'd08cd1b0d1a6d09377017c067170d1a3d09ed0940d010dd0947f7d7c0678017f750fd1a301d0947d0005097e7fd0930875027101d1a071d0930903750e0a75d1a30174757f7cd09a'
# ENCODED_MESSAGE_KEY = 'друг'
# MESSAGE = 'Hello world!'

# decoded_message: str = Vernam.decode(ENCODED_MESSAGE, ENCODED_MESSAGE_KEY)
# encoded_message: str = Vernam.encode(MESSAGE, decoded_message)
# print(f'Pасшифрованное сообщение: {decoded_message}')
# print(f'Засшифрованное сообщение: {encoded_message}')