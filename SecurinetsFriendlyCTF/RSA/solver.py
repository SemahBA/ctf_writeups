import gmpy
n=1236295892405270230539230969040992785185291816718701100304929794909995200627
e=65537
c=207601056193156560193719709777182802049921556024453789197870496765940858099
d=1220318007838273512879485655236916905998981315311166865536426877649021443873

m=pow(c,d,n)        # as we said to get the message back we need to calculate m=c^d(mod n)
		    # the pow fucntion : pow(a,b,c) is equivalent to a^b(mod c)

print (hex(m))    #converting the m to hex and print it

#after we get that hex either we go to https://www.browserling.com/tools/hex-to-text and convert it 
#or simply add this "0x5253415f69735f656173795f345f6e3077"[2:].decode('hex')

