import random

n=10878437946129824858375622519762424194955730368277534437290174622639809645400690595337495427498420862745759021802412863038354086363439051304120942154948641
generator=97298611782702387975032893084146405290882813993997857845994521625941378689367

def gen_rnd(x):
	random.seed(ord(x)+((generator**(n-1))%n))
	return random.randint(1,10000)

def gen_key(pl):
	Key=[]
	for i in range(len(pl)):
		Key.append(gen_rnd(pl[i]))
	return Key

def func(table):
	for i in range(len(table)//2):
		table[i]=table[i]^table[len(table)-1-i]
		table[len(table)-1-i]=table[i]^table[len(table)-1-i]
		table[i]=table[i]^table[len(table)-1-i]

	return table

plaintext="########################"
key=gen_key(plaintext)
key=func(key)
for i in range(len(key)):
	key[i]=key[i]^83
print (key)
#key=[5645, 2353, 353, 5054, 9043, 1506, 9835, 5863, 8928, 4766, 2353, 8928, 5863, 9043, 6223, 8734, 8928, 2353, 718, 8195, 9691, 8261, 2353, 1433, 8195, 7056, 9043, 7061, 1506, 1433, 7367]
