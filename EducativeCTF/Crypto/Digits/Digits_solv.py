from Crypto.Util.number import *


Words = ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
Digits = ["0","1","2","3","4","5","6","7","8","9"]


encrypted=open('enc.txt','r').read().strip().split(' ')
decrypted=""

for i in range(len(encrypted)):
	encrypted[i]=Digits[Words.index(encrypted[i])]
for i in encrypted:
	decrypted+=i

print long_to_bytes(int(decrypted))

