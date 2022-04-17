# HackZoneX Forensics Writeup

## The challenges were revenge of last years challenges that were solved by simple strings command. This Year, The solution was already published by the AUTHOR DURING THE CTF COMPETITION! WHY? WHO KNOWS! 

## TL;DR
* Hints everywhere, for solved challenges, and sharing the solution! YES, solution during a CTF from the author ^^
* 0 Organization 
* 0 response from admins
* 2hours BLIND HOUR

## I have been enjoying the last HackZone Editions, but this one? Not at all, this year organizer ruined the legacy that the one before this "kinda admin" have worked for. Anyway, this is the support and kind words of their admin ^^ 

![admin](https://i.ibb.co/Q98Pp4p/admin.png)



## Before Explaining the challenges, I would like to thank my teammate *Cyb3rdoctor*.  

## Forensics1

![Forensics1](https://i.ibb.co/wL24Tp7/for1.png)

Downloading the image, we see box.img which is: **QEMU QCOW2 Image (v2), 44023414784 bytes**

To mount QCOW2 Image, the following commands:
* sudo modprobe nbd max_part=8
* sudo qemu-nbd --connect=/dev/nbd0 box.img
* sudo mkdir /mnt/foren
* sudo mount /dev/nbd0p1 /mnt/foren

And the image is successfully mounted:

![mounted](https://i.ibb.co/wCDBwxY/for2.png)

Looking around, we can find the bash history in root directory having the following:

```txt
systemctl status 
systemctl status tunizjan 
ls
history 
cd /etc/systemd/system/
ls
cat > tunizjan.service
systemctl daemon-reload 
systemctl status tunizjan
cat  tunizjan.service
mkdir -p /opt/utils/antivirus 
cd  /opt/utils/antivirus 
mv /tmp/tunizjan .
ls
mkdir /etc/tunizjan/
cat > /etc/tunizjan/config.yaml 
cat > /etc/tunizjan/config.yaml 
systemctl enable  tunizjan
systemctl status tunizjan
systemctl start  tunizjan
systemctl status tunizjan
systemctl enable tunizjan
systemctl enable tunizjan.service
journalctl -xe 
ls
./tunizjan 
journalctl -xe -u tunizjan 
vim /etc/systemd/system/tunizjan.service 
vi /etc/systemd/system/tunizjan.service 
systemctl start  tunizjan
systemctl daemon-reload 
systemctl start  tunizjan
systemctl status  tunizjan
systemctl enable   tunizjan.service$
systemctl enable tunizjan
systemctl status  tunizjan
systemctl enable tunizjan
systemctl enable tunizjan -h 
systemctl enable tunizjan --now
service enable tunizjan 
cat /etc/os-release 
systemctl enable tunizjan 
systemd-analyze verify tunizjan 
systemctl status  tunizja
systemctl status  tunizjan 
systemctl status  tunizjan 
systemctl status  tunizjan -l
reboot 
systemctl status tunizjan 
```

important parts:
```bash
mkdir -p /opt/utils/antivirus 
cd  /opt/utils/antivirus 
mv /tmp/tunizjan .
```
```bash
mkdir /etc/tunizjan/
cat > /etc/tunizjan/config.yaml 
cat > /etc/tunizjan/config.yaml
```
```bash
vim /etc/systemd/system/tunizjan.service
```

first, lets check the tunizjan.service:
```txt
[Unit]
After=network.target
Wants=network-online.target

[Service]
Type=notify
PermissionsStartOnly=true
ExecStart=/opt/utils/antivirus/tunizjan
Restart=on-abnormal

[Install]
WantedBy=multi-user.target
Alias=tunizjan.service
```

As shown above, **ExecStart=/opt/utils/antivirus/tunizjan**

So we have everything for now, the service tunizjan, the config file located at /etc/tunizjan/config.yaml, and the binary in /opt/utils/antivirus. 

the config file has the following:
```yaml
password: 00000000690ed426ccf17803ebe2bd0884bcd58a1bb5e7477ead3645f356e7a9
```

This will be needed later. For now, let's try to run the tunizjan in /opt/utils/antivirus/.

![config](https://i.ibb.co/S6g2vCr/for3.png)

It was looking for the config file in /etc/tunizjan. so i copied the config file and create the /etc/tunizjan and relaunched the binary. and the error was gone. 

![password](https://i.ibb.co/QQL2Xfb/wxc.png)

Asking about password? This is for the next challenge? I opened the wireshark, let it capture and starting digging about the password (it will be explained in the next challenge). I saw the following:

![log](https://i.ibb.co/VM39mWg/wwxcwcxwcwxc.png)

I went back to my wireshark, and followed some captures, and got the flag :D 

![flag](https://i.ibb.co/zHRpdm5/wwwwi.png)

### flag: HZXCTF{FixedHZiX-Hi%JackMan}

## Forensics 2

![Forensics2](https://i.ibb.co/fM75FDp/fff.png)

After running the binary, as mentioned before, it asks about a password, and we have the config.yaml right? googling the password, i found this link: 
https://www.chess.com/forum/view/chess-lessons/teach-me-python-ill-teach-you-chess?page=3 , this answer gave me the password ^^

```md 
ok. just ran it & got this :

Found Oneshot Count: 426479724 tries...yippee !!
00000000690ed426ccf17803ebe2bd0884bcd58a1bb5e7477ead3645f356e7a9
572.839307 seconds

so. the sha256 hash abv represents the base10 integer 426,479,724...a 64-character hexstring w/ (8) leading zeros - found in 573 seconds or abt 9+ mins.

check it here :

https://emn178.github.io/online-tools/sha256.html

the odds of hitting this is 16^8 ≈ 4.3BB to 1. so sooper dooper early...yee !
```

so connecting to the service and providing the password, we get our flag \o/

![flag2](https://i.ibb.co/3dLWJRf/flag.png)

### flag: HZXCTF{FixedHZiX-Bru2forceMan}
