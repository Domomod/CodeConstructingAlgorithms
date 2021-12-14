from decimal import *
from typing import *

getcontext().prec = 8

def GetData(_word, _dataset):
    word = _word
    dataset = [Decimal(x) for x in _dataset]


    for XX, P_XX in zip(word, dataset):
        print(f"P({XX}) = {P_XX} ")

    print("\n\n 2 rozszerzeni zrodla:")

    word_2 = []
    dataset_2 = []
    for XX, P_XX in zip(word, dataset):
        for YY, P_YY in zip(word, dataset):
            print(f"P({XX}{YY}) = {P_XX * P_YY} ")
            
            word_2.append(XX + YY)
            dataset_2.append(P_XX * P_YY)

    return word_2, dataset_2        


class node:
    def __init__(self, symbol, prob, L = None, R = None, UP = None):
        self.symbol = symbol
        self.prob = prob
        self.code = ''
        self.L = L
        self.R = R

    def print(self, depth = 0):
        
        str_val = "  " * depth + f"{self.prob:.4} [{self.symbol} => {self.code}]\n"
        if self.L:
            str_val += self.L.print(depth+1)
        if self.R:
            str_val += self.R.print(depth+1)
            
        return str_val
        
    def __str__(self):
        return f"{self.prob:.4} [{self.symbol} => {self.code}]"

def GetSymbolDict(symbol_vec, prob_vec):
    symbols = dict()
    for symbol, prob in zip(symbol_vec, prob_vec):
        symbols[symbol] = prob
    return symbols
    

def GetCodes(node, codes, val=''):
    code = val + node.code
    if node.L:
        GetCodes(node.L, codes, code)
    if node.R:
        GetCodes(node.R, codes, code)
    if not ( node.L or node.R) :
        #print(f"New code found: {code}")
        codes[node.symbol] = code


def GetHuffman(symbols_with_probs):
    nodes = []
    for symbol in symbols_with_probs:
        nodes.append(node(symbol, symbols_with_probs.get(symbol)))

    while len(nodes) > 1:
        nodes = sorted(nodes, key = lambda x: x.prob)

        smallest_1 = nodes[0]
        smallest_2 = nodes[1]

        #print(smallest_1)
        #print(smallest_2)
        #print("")

        smallest_1.code = '0'
        smallest_2.code = '1'

        s = ''
        p = smallest_1.prob + smallest_2.prob
        
        newNode = node(s, p, smallest_1, smallest_2)
        #print(newNode.print())
        
        nodes.remove(smallest_1)
        nodes.remove(smallest_2)
        nodes.append(newNode)
        
        #print("")
    print(nodes[0].print())
    
    codes = dict()
    GetCodes(nodes[0], codes)
    return codes
