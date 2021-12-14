# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

from huffman import *
from shanon import *
from stats import *
from entrophy import *

word = ["0", "1"]
dataset = ['0.75', '0.25']

word_2, data_2 = GetData(word, dataset)
symbols_dict = GetSymbolDict(word_2, data_2)

#print(f"{symbols_dict}")
codes = GetHuffman(symbols_dict)


print(f"Huffman")
for key in codes:
    print(key, '->', codes[key])

print(f"Entrophy is {eta(data_2)}")
print(f"Mean length of code word is {mean_len(codes)}")
print(f"Coding efficiency is {efficiency(codes, eta(data_2))}")

symbols_dict = GetSymbolDict(word_2, data_2)
codes = fanoshannon(symbols_dict)

print(f"Shanon")
for key in codes:
    print(key, '->', codes[key])
print(f"Entrophy is {eta(data_2)}")
print(f"Mean length of code word is {mean_len(codes)}")
print(f"Coding efficiency is {efficiency(codes, eta(data_2))}")

