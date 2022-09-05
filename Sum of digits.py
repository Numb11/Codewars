def digital_root(n):
    while len(str(n)) >=2:
       n = sum(map(int, str(n)))
    return n
