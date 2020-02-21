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
sudo chmod 777 awscraft
wget https://raw.githubusercontent.com/FlantasticDan/awscraft/master/AWS%20Instance/InstanceController.py -P ./awscraft/
wget https://raw.githubusercontent.com/FlantasticDan/awscraft/master/AWS%20Instance/data_manager.py -P ./awscraft/
wget https://raw.githubusercontent.com/FlantasticDan/awscraft/master/AWS%20Instance/first_run_setup.py -P ./awscraft/

echo "Resourced Fetched, Starting First Run"
cd awscraft
python3 first_run_setup.py
rm first_run_setup.py

echo "   ###    ##      ##  ######   ######  ########     ###    ######## ######## "
echo "  ## ##   ##  ##  ## ##    ## ##    ## ##     ##   ## ##   ##          ##    "
echo " ##   ##  ##  ##  ## ##       ##       ##     ##  ##   ##  ##          ##    "
echo "##     ## ##  ##  ##  ######  ##       ########  ##     ## ######      ##    "
echo "######### ##  ##  ##       ## ##       ##   ##   ######### ##          ##    "
echo "##     ## ##  ##  ## ##    ## ##    ## ##    ##  ##     ## ##          ##    "
echo "##     ##  ###  ###   ######   ######  ##     ## ##     ## ##          ##    "
echo "                      Instance Installation Complete                         "
