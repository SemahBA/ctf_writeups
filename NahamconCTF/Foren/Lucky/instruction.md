# Instructions :


## Cracking the passphrase : 
	sudo ./grond.sh -t4 -w ~rockyou.txt -d lucky.img
	password cracked => iloveyou

	sudo losetup /dev/loop30 lucky.img

	sudo cryptsetup open /dev/loop30 ctf and give the passphrase 'iloveyou'

	sudo mount /dev/mapper/ctf /mnt

	cat /mnt/flag.txt 
### flag : flag{lucky_it_was_an_easy_password}
