import os
import sys
import hashlib

another =b'a'
something =b'b'

another = hashlib.sha256(another).digest()
something = hashlib.sha256(something).digest()

hex_another = another.hex()
hex_something = something.hex()

print("'a' sha256 in hex: {}".format(hex_another))
print("'b' sha256 in hex: {}".format(hex_something))