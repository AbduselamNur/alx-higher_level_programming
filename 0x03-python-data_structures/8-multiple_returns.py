#!/usr/bin/python3
def multiple_returns(sentence):
    for i in sentence:
        if not sentence:
            return len(sentence), None
        leng = len(sentence)
        fir = sentence[0]
        return leng, fir
