from pwn import *
import enchant as e 

#setting up connection 
HOST="jh2i.com"
PORT=50012
conn=remote(HOST,PORT)

def sol_quest1(text):
	nb_wrng=0
	for i in data:
		if not checker.check(i):
			nb_wrng+=1
	return nb_wrng

def sol_quest2(text):
	to_send=""
	for i in text:
		if not checker.check(i):
			to_send+=i+" "
	return to_send[:-1]

def sol_quest3(text):
	to_send=""
	wrong=[]
	for i in text:
		if not checker.check(i):
			wrong.append(i)
	wrong.sort()
	for i in wrong:
		to_send+=i+" "
	return to_send[:-1]

def sol_quest4(text):
	to_send=0
	for i in text:
		if checker.check(i):
			to_send+=1
	return to_send

def sol_quest5(text):
	to_send=""
	for i in text:
		if checker.check(i):
			to_send+=i+" "
	return to_send[:-1]

def sol_quest6(text):
	to_send=""
	corr=[]
	for i in text:
		if checker.check(i):
			corr.append(i)
	corr.sort()
	for i in corr:
		to_send+=i+" "
	return to_send[:-1] 

checker = e.Dict()
Question1="Can you tell me how many words here are NOT real words?"
Question2="Can you tell me which words here are NOT real words IN CHRONOLOGICAL ORDER? Separate each by a space."
Question3="Can you tell me which words here are NOT real words IN ALPHABETICAL ORDER? Separate each by a space."
Question4="Can you tell me how many words here ARE real words?"
Question5="Can you tell me which words here ARE real words IN CHRONOLOGICAL ORDER? Separate each by a space."
Question6="Can you tell me which words here ARE real words IN ALPHABETICAL ORDER? Separate each by a space."
try:
	while True:
		Question=conn.recvline().strip()
		print Question
		data=conn.recvline().strip().split(' ')
		if Question in Question1 or Question1 in Question:
			to_send=sol_quest1(data)
			conn.sendline(str(to_send))
		if Question in Question2 or Question2 in Question:
			to_send=sol_quest2(data)
			conn.sendline(to_send)
		if Question in Question3 or Question3 in Question:
			to_send=sol_quest3(data)
			conn.sendline(to_send)
		if Question in Question4 or Question4 in Question:
			to_send=sol_quest4(data)
			conn.sendline(str(to_send))
		if Question in Question5 or Question5 in Question:
			to_send=sol_quest5(data)
			conn.sendline(to_send)
		if Question in Question6 or Question6 in Question:
			to_send=sol_quest6(data)
			conn.sendline(to_send)
		print conn.recvline()


except:
	print "Error occured !"

#flag : flag{you_know_the_dictionary_so_you_are_hired}
