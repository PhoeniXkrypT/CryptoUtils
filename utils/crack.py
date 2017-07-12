
import random

def random_zn_star(n):
    # r in Zn* i.e. gcd(r,n) =1
    r = random.randint(2, n-1)
    while xgcd(r,n)[0] != 1:
        r = random.randint(2, n-1)
    return r

def xgcd(a, b):
    # Function return (gcd, x, y)
    if a == 0:
        return b, 0, 1
    if b == 0:
        return a, 1, 0
    x2, x1, y2, y1 = 1, 0, 0, 1
    while b > 0:
        q = a/b
        x = x2 - q * x1
        y = y2 - q * y1
        a, b = b, a%b
        x2, x1, y2, y1 = x1, x, y1, y
    return a, x2, y2

def modinv(a, n):
    g, x, y = xgcd(a, n)
    if g != 1:
        return None
    return x % n

def rsa_sign(n, d, msg):
    return pow(msg, d, n)

def rsa_msg_blind(n, e, msg):
    r = random_zn_star(n)
    return (pow(r, e, n)*msg)%n, r

def rsa_blind_sign(r, n, s):
    return (s*modinv(r,n))%n

def rsa_commod(n, e1, c1, e2, c2):
    '''
    RSA Common modulus attack with gcd(e1, e2) == 1
    '''
    _, x, y = xgcd(e1, e2)
    if x < 0:
        c1, x = modinv(c1, n), x*(-1)
    elif y < 0:
        c2, y = modinv(c2, n), y*(-1)
    if (not c1) or (not c2):
        return 'MODINV Error!'
    m = (pow(c1, x, n) * pow(c2, y, n))%n
    return str(m)