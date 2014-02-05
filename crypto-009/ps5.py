#!/usr/bin/env python

import gmpy2

p = gmpy2.mpz(13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171)
g = gmpy2.mpz(11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568)
h = gmpy2.mpz(3239475104050450443565264378728065788649097520952449527834792452971981976143292558073856937958553180532878928001494706097394108577585732452307673444020333)
B = gmpy2.mpz(2**20)

# h / g**x1 == (g**B)**x0 in Zp

# Build a hash table of all possible values of the left hand side
left = dict()
for x1 in range(B):
    left[gmpy2.divm(h, gmpy2.powmod(g, x1, p), p)] = x1

X0 = None
X1 = None

# Check if the right hand side is in the hash table.
for x0 in range(B):
    right = gmpy2.powmod(gmpy2.powmod(g, B, p), x0, p)
    if right in left:
        X1 = left[right]
        X0 = x0
        break

assert X0
assert X1
x = X0 * B + X1
assert h == gmpy2.powmod(g, x, p)

print x

# This is the answer.
assert x == 375374217830
