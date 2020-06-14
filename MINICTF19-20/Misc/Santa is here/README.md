# Challenge : Santa is here ! 

The desription of the challenge : 

![](https://i.imgur.com/ftRznee.png)

so we have an image and a zip file which is protected with the password , so that password should be hidden in the image ! trying **exitool** we notice something suspecious at the artist part 

![](https://i.imgur.com/wbO6qvW.png) <br>

decoding it from base64 we got 

![](https://i.imgur.com/CsBWcha.png) <br>

that's the password of the zip ! After that we extract file from the zip and we got "Securinets.txt" but there is lot of spaces and tabs 

![](https://i.imgur.com/smmnZo0.png) <br> 

Applying stegsnow -C we get a code from it 

![](https://i.imgur.com/qbeZuuS.png) <br>

Seeding with 2019 (answering to what year is it ?) we generate the same random number p and we apply a simple xor to get back the plaintext 

![](https://i.imgur.com/xYPrOMm.png) <br>

So we got the passphrase , so we extract from the initial image (Securinets.jpg) with InsatSecurinets2019 as passphrase and we get final.txt 

![](https://i.imgur.com/HEOaisZ.png) <br>

the flag is : Securinets{W3_Ar3_h3r3_t0_overt@ke_everything_!!!}
