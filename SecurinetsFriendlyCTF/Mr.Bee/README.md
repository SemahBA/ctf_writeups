# SecurinetsFriendlyCTF
# Mr.Bee Writeup

![](https://i.imgur.com/TIezt3X.png)

So given this task , and by reading it , we can notice that there is a XOR and by that hint "0x62's everything is good!" now we sure **that there is an XOR with 0x62='b'** ! 
So we're going to XOR that number given with 0x62 and look to the output : 


![](https://i.imgur.com/NUcM9kY.png)

and **the output we get is this **: 


![](https://i.imgur.com/DMdvg0v.png)

By that output , we observe that there is the '_' that indicates the format of the flag but is kinda messed up , So why don't we use **caesar** to test the shifts and maybe that leads us to the flag ! 

![](https://i.imgur.com/FkqBKuW.png)


and this is the output we get : 

![](https://i.imgur.com/m8f6WiD.png)


Strange right ? But the flag is still somewhere there , So let's try to reverse the string,The output of xor and try again with caesar maybe this helps ! 


![](https://i.imgur.com/3Owgbce.png)


and the output we get is : 


![](https://i.imgur.com/f0StLUU.png)



And when reading carefully the output we finally see the right output with a flag : 
**well done dude you can submit now with you_mu5t_b4_a_gr4at_digGerr**
Let's Submit with this flag : **Securinets{you_mu5t_b4_a_gr4at_digGerr}**

![](https://i.imgur.com/BXn3lYj.png)







