def mean_len(codes_dict, probs_dict):
    return sum([len(code) * float(probs_dict[word]) for word, code in codes_dict.items()])

def efficiency(codes_dict, entrophy, probs_dict):
    H_X = entrophy
    L = mean_len(codes_dict, probs_dict)
    n = H_X / L
    return n
