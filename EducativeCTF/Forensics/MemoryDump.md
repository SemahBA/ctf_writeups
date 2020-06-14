# Challenges : 

##  Part1 : 

![](https://i.imgur.com/eZXxtf2.png)

In these memory dump challenges we are going to use [Volatility](https://github.com/volatilityfoundation/volatility) !

So in the first part , we are asked for the username and password ! 

So first , lets start by identifying the profile with **imageinfo**

![](https://i.imgur.com/Iuaeklp.png)

so we have windows7 ! There is 2 ways to get the username and password !! using the plugin mimikatz as shown below : 

![](https://i.imgur.com/dVgLZ20.png)

or we can use hashdump 

![](https://i.imgur.com/Sr31xqW.png)

we can the user and the hash of the password (a9fdfa038c4b75ebc76dc855dd74f0da) ! try in crackstation and we get the hash ntlm and the value is password123 

Flag for the first part is **Securinets{Mes-vms.fr:password123}**


## Part2

![](https://i.imgur.com/hB8sCl5.png)

so we are looking for a secret file ! playing around with **filescan** , looking for files that its name secret or flag or something related to that ! we get lucky for a file flag 

![](https://i.imgur.com/qErTUOR.png)


Dumping the file using dumpfiles -Q offset and -D directory ! we get the flag : 

![](https://i.imgur.com/bMy2P1I.jpg)

## Part3

![](https://i.imgur.com/fItgTew.png)

from the description , the work is clear ! **clipboard**

![](https://i.imgur.com/IzfySB3.png)

we got that link **https://imgur.com/a/31XyimN** which is the flag !!  : 

![](https://i.imgur.com/v87krBR.jpg)






