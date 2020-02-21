import subprocess
import os
import data_manager as data

# Download Latest Server .jar
data.update_server()

# Run First Time
subprocess.run('java -jar server.jar nogui')

# Accept Mojang EULA
with open('eula.txt', 'r') as eula:
    text = eula.readlines

text[2] = 'eula=true\n'

with open('eula.txt', 'w') as eula:
    eula.writelines(text)
