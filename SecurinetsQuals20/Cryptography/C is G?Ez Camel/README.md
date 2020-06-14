# Challenge : C is G ?Ez Camel 

![](https://i.imgur.com/BgrFw1p.png) 

connecting the the server and we receive : 

![](https://i.imgur.com/oKUOtpu.png)

Refering to the title and server message its [ElGamal Encryption](https://en.wikipedia.org/wiki/ElGamal_encryption) . Taking a look for encryption option : 

![](https://i.imgur.com/ulw99gP.png) 

so we can give a message and a random number , that's interesting ! i will tell you why in a moment , lets see first get the cure option : 

![](https://i.imgur.com/JiitmHb.png)

So we need the private key to get the cure , but how ? we don't have public keys , no g no y no p nothing ... 
Back to the interesting thing , the encryption options allows us to give a message and a random 

since : 
**c1=pow(g,r,p) and c2=M*pow(y,r)[p]** 

we send r=1 and M=1 , it gives us : **c1=g and c2=y**
we send r=1 and M=-1 , it gives us : **c1=g and c2=py** 

now we have everything y,g and p , calculating the secret key x ! all we know is that y=pow(g,x,p) !
Discret log is solution !! we can use Pohlig_Hellman 

Sending now the secret key to the server 

![](https://i.imgur.com/XbO8vhN.png)

flag is : Securinets{B4444d_3lG4m4l_system}
