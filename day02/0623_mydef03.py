from random import random
def getHolJjak():
    ret = "홀"
    rnd = random()
    if rnd > 0.5:
        ret = "짝"
    return ret

com = getHolJjak()

print("com", com)
