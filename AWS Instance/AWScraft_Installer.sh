#!/bin/sh

echo "   ###    ##      ##  ######   ######  ########     ###    ######## ######## "
echo "  ## ##   ##  ##  ## ##    ## ##    ## ##     ##   ## ##   ##          ##    "
echo " ##   ##  ##  ##  ## ##       ##       ##     ##  ##   ##  ##          ##    "
echo "##     ## ##  ##  ##  ######  ##       ########  ##     ## ######      ##    "
echo "######### ##  ##  ##       ## ##       ##   ##   ######### ##          ##    "
echo "##     ## ##  ##  ## ##    ## ##    ## ##    ##  ##     ## ##          ##    "
echo "##     ##  ###  ###   ######   ######  ##     ## ##     ## ##          ##    "
echo "                              Installer v.0.1                                "

echo "Installing Python"
sudo yum install python3

echo "Python Installed, Installing Java"
sudo yum install java

echo "Java Installed, Installing pip"
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py
rm get-pip.py

echo "pip Installed, Installing Python Dependencies"
pip install websockets, requests

echo "Dependencies Installed, Fetching AWScraft Resources"
mkdir awscraft