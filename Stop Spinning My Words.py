def spin_words(sentence):
    b = []
    for i in sentence.split():
        if len(i) > 4:
            b.append(i[::-1])
        else:
            b.append(i)
    return " ".join(b)
