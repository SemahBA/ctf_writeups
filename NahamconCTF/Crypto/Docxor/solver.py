from pwn import *


corrupted=open('homework','rb').read()

key = xor(corrupted[:4], b"\x50\x4B\x03\x04")

open('fixed_file.doc','wb').write(xor(key,corrupted))
