# Challenge : Destruction

![](https://i.imgur.com/q5Oe1bU.png )

connecting the the server and we receive : 

![](https://i.imgur.com/497Dp2i.png)

we were asked to give username and password for the access how we get that ? 
Well ,we were given MSB and LSB of something related to modulus , well its for one of the primes ! That way we can use to factor n ! So we Have modulus n size and knownbits ! So we need to define an polynomial == 0 (mod p) that gives us the missing part (x) (solver.sage)

After getting the value of p ! all the rest is easy back to simple RSA !

calculating the message m=pow(c,d,n) 

We get "Username : LUCIFER password : MORNINGSTAR"

Sending these infos to server and we receive : 

![](https://i.imgur.com/2cUOcQt.png)

Securinets{Ev3_h4s_d0ne_1T_a5k_Amenadiel}
