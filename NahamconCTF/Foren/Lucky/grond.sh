#! /bin/bash

#
# This is teh Grond Script, designed for cracking LUKS passwords, Note that it is still under construction so everything is not working perfectly yet, but it does work... 
#

while getopts w:d:t:h: option
do
        case "${option}"
        in
                w) WORDLIST=${OPTARG};;
                d) DRIVE=${OPTARG};;
                t) THREADS=${OPTARG};;
		h) args="${args}-h ";;
		\?) 
                    exit 1;;
        esac
done


trap 'exit 0' INT

echo "Welcome to Grond, the LUKS password cracker."
echo "Note that this script might not work for your setup, it has not been stressed tested, so there are a couple of bugs in it."
echo "When Grond finds the password, it should close all of the extra windows and print the Password.  If it is not showing the correct password, check the grond.log file."
echo "The date is currently"
date

# devmapper is used to map the drive, once cracked you should be able to mount the drive with "mount /dev/mapper/grondi /mnt" 
#also note that if the password is cracked and you need to crack another one, then change this to something else
devmapper="grondmapper" 
pwtries="0"

# Threads
if [ "$THREADS" == "1" ] ; then
	echo "Starting one thread"
	split -n 1 $WORDLIST grond
	WORDLIST2=$WORDLIST

elif [ "$THREADS" == "2" ] ; then
	echo "launching second thread"
	split -n 2 $WORDLIST grond
	WORDLIST2="grondaa"
	xterm -e ./grond.sh -t 1 -d $DRIVE -w grondab 

elif [ "$THREADS" == "3" ] ; then
	echo "Launching 3 threads"
	split -n 3 $WORDLIST grond
	WORDLIST2="grondaa"
	xterm -e ./grond.sh -t 1 -d $DRIVE -w grondab &
	xterm -e ./grond.sh -t 1 -d $DRIVE -w grondac &

elif [ "$THREADS" == "4" ] ; then
	echo "Launching 4 thrads"
	split -n 4 $WORDLIST grond
	WORDLIST2="grondaa"
	xterm -e ./grond.sh -t 1 -d $DRIVE -w grondab & 
	xterm -e ./grond.sh -t 1 -d $DRIVE -w grondac & 
	xterm -e ./grond.sh -t 1 -d $DRIVE -w grondad & 

elif [ "$THREADS" == "8" ] ; then
	echo "Launching 8 threads"
	split -n 8 $WORDLIST grond
	WORDLIST2="grondaa"
	xterm -e ./grond.sh -t 1 -d $DRIVE -w grondab & 
	xterm -e ./grond.sh -t 1 -d $DRIVE -w grondac & 
	xterm -e ./grond.sh -t 1 -d $DRIVE -w grondad & 
	xterm -e ./grond.sh -t 1 -d $DRIVE -w grondae & 
	xterm -e ./grond.sh -t 1 -d $DRIVE -w grondaf & 
	xterm -e ./grond.sh -t 1 -d $DRIVE -w grondag & 
	xterm -e ./grond.sh -t 1 -d $DRIVE -w grondah & 
else 
	echo "Sorry, the number of threads (-t)  is not a valid number.  Please try again."
	kill 0
fi


for pw in `cat $WORDLIST2`
        do
        if ls /dev/mapper | grep $devmapper > /dev/null; then
                echo "Finished at" 
                date
                echo "Total passwords tried in this thread = " $pwtries
                echo "Game Over" 
                exit 0

	else    
		###### MAGIC ######  
		 echo $pw | cryptsetup luksOpen $DRIVE $devmapper
       		
		if ls /dev/mapper | grep $devmapper > /dev/null; then
               		echo "hello.  The password apears to be " $pw
               		echo "hello.  The password apears to be " $pw >> grond.log
               	else
			let pwtries++
        	        echo "Trys = "$pwtries "Failed--------------------------------" $pw	
			echo $WORDLIST $pwtries >> grond.log 
		fi
        fi
done

echo "Unfortunatly it looks like you are out of luck.  Try building a better password list and try again"
echo "Total passwords tried for this thread" $pwtries 
date 
bash

HELP() {

echo "Usage grond [options] "
echo "Notes about Grond... 

Grond is a LUKS password cracker.  It works by trying to mount the specified drive with a password from a password file, if the password fails it moves on to the next password.  Grond was created to help speed up the pasword cracking process up by offering threads and by automating the process.  

Threads:  Threads is basically just launching the script again so you can chew through more password in a shorter amount of time 
"
echo "Options 

Example:   ./grond.sh -t 8 -w grondpw.txt -d /dev/sda2
 
The above example runs Gron with 8 threads and with password list grondpw.txt.
"
}

