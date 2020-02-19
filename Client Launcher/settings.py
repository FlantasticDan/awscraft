'''Handles Settings and Configuration Data for AWScraft.'''

import os
import nbt.nbt as nbt

class ConfigurationSettings:
    '''Stores and detects User Configuration Data'''

    def __init__(self):
        self.data_directory = self.find_minecraft_data()
        self.launcher = self.find_minecraft_launcher()

    def find_minecraft_data(self):
        '''Find the .minecraft user data folder.'''
        appdata = os.getenv('APPDATA')
        minecraft_data = os.path.join(appdata, '.minecraft')

        if os.path.isdir(minecraft_data):
            return minecraft_data

        return False

    def find_minecraft_launcher(self):
        '''Find the Minecraft Launcher EXE.'''
        program_files = os.getenv('ProgramFiles(x86)')
        minecraft_exe = os.path.join(program_files, 'Minecraft Launcher', 'MinecraftLauncher.exe')

        if os.path.isfile(minecraft_exe):
            return minecraft_exe

        return False

    def update_server_address(self, ip, name='AWScraft'):
        '''
        Updates the server named <name> with new IP address <ip> in servers.dat.
        Otherwise creates a new server entry named <name> with <ip>
        '''
        server_file = os.path.join(self.data_directory, 'servers.dat')
        if not os.path.isfile(server_file):
            return False # Check Server File Exists

        with open(server_file, 'rb') as binary:
            server = nbt.NBTFile(buffer=binary)

        updated = False
        for entry in server['servers']:
            if entry['name'] == name:
                entry['ip'] = ip
                updated = True

        if not updated:
            new_server = nbt.TAG_Compound()
            new_server.tags.append(nbt.TAG_String(name='name', value=name))
            new_server.tags.append(nbt.TAG_String(name='ip', value=ip))

            server['servers'].append(new_server)

        os.remove(server_file)
        with open(server_file, 'wb') as new_binary:
            server.write_file(buffer=new_binary)

ConfigurationSettings()
