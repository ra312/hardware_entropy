#!usr/local/bin python3
import numpy as np

def cryptorand(n):
    with open('/dev/random','rb') as rnd:
        a = np.frombuffer(rnd.read(n*4), dtype=np.uint32) >> 5
        b = np.frombuffer(rnd.read(n*4), dtype=np.uint32) >> 6
        return (a * 67108864.0 + b) / 9007199254740992.0


if __name__ == '__main__':

    print(cryptorand(100))
