#%%

from message import message

LETTER = 0
FIGURE = 1
ERROR = 2

# ITA2 Baudot-Murray code
code_figure_to_letter = 0x1F
code_letter_to_figure = 0x1B

codes = [
    ['NUL', 'NUL'],
    ['E', '3'],
    ['\n', '\n'],
    ['A', '-'],
    [' ', ' '],
    ['S', '\''],
    ['I', '8'],
    ['U', '7'],
    ['\r', '\r'],
    ['D', 'enq'],
    ['R', '4'],
    ['J', 'bel'],
    ['N', ','],
    ['F', '!'],
    ['C', ':'],
    ['K', '('],
    ['T', '5'],
    ['Z', '+'],
    ['L', ')'],
    ['W', '2'],
    ['H', 'pounds'],
    ['Y', '6'],
    ['P', '0'],
    ['Q', '1'],
    ['O', '9'],
    ['B', '?'],
    ['G', '&'],
    ['fs', 'fs'],
    ['M', '.'],
    ['X', '/'],
    ['V', '='],
    ['ls', 'ls']
]

def char_to_integer(char, current_code_type):
    for i in range(len(codes)):
        if codes[i][current_code_type] == char:
            return [i, current_code_type]

    if current_code_type == LETTER:
        next_code_type = FIGURE
    else:
        next_code_type = LETTER

    for i in range(len(codes)):
        if codes[i][next_code_type] == char:
            return [i, next_code_type]

    return [0, ERROR]

def string_to_integer(message):
    message_in_code = []
    current_code_type = LETTER
    for char in message:
        [code, next_code_type] = char_to_integer(char, current_code_type)
        if next_code_type == ERROR:
            message_in_code.append("e")
        else:
            if next_code_type != current_code_type:
                current_code_type = next_code_type
                if next_code_type == LETTER:
                    message_in_code.append(code_figure_to_letter)
                else:
                    message_in_code.append(code_letter_to_figure)
            message_in_code.append(code)

    return message_in_code

def integer_to_bitarray(message_integer):
    return (['{0:05b}'.format((code)) for code in message_integer])

def bitarray_to_array(message_bitarray):
    message_array = [[0,0,0,0,0] for i in range(len(message_bitarray))]

    for i in range(len(message_bitarray)):
        for j in range(5):
            message_array[i][j] = int(message_bitarray[i][j])

    return message_array

def array_repeat(message_array, n):
    message_repeated = []
    for i in range(len(message_array)):
        message_repeated.append([item for item in message_array[i] for j in range(n)])

    return message_repeated

def add_start_and_stops_bits(message_array_repeated):
    message_with_start_and_stop_bits = []
    n = int(len(message_array_repeated[0]) / 5)
    start_bit = [0] * n
    stop_bit = [1] * int(n * 3 / 2)
    for i in range(len(message_array_repeated)):
        message_with_start_and_stop_bits.append(start_bit + message_array_repeated[i] + stop_bit)

    return message_with_start_and_stop_bits
#%%
# message_string = "HELLO 123 WORLD!"
message_string = message
message_integer = string_to_integer(message_string)
message_bitarray = integer_to_bitarray(message_integer)
message_array = bitarray_to_array(message_bitarray)
message_array_repeated = array_repeat(message_array, 2)
message_with_start_and_stop = add_start_and_stops_bits(message_array_repeated)

#%%

import matplotlib.pyplot as plt
import numpy as np

#%%
chars = range(1)

b = []
message_to_print = ""
for i in chars:
    b += message_with_start_and_stop[i]
    message_to_print += repr(message_string[i])

n = np.arange(len(b))
plt.step(n, b)

plt.xlabel('n')
plt.ylabel('b[n]')
plt.title(message_to_print)
plt.grid(True)
plt.show()
# %%
