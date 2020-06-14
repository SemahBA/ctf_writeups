f=open('binary.txt').read()
t=f.strip().split(' ')
flag=''
for i in t:
	flag+=chr(int(i,2))
print flag
