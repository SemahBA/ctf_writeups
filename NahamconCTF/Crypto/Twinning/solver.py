from pwn import *
from Crypto.Util.number import *
from primefac import primefac as fact
from gmpy import *

HOST="jh2i.com"
PORT=50013
conn=remote(HOST,PORT)

conn.recvuntil(": (")
public_pair=conn.recvline().strip()[:-1].split(',')
conn.recvuntil("is ")
encrypted=int(conn.recvline().strip())
conn.recvline()
e=int(public_pair[0])
n=int(public_pair[1])
primes=list(fact(n))

phi=1
for i in primes:
	phi*=int((i-1))

d=invert(e,phi)
conn.sendline(str(pow(encrypted,d,n)))
print ("Flag : "+conn.recvall().strip())