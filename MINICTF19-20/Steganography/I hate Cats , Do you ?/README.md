# Challenge : I hate Cats,Do you? 

The desription of the challenge : 

![](https://i.imgur.com/4urSORF.png)

From the description , that equation means we are going to change bytes of image , 4 bytes from 15DD and 4 bytes from 16B8 using hexedit ! Then we try binwalk and get this result ! 

![](https://i.imgur.com/brGWOWk.png) <br>

there is a zip file , we either do binwalk -e CAT.jpg or we can unzip CAT.jpg

![](https://i.imgur.com/8u31cF7.png) <br>

and we get the flag.txt

![](https://i.imgur.com/ug34IXe.png)

Flag : Securinets{y0u_l0v3_c4t5_i'm_afraid_0f_th3m}
