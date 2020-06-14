#Initializing  the table by putting that numbers given in the description of the task
t=[3, 3, 12, 50, 18, 16, 15, 61, 1, 8, 86, 3, 18, 61, 8, 61, 86, 9, 61, 1, 87, 6, 20, 61, 6, 26, 10, 66, 19, 1, 16, 4, 66, 4, 26, 21, 66, 1, 16, 20, 9, 6, 0, 66, 21, 8, 14, 66, 6, 26, 10, 66, 12, 15, 6, 15, 66, 12, 21, 26, 15, 66, 23, 23, 12, 4 ]

outputXor=""
for i in t:
	outputXor+=chr(i^0x62)    #XORing each element of the table with 0x62 and converting it into
				  #caraters and adding it to the outputXOR string

print outputXor


#So let's implement the caesar algorithm
'''
for i in range(26):
	caesar_output=""
	for j in outputXor:
		if j.islower():
			caesar_output+=chr((ord(j)-97-i)%26+97)
		elif j.isupper():
			caesar_output+=chr((ord(j)-65-i)%26+65)
		else:
			caesar_output+=j
	print caesar_output
''' 
reverse_output=outputXor[::-1]   #Reversing the string (Same as Backward )

#Doing the same code just with replacing outputXor with reverse_output
for i in range(26):
        caesar_output=""
        for j in reverse_output:
                if j.islower():
                        caesar_output+=chr((ord(j)-97-i)%26+97)
                elif j.isupper():
                        caesar_output+=chr((ord(j)-65-i)%26+65)
                else:
                        caesar_output+=j
        print caesar_output
