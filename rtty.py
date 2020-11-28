#%%

# Baudot-Murray - ITA 2 
codes_char = {
'A' : 3 ,
'B' : 25,
'C' : 14,
'D' : 9 ,
'E' : 1 ,
'F' : 13,
'G' : 26,
'H' : 6 ,
'I' : 11,
'J' : 15,
'K' : 18,
'L' : 28,
'M' : 12,
'N' : 24,
'O' : 22,
'P' : 23,
'Q' : 10,
'R' : 5 ,
'S' : 16,
'T' : 30,
'U' : 19,
'X' : 29,
'Y' : 21,
'Z' : 17,
}
#%%

for code in codes_char.values():
    print([int(digit) for digit in list('{0:05b}'.format(code))])