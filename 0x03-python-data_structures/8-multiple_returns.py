#!/usr/bin/python3
def multiple_returns(sentence):
    for i in sentence:
        if len(sentence) < 0:
            return None
        leng = len(sentence)
        fir = sentence[0]
        return leng, fir
