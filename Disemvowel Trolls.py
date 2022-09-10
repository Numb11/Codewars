def disemvowel(string_):
    for i in string_:
        if i in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            string_ = string_.replace(i, "")
    return string_
