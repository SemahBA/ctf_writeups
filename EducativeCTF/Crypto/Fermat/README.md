
# Challenge : Fermat 

![](https://i.imgur.com/Rm09xQW.png)

Its RSA challenge, we were given the pair (n,e) , the cipher, and the function that generates the primes p,q ! 

`def generate_primes():

	while True:

		randomly_choosen=getPrime(4096)

		p=nextprime(randomly_choosen)

		q=nextprime(p)

		return p,q`



the primes are same length which can lead to FERMAT attack as the title of the challenge mentions ! 

[Fermat Factorization !](https://fr.wikipedia.org/wiki/M%C3%A9thode_de_factorisation_de_Fermat) 

Here is script fermat.py to factor the modulus n ! 

We get the two primes p and q ! Calculating **phi** we find that **gcd(e,phi)!=1** which is a problem , we can't calculate d (the privkey) because we can't calculate the invmod !!

We have gcd(e,phi)=6 , trying gcd(e/gcd(e,phi),phi) we get 1 so we have **gcd(e/6,phi)=1** which lead to small changes in decryption process ?  whats the change ? explanation below 

we  calculate d=invmod(e/6,phi)

What's changes in the decryption ? Okey let's follow it slowly ! 

we know in the decryption process , **m=pow(c,d,n)**

since c=pow(m,e,n) then we have pow(c,d,n)=(m\*\*e)\*\*d [n]=m\*\*(e*d)[n] 

**Property : a\*\*b[n] equals a\*\*(b%phi(n)) [n]**

Lets back , m\*\*(e*d) [n] = m\*\*(e*d % phi(n) ) [n] 

but we have (e/6 * d)=1[phi] so multiply and divide with 6 we get m\*\*(6* e/6 * d % phi(n) ) [n] = m\*\*6[n]

So in the decryption we get **m\*\*6** ! so we just do the sixth root of the result and we get back the message !

final script **sol.py**

#flag : Well after all you have done it !!! Securinets{F3rm4t_&_exp0nent_and_pH1_n0t_c0pr1m33_Really??}


