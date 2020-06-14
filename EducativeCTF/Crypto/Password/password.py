from hashlib import md5

hash="4b98f9a13ce47dbb90c8b79a72d1d04b"

fruits = open("fruit.txt",'r').read().split("\n")
countries = open("countries",'r').read().split("\n")

for fruit in fruits:
	for country in countries:
		for year in range(1900,2020):
			password=fruit.strip().lower()+"_"+country.strip().lower()+"_"+str(year)
			if md5(password).hexdigest()==hash:
				print "Password Cracked!!"
				print password
				exit(1)