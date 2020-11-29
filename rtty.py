#%%

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

#%%

for i in range(1 << 5):
    print([int(digit) for digit in list('{0:05b}'.format(i))])

#%%
#%%

def char_to_code(char, current_code_type):
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

def message_to_code(message):
    message_in_code = []
    current_code_type = LETTER
    for char in message:
        [code, next_code_type] = char_to_code(char, current_code_type)
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


# %%


message = "HELLO 123 WORLD!"
message_in_code = message_to_code(message)

message_in_code_binary = (['{0:05b}'.format((code)) for code in message_in_code])

# taken from https://cryptii.com/pipes/baudot
# modified since "3 space W" should transistion from figure to letter after the
# space but transisions before space
message_in_code_binary_desired = [
    '10100', # H 
    '00001', # E
    '10010', # L
    '10010', # L
    '11000', # O
    '00100', # space
    '11011', # 0x1B letter to figure
    '10111', # 1
    '10011', # 2
    '00001', # 3
 #   '11111', # 0x1F figure to letter
    '00100', # space
    '11111', # 0x1F figure to letter
    '10011', # W
    '11000', # O
    '01010', # R
    '10010', # L
    '01001', # D
    '11011', # 0x1B letter to figure
    '01101'] # !

for i in range(len(message_in_code_binary_desired)):
    if message_in_code_binary[i] == message_in_code_binary_desired[i]:
        print(str(i) + " " +message_in_code_binary[i] + " " +message_in_code_binary_desired[i] +" ok")
    else:
        print(str(i) + " " +message_in_code_binary[i] + " " +message_in_code_binary_desired[i] +" nok")

# %%
