from Crypto.Util.number import *
from sympy import *

def nonsense():
	while True:
		p=getPrime(1024)
	   	again_what = len(bin(p)[2:])
	   	this_is_great=pow(2,again_what)
	   	well=this_is_great-1
	   	having_fun=well^p
	   	if isprime(having_fun+31337):
	   		return p,(having_fun+31337)

#The only information we could get
