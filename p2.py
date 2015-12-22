"""
    Fib sequence: 1,1,2,3,5,8,13,21,34,55,89...
    odd,odd,even,odd,odd,even,odd,odd,even,odd,odd...
    p,q,(p+q),(p+2q),(2p+3q),(3p+5q),(5p+8q)...
"""


def mine(mx):
    p = q = 1
    sm = 0

    while q < mx:
        sm += p + q
        p, q = p + 2*q, 2*p + 3*q

    return sm
