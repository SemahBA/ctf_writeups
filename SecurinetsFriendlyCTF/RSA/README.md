# SecurinetsFriendlyCTF
# RSA ? 
RSA ( Rivest Shamir Adleman) is an asymetric algorithm . In such a cryptosystem the encryption key is public and it is different from the decryption key which is kept secret (private) . In RSA, this asymmetry is based on the practical difficulty of the factorization of the product of two large prime numbers . A user of RSA creates and then publishes a public key based on two large prime numbers . The prime numbers must be kept secret. Anyone can use the public key to encrypt a message, but only someone with knowledge of the prime numbers can decode the message. Breaking RSA encryption is known as the RSA problem. Whether it is as difficult as the factoring problem remains an open question. There are currently no published methods to defeat the system if a large enough key is used.

# Encryption Part
1. Choose two distinct prime numbers p and q and they are kept secret
2. Compute n = pq (n is used as the **modulus** for both the public and private keys.)
3. chosing the **exponent e** and it is released as part of the public key.
4. Since we are going to work with numbers we're going to convert the message into a number and **to make sure THAT n>m** or no encryption is going to happen ! 
5. the cipher text c is : **c≡m^e(mod n)**  and send it 

# Decryption Part 
When you receive that cipher c , to get the message back we need to : 


1.phi(n) is Indicatrice d'Euler , using Euler function to get ! Earlier **we said that we need to keep the p and q secret** otherwise we can easily get the phi(n) and compute d because **phi(n)=(p-1)*(q-1)** 

2. Determine d as ed ≡ 1 (mod phi(n)) 


3. the message is : m≡c^d(mod n)

# Back to our challenge : 


![](https://i.imgur.com/E2HYJhv.png)


So as we read the description we see that we have the modulous n and the exponent e and the cipher c but **ALSO there is the d** , So we can easily get the message back ! 
So using this code : 

![](https://i.imgur.com/S7j0peR.png)


and we get this output : 

![](https://i.imgur.com/gnCJX93.png)

we use https://www.browserling.com/tools/hex-to-text  to convert from hex to string and we get this : 

![](https://i.imgur.com/Yf7LnZ4.png)


We submit with : **Securinets{RSA_is_easy_4_n0w}**



