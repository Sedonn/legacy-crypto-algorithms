class Playfair:
    APLHABET: str = 'АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ'
    char_matrix: list = []

    @staticmethod
    def __create_char_matrix(word: str) -> None:
        matrix: str = word
        for char in Playfair.APLHABET:
            if matrix.find(char) == -1:
                matrix += char

        for char_index in range(0, len(matrix), 6):
            Playfair.char_matrix.append(list(matrix[char_index: char_index + 6]))

        pass

    @staticmethod
    def __slice_bigrams(message: str) -> str:
        bigrams: str = ''
        for char_index in range(0, len(message), 2):
            bigrams += message[char_index: char_index + 2] + ' '

        return bigrams.rstrip()

    @staticmethod
    def __insert_x_chars(bigrams: str) -> str:
        result: str = ''
        bigrams = bigrams.replace(' ', '')

        for char_index, char in enumerate(bigrams):
            result += char
            if char_index + 1 < len(bigrams):
                if char == bigrams[char_index + 1]:
                    result += 'Х'

        if len(result) % 2 != 0:
            result += 'Х'

        return result

    @staticmethod
    def __check_bigrams(bigrams: str) -> bool:
        for bigram in bigrams.split(' '):
            if len(bigram) != 2:
                return False

            if bigram[0] == bigram[1]:
                return False

        return True
    
    @staticmethod
    def __find_in_row(bigram: str) -> int:
        for row_index, row in enumerate(Playfair.char_matrix):
            if bigram[0] in row and bigram[1] in row:
                return row_index
        
        return -1

    @staticmethod
    def __find_in_col(bigram: str) -> int:
        for row_index, row in enumerate([*zip(*Playfair.char_matrix)]):
            if bigram[0] in row and bigram[1] in row:
                return row_index

        return -1

    @staticmethod
    def __find_char(char: str) -> tuple:
        for row_index, row in enumerate(Playfair.char_matrix):
            if char in row:
                return (row_index, row.index(char))

        return ()

    @staticmethod
    def __prettify(message: str) -> str:
        return message.replace('Й', 'И').replace('Ё', 'Е').replace('Й', 'И')

    @staticmethod
    def encode(message: str, key: str) -> str:
        Playfair.__create_char_matrix(key)
        message = Playfair.__prettify(message)
        bigrams: str = Playfair.__slice_bigrams(message)

        while not Playfair.__check_bigrams(bigrams):
            bigrams = Playfair.__insert_x_chars(bigrams)
            bigrams = Playfair.__slice_bigrams(bigrams)

        encoded_message = ''
        for bigram in bigrams.split(' '):
            index: int = Playfair.__find_in_row(bigram)
            if index != -1:
                row = Playfair.char_matrix[index]
                encoded_message += row[0] if row.index(bigram[0]) > 3 else row[row.index(bigram[0]) + 1]
                encoded_message += row[0] if row.index(bigram[1]) > 3 else row[row.index(bigram[1]) + 1]
                continue

            index = Playfair.__find_in_col(bigram)
            if index != -1:
                row = [*zip(*Playfair.char_matrix)][index]
                encoded_message += row[0] if row.index(bigram[0]) > 3 else row[row.index(bigram[0]) + 1]
                encoded_message += row[0] if row.index(bigram[1]) > 3 else row[row.index(bigram[1]) + 1]
                continue
            
            bigram_first = Playfair.__find_char(bigram[0])
            bigram_second = Playfair.__find_char(bigram[1])
            encoded_message += Playfair.char_matrix[bigram_first[0]][bigram_second[1]]
            encoded_message += Playfair.char_matrix[bigram_second[0]][bigram_first[1]]

        return encoded_message

    @staticmethod
    def decode(message: str, key: str) -> str:
        Playfair.__create_char_matrix(key)
        bigrams: str = Playfair.__slice_bigrams(message)

        encoded_message = ''
        for bigram in bigrams.split(' '):
            index: int = Playfair.__find_in_row(bigram)
            if index != -1:
                row = Playfair.char_matrix[index]
                encoded_message += row[row.index(bigram[0]) - 1]
                encoded_message += row[row.index(bigram[1]) - 1]
                continue

            index = Playfair.__find_in_col(bigram)
            if index != -1:
                row = [*zip(*Playfair.char_matrix)][index]
                encoded_message += row[row.index(bigram[0]) - 1]
                encoded_message += row[row.index(bigram[1]) - 1]
                continue
            
            bigram_first = Playfair.__find_char(bigram[0])
            bigram_second = Playfair.__find_char(bigram[1])
            encoded_message += Playfair.char_matrix[bigram_first[0]][bigram_second[1]]
            encoded_message += Playfair.char_matrix[bigram_second[0]][bigram_first[1]]
        
        return encoded_message.replace('Х', '')

# print(Playfair.encode('ПАДЕНИЕЭТОНЕПРОВАЛПРОВАЛЭТОПРОВАЛПАДЕНИЕЭТОГДЕУПАЛ', key='КЛАД'))
# print(Playfair.decode('ЩГЖПЛРЕНЛТАЛЛЖТНЯФГЩПДОПОГЩГЖПЛРМЧГЩПЭИООЯЛТАЛ', key='КЛАД'))