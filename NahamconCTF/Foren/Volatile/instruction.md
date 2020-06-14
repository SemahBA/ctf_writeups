# instructions : 

## identify the os :
	vol.py -f memdump.raw imageinfo 
	
	```
	Volatility Foundation Volatility Framework 2.6.1
	INFO    : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : Win7SP1x86_23418, Win7SP0x86, Win7SP1x86_24000, Win7SP1x86
                     AS Layer1 : IA32PagedMemoryPae (Kernel AS)
                     AS Layer2 : FileAddressSpace (/home/samehba/Downloads/Challenges/NahamCon_CTF/Foren/Volatile/memdump.raw)
                      PAE type : PAE
                           DTB : 0x185000L
                          KDBG : 0x8276fc28L
          Number of Processors : 1
     Image Type (Service Pack) : 1
                KPCR for CPU 0 : 0x82770c00L
             KUSER_SHARED_DATA : 0xffdf0000L
           Image date and time : 2020-04-20 21:16:55 UTC+0000
     Image local date and time : 2020-04-20 14:16:55 -0700
	```

## looking for the flag : (looking for typing commands) 
either : using cmdscan or consoles
echo JCTF{nice_volatility_tricks_bro}

### flag : JCTF{nice_volatility_tricks_bro}
