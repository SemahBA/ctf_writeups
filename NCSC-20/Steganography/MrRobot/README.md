Challenge : Mr.Robot --Steganography

![](https://i.imgur.com/t8ReSFE.png)

After Downloading the files , we get a zip file protected with a password ,a picture and a text file.
the txt file appeared to be pixels of image , so let's create a picture 
So we write this script : 
![](https://i.imgur.com/FZqZiJv.png) 

and we get this : 
![](https://imgur.com/6o8aaUo.png)

We got the password of the zip file "still_n0t_d0n3" , extracting it and we get a picture and another zip file also protected with a password , so obvs the password will be extracted from the picture . Taking a look at the picture and we notice red dots and with the message in the picture , we're sure that the red dots is the key . 
we wrote this script : 
![](https://imgur.com/dQenamg.png)
<br>
and the output was this : <br>

![](https://imgur.com/n8tENqF.png) 

we notice that "i" is starting from 300 and increments but the "j" looks like ASCII . 
another script to extract the string : 
![](https://imgur.com/dDBwasX.png)

we got : "Not to much to get ! more steps to get her down ! pw : wh1t3r0s3_i5_s3cr3t" . The password of the zip is "wh1t3r0s3_i5_s3cr3t" . We got a QR code and another zip ! 
We extracted a base32 string from that QR code , after decoding it we got : 
"we're running out of time ! we need to get it before too late ! pw : the_l4st_p4rt_of_1t"
the password of the zip is : "the_l4st_p4rt_of_1t"
again after extracting it we got a picture .
using exiftool tool we notice that there is a base64 string in comment section which is suspicious . (the command is exiftool the_image")
![](https://imgur.com/hfrz5GM.png)

after decoding it from base64 we get the flag : 
![](https://imgur.com/arEJNS0.png)

Flag : Securinets{w3ll_f**k_s0ci3tY_4nD_wh1t3r0s3}
