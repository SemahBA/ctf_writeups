#md5 hash : 4b98f9a13ce47dbb90c8b79a72d1d04b
#password : fruit_country_year
from hashlib import md5

fruits=open('Password/fruit.txt','r').read().split('\n')
countries=open('Password/countries.txt','r').read().split('\n')

password_to_find='4b98f9a13ce47dbb90c8b79a72d1d04b'
trying_pass=""
for fruit in fruits:
	for country in countries:
		for year in range(1900,2000):
			trying_pass=fruit.lower()+"_"+country.lower()+"_"+str(year)
			if md5(trying_pass).hexdigest()==password_to_find:
				print ("FOUND")
				print trying_pass
				exit(0)


