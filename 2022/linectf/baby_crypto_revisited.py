from sage.all import *
 
def Babai_closest_vector(M, G, target):
     small = target
     for _ in range(1):
         for i in reversed(range(M.nrows())):
            c = ((small * G[i]) / (G[i] * G[i])).round()
            small -=  M[i] * c
     return target - small
 
r_s = []
s_s = []
k_s = []
h_s = []
 
with open("Babycrypto_revisited_b1f108dea290b83253b80443260b12c3cadc0ed7.txt", "r") as f:
    while True:
        line = f.readline()
        if line == '':
            break
        r, s, k, h = f.readline().split(" ")
        r_s.append(int(r, 16))
        s_s.append(int(s, 16))
        k_s.append(int(k, 16))
        h_s.append(int(h, 16))
 
p = 0xffffffffffffffffffffffffffffffff7fffffff
K = GF(p)
a = K(0xffffffffffffffffffffffffffffffff7ffffffc)
b = K(0x1c97befc54bd7a8b65acf89f81d4d4adc565fa45)
E = EllipticCurve(K, (a, b))
G = E(0x4a96b5688ef573284664698968c38bb913cbfc82, 0x23a628553168947d59dcc912042351377ac5fb32)
E.set_order(0x0100000000000000000001f4c8f927aed3ca752257 * 0x01)
q = E.order()
M = matrix(QQ, 102)
B = 2**64
for i in range(50):
    M[i, i] = q
    M[50 + i, i] = 1 << 96
    M[50 + i, 50 + i] = -1
    r = r_s[i]
    s = s_s[i]
    k = k_s[i]
    h = h_s[i]
    M[100, i] = -r * inverse_mod(s, q) % q
    M[101, i] = (k - h * inverse_mod(s, q)) % q
 
M[100, 100] = B / q
M[101, 101] = B
M = M.LLL()
 
print(hex(q + M[1][100] * q / B))
