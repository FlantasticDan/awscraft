'''Handles Settings and Configuration Data for AWScraft.'''

import os
import json
import nbt.nbt as nbt

class ConfigurationSettings:
    '''Stores and detects User Configuration Data'''

    def __init__(self):
        self.awscraft_dir = None
        self.data_directory = None
        self.launcher = None
        self.user_id = None
        self.host = None

    def start(self):
        '''Startup Config Operations'''
        appdata = os.getenv('APPDATA')
        self.awscraft_dir = os.path.join(appdata, 'AWScraft')

        if os.path.isdir(self.awscraft_dir):
            settings = os.path.join(self.awscraft_dir, 'user_settings.json')
            if not os.path.isfile(settings):
                return True

            with open(settings, 'r') as user_data:
                user_settings = json.load(user_data)

            self.data_directory = user_settings['data_directory']
            self.launcher = user_settings['launcher']
            self.user_id = user_settings['user_id']
            self.host = user_settings['host']

            return False
        else:
            os.mkdir(self.awscraft_dir)
            return True

    def save(self):
        '''Save settings to user data.'''
        user_settings = {
            'data_directory': self.data_directory,
            'launcher': self.launcher,
            'user_id': self.user_id,
            'host': self.host
        }

        export = os.path.join(self.awscraft_dir, 'user_settings.json')

        if os.path.isfile(export):
            os.remove(export)

        with open(export, 'w') as settings:
            json.dump(user_settings, settings)

    def find_minecraft_data(self):
        '''Find the .minecraft user data folder.'''
        appdata = os.getenv('APPDATA')
        minecraft_data = os.path.join(appdata, '.minecraft')

        if os.path.isdir(minecraft_data):
            self.data_directory = minecraft_data
            return minecraft_data

        return False

    def find_minecraft_launcher(self):
        '''Find the Minecraft Launcher EXE.'''
        program_files = os.getenv('ProgramFiles(x86)')
        minecraft_exe = os.path.join(program_files, 'Minecraft Launcher', 'MinecraftLauncher.exe')

        if os.path.isfile(minecraft_exe):
            self.launcher = minecraft_exe
            return minecraft_exe

        return False

    def get_display_name(self):
        '''Returns the display name of the currently selected Minecraft User.'''
        profile_file = os.path.join(self.data_directory, 'launcher_profiles.json')
        if not os.path.isfile(profile_file):
            return False

        with open(profile_file, 'r') as profile:
            data = json.load(profile)

        return data['authenticationDatabase'][data['selectedUser']['account']]['profiles'][data['selectedUser']['profile']]['displayName']

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
        
        return True
