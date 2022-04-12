import numpy as np
def lcm(*args):
    if args == ():
        return 1
    return np.lcm.reduce(args)
