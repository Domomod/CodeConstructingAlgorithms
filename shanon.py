
class symbol:
    def __init__(self, symbol, prob):
        self.symbol = symbol
        self.prob = prob
        self.code = ''
        
    def __str__(self):
        return f"{self.prob:.4} [{self.symbol} => {self.code}]"

def fanoshannon(symbols_dict):
    symbols = []
    for word, prob in symbols_dict.items():
        print(f"{word} {prob}")
        symbols.append( symbol(word, prob) )

    _fanoshannon(symbols[::-1], 0, len(symbols) - 1)
    return get_codes(symbols)

def get_codes(symbols):
    codes = dict()
    for symbol in symbols:
        codes[symbol.symbol] = symbol.code
    return codes

def _fanoshannon(symbols, start, end):
    #print(f"_fanoshannon(symbols, {start}, {end})")
    
    if start == end:
        return
    
    left, right = 0, 0
    i, j = start, end

    while i <= j:
        if left <= right :
            left += symbols[i].prob
            i += 1
        else:
            right += symbols[j].prob
            j -= 1

    for k, symbol in enumerate(symbols[start:end+1]):
        symbol.code += "0" if k < i else "1"

    _fanoshannon(symbols, start, i - 1)
    _fanoshannon(symbols, i,   end)

class symbol:
    def __init__(self, symbol, prob):
        self.symbol = symbol
        self.prob = prob
        self.code = ''
        
    def __str__(self):
        return f"{self.prob:.4} [{self.symbol} => {self.code}]"

def fanoshannon(symbols_dict):
    symbols = []
    for word, prob in symbols_dict.items():
        print(f"{word} {prob}")
        symbols.append( symbol(word, prob) )

    _fanoshannon(symbols[::-1], 0, len(symbols) - 1)
    return get_codes(symbols)

def get_codes(symbols):
    codes = dict()
    for symbol in symbols:
        codes[symbol.symbol] = symbol.code
    return codes

def _fanoshannon(symbols, start, end):
    #print(f"_fanoshannon(symbols, {start}, {end})")
    
    if start == end:
        return
    
    left, right = 0, 0
    i, j = start, end

    while i <= j:
        if left <= right :
            left += symbols[i].prob
            i += 1
        else:
            right += symbols[j].prob
            j -= 1

    for k, symbol in enumerate(symbols[start:end+1]):
        symbol.code += "0" if k < i else "1"

    _fanoshannon(symbols, start, i - 1)
    _fanoshannon(symbols, i,   end)
