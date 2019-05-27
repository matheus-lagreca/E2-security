import os
import sys
import hashlib
video = sys.argv[1]
size = 1024
everything = []
with open(video,"rb") as BF:
    B0=BF.read(size)
    while B0:
        everything.append(B0)
        B0 = BF.read(size) 
H0 = b''
for B0 in reversed(everything):
    H0 = hashlib.sha256(B0 + H0).digest()
final = H0.hex()
print(final)