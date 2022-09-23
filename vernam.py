import binascii
import itertools


class Vernam:
    '''Class for encoding and decoding strings with the Vernam cipher.'''

    @staticmethod
    def __xor_str(message: str, key: str) -> str:
        '''Function for "xor" of the all string with specific key.'''
        def __xor(first: str, second: str) -> str:
            '''Function for "xor" of two chars.'''
            return chr(ord(first) ^ ord(second))

        return ''.join([__xor(m_char, k_char) for m_char, k_char in zip(message, itertools.cycle(key))])

    @staticmethod
    def encode(message: str, key: str) -> str:
        '''Encode the message with "xor" and encode a result to hex with UTF-8 encoding for correct display.'''
        encoded_message = Vernam.__xor_str(message, key)
        return binascii.hexlify(encoded_message.encode()).decode(encoding='utf-8')

    @staticmethod
    def decode(message: str, key: str) -> str:
        '''Decode a hex to string with UTF-8 and "xor" it.'''
        unhexed = binascii.unhexlify(message.encode()).decode(encoding='utf-8')
        return Vernam.__xor_str(unhexed, key)


print('Encoded:', Vernam.encode('Hello world', 'sun'))
print('Decoded:', Vernam.decode('3b10021f1a4e041a1c1f11', 'sun'))
