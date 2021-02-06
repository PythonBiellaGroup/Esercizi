def char_freq(str):
    mappa = {}
    for carattere in str:
        if carattere in mappa:
            mappa[carattere] += 1
        else:
            mappa[carattere] = 1
    return mappa