#!/bin/bash

find /usr/lib/maddash/maddash-webui/ -maxdepth 1 -name *.png > /usr/lib/maddash/maddash-webui/temp.txt
var=$(cat /usr/lib/maddash/maddash-webui/temp.txt | cut -d'/' -f6)
sed -i -e "78 s/.*/                            var titlePane = new MadDashTitleSpan('maddashTitle', 'index.cgi', '$var');/g" /usr/lib/maddash/maddash-webui/index.cgi

cat /etc/maddash/maddash-server/maddash.yaml | grep groups -A 1000 | grep groupMembers -B 1000 | sed '$d' | grep \" | sed -e "s/^ *//g" | sed 's/^.\{3\}//' | sed 's/"$//' | sort -u > /etc/maddash/maddash-server/temp.txt

for i in `cat /etc/maddash/maddash-server/temp.txt`
do
	ping -c 3 $i > /dev/null
	if [ $? -eq 0 ]
	then
		echo UP > /usr/lib/maddash/maddash-webui/states_hosts/$i.state
	else
		echo DOWN > /usr/lib/maddash/maddash-webui/states_hosts/$i.state 
	fi
done
