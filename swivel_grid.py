class SwivelGrid:

    @staticmethod
    def __reverse_grid_horizontly(grid: list) -> list:
        return [*map(lambda x: x[::-1], grid)]

    @staticmethod
    def __reverse_grid_verticaly(grid: list) -> list:
        def __transpose_grid(grid: list) -> list:
            return [*map(lambda x: [*x], [*zip(*grid)])]

        return __transpose_grid(SwivelGrid.__reverse_grid_horizontly(__transpose_grid(grid)))

    @staticmethod
    def __change_position(grid: list, position: int) -> list:
        if position == 2:
            return SwivelGrid.__reverse_grid_horizontly(SwivelGrid.__reverse_grid_verticaly(grid))
        elif position == 3:
            return SwivelGrid.__reverse_grid_horizontly(grid)
        elif position == 4:
            return SwivelGrid.__reverse_grid_verticaly(grid)
        else:
            return grid

    @staticmethod
    def encode(message: list, key_grid: list) -> str:
        encoded_char_grid = [[''] * len(key_grid) for _ in range(len(key_grid))]
        char_index = 0

        for position in range(1, 5):
            for row_index, row in enumerate(SwivelGrid.__change_position(key_grid, position)):
                for col_index, col in enumerate(row):
                    if col == 1:
                        encoded_char_grid[row_index][col_index] = message[char_index]
                        char_index += 1

        return ''.join(map(lambda x: ''.join(x), encoded_char_grid))

    @staticmethod
    def decode(message: str, key_grid: list) -> str:
        encoded_char_grid = [[*message[i:i + len(key_grid[0])]] for i in range(0, len(message), len(key_grid[0]))]
        decoded_message = ''

        for position in range(1, 5):
            for row_index, row in enumerate(SwivelGrid.__change_position(key_grid, position)):
                for col_index, col in enumerate(row):
                    if col == 1:
                        decoded_message += encoded_char_grid[row_index][col_index]

        return decoded_message


# MESSAGE_DECODE = [
#     ['н', 'о', 'н', 'а'],
#     ['С', 'п', ' ', 'м'],
#     ['и', ',', ' ', 'о'],
#     ['я', 'м', ' ', ' '],
#     ['р', 'о', 'о', 'я'],
#     [',', 'с', ' ', 'п'],
#     ['д', 'о', 'р', '.'],
#     [' ', 'о', 'к', 'и'],
#     [' ', ' ', 'н', 'а'],
#     ['д', 'и', 'о', 'й']
# ]

# MESSAGE_DECODE = ''.join(map(lambda x: ''.join(x), MESSAGE_DECODE))
# MESSAGE_DECODE_KEY_GRID = [
#     [0, 0, 0, 0],
#     [1, 1, 0, 0],
#     [1, 0, 0, 0],
#     [0, 0, 0, 1],
#     [0, 0, 0, 0],
#     [0, 1, 0, 1],
#     [0, 1, 0, 0],
#     [0, 0, 1, 0],
#     [0, 0, 0, 0],
#     [0, 0, 1, 1]
# ]
# print(SwivelGrid.decode(MESSAGE_DECODE, MESSAGE_DECODE_KEY_GRID))