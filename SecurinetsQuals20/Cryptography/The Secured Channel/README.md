# Challenge : The Secured channel

![](https://i.imgur.com/56arl2y.png)

Connecting to the server : 

![](https://i.imgur.com/6hOiTde.png)

We weren't given the modulus N but g,and r were given and very big secret ! 

taking a look at information.py given : 

![](https://i.imgur.com/tqrzoNY.png)

check this part : 

`again_what = len(bin(p)[2:])`

`this_is_great=pow(2,again_what)`

`well=this_is_great-1`

`having_fun=well^p`

Trying with many values of p we notice that p+having_fun=2**k-1 with k is number bits of p ! 

Very interesting ! so the function returns p and having_fun+31337(which is q) 

so p+q=p+having_fun+31337=pow(2,k)-1+31337=2**k+31336 

and p*q=n 

for solving p we get the quadtratic equation :  p**2-Sp+n=0 with S=p+q and n=p*q ! 

But we are missing n ! 

Taking a look at the Help option ! 

![](https://i.imgur.com/LdgF5e3.png)

It says not like the encryption as option1 but helps us to get missing part , meaning N ! How is that ? 
well : 

![](https://i.imgur.com/nbjCcJO.png)

Basing on that we get the n (script getN.py)

![](https://i.imgur.com/7QqAQYh.png)

So back to our equation : **pow(p,2)-Sp+n=0** 

Solving it : (solvp.py)

`from sympy.solvers import solve`

`from sympy import Symbol`

`from sympy import *`

`p=Symbol('p')`

`S=2**1024+31336`

`n=(value found using getN)`

`print (solve(p**2-S*p+n,p))`

And we got p and q !! 

![](https://i.imgur.com/i3rai4B.png)

Back to the server , we were given N , g , r and the cipher was lot bigger than the n .. 
Well After all it was : [Paillier Cryptosystem](https://en.wikipedia.org/wiki/Paillier_cryptosystem)

Compute the plaintext message as: ![](https://i.imgur.com/UaVSJgL.png) 

with L is :    ![](https://i.imgur.com/aUflpMy.png)

Lamda is : lcm(p-1,q-1) and mu=invert(((pow(int(g),int(lamda),int(n**2))-1)//n),n)

Decrypting the cipher (getMessage.py) and we get : 

**Well after all its not that secure , well done , here you go ! have your gift : Securinets{Pa1lli3r??_I_Th1nk_y0u_r0ck!!}**

**Flag : Securinets{Pa1lli3r??_I_Th1nk_y0u_r0ck!!}**





