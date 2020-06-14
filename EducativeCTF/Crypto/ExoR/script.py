import base64
import codecs
from pwn import xor
from base64 import b64decode as dec 
"""
def Alpha(flag):
	enc = xor(flag[0],'\x13')
	for i in range(1,len(flag)):
		enc += xor(flag[i],enc[i-1])
	return enc



flag = "TODO"
encrypted = Alpha(flag)
encrypted = codecs.encode(encrypted, 'rot_13')

with open("encrypted.txt","w+") as f:
	f.write(base64.b64encode(encrypted))

"""

#encrypted.txt : QCVTM04oUyNKJF8aLhp2EHYQQjcHaCpLdg5zMnMyc0wk

""""""
#Solver

encrypted = "QCVTM04oUyNKJF8aLhp2EHYQQjcHaCpLdg5zMnMyc0wk"
encrypted = dec(encrypted)
encrypted = codecs.decode(encrypted, 'rot_13')
decrypted=chr(ord(encrypted[0])^ 0x13)
print "Flag [0]"+decrypted
for i in range(1,len(encrypted)):
	decrypted+=chr(ord(encrypted[i])^ord(encrypted[i-1]))
print decrypted
