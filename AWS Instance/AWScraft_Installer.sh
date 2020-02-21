#!/bin/sh

echo "   ###    ##      ##  ######   ######  ########     ###    ######## ######## "
echo "  ## ##   ##  ##  ## ##    ## ##    ## ##     ##   ## ##   ##          ##    "
echo " ##   ##  ##  ##  ## ##       ##       ##     ##  ##   ##  ##          ##    "
echo "##     ## ##  ##  ##  ######  ##       ########  ##     ## ######      ##    "
echo "######### ##  ##  ##       ## ##       ##   ##   ######### ##          ##    "
echo "##     ## ##  ##  ## ##    ## ##    ## ##    ##  ##     ## ##          ##    "
echo "##     ##  ###  ###   ######   ######  ##     ## ##     ## ##          ##    "
echo "                              Installer v.0.2                                "

echo "Installing Python"
sudo yum -y install python3
sudo yum -y install python3-pip

echo "Python Installed, Installing Java"
sudo yum -y install java

echo "Java Installed, Installing Python Dependencies"
pip3 install websockets requests

echo "Dependencies Installed, Fetching AWScraft Resources"
mkdir awscraft