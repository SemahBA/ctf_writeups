from Crypto.Util.number import *
from random import *
from sympy import * 
import gmpy

def crack(n):
	a = gmpy.sqrt(n)
	while True:
		b2 = a*a - n
		if b2<=0:
			a+=1
		else:
			b = gmpy.sqrt(b2)
			if b*b == b2:
				p = a+b
				q = a-b
				return p,q
			a += 1
