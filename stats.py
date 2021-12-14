def mean_len(codes_dict):
    codes = list(codes_dict.values())
    return sum([len(code) for code in  codes])/len(codes)

def efficiency(codes_dict, entrophy):
    codes = list(codes_dict.values())
    H_X = entrophy
    L = mean_len(codes)
    n = H_X / L
    return n
