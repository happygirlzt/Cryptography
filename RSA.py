# 有bug。。不过暂时找不出来。。

from math import fmod, pow
from fractions import gcd

def ext_euclid(a, b, q):
    if b == 0:
        return 1, 0
    else:
        x, y = ext_euclid(b, a % b, q)
        x, y = y, (x - (a // b) * y)
        return x, y

# Main part of RSA algorithm
if __name__ == "__main__":
    # Select 2 random prime numbers
    # p, q should be private
    p = 3.0
    q = 7.0

    # First part of public key, n
    n = p * q;

    # A smalle exponent say e, an integer
    # e stands for encrypt, another public key
    e = 3.0
    phi = (p - 1) * (q - 1)
    while e < phi:
        if gcd(e, phi) == 1:
            break
        else:
            e+=1

    # Private key (d stands for decrypt)
    d, k = ext_euclid(e, phi, 1)

    msg = 30.0

    print("Message data = %f" % msg)

    # Encryption c = (msg ^ e) % n
    c = msg ** e
    c = fmod(c, n)
    print("\nEncrpyted data = %f" % c)

    # Decryption m = (c ^ d) % n
    m = c ** d
    m = fmod(m, n)
    print("\nOriginal Message Sent = %f" % m)
