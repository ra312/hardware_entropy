#!usr/local/bin python3
import numpy as np
import pandas as pd
def cryptorand(n):
    with open('/dev/random','rb') as rnd:
        a = np.frombuffer(rnd.read(n*4), dtype=np.uint32) >> 5
        b = np.frombuffer(rnd.read(n*4), dtype=np.uint32) >> 6
        return (a * 67108864.0 + b) / 9007199254740992.0

def generate_random_points(n, p):
  """
  use hardware entropy to generate random points n points in p-dimensional 
  Euclidean space form 
  """
  x = np.frombuffer(os.urandom(4*n*p), dtype = np.uint32)
  x = x.reshape(n,p)
  x = [row.tolist() for row in x]
  return x

if __name__ == '__main__':

    print(cryptorand(100))
