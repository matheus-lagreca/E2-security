import os
import sys
import hashlib


if len(sys.argv) <2:
    print("The algorithm requires readFile.py <file>")
    sys.exit(1)

file_path = sys.argv[1]

something =b''

with open(file_path, "rb") as bufferedReader:   
    something = bufferedReader.read()


something = hashlib.sha256(something).digest()

hex_something = something.hex()
print("result: {}".format(hex_something))



