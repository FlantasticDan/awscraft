import os
import datetime
import requests

def get_server_download_url(version='latest'):
    '''Returns the Mojang download URL for the server of version <version>'''
    version_database = requests.get('https://launchermeta.mojang.com/mc/game/version_manifest.json').json()

    if version == 'latest':
        version = version_database['latest']['release']
    
    for release in version_database['versions']:
        if release['id'] == version:
            query_url = release['url']
            break
    
    if not query_url:
        return
    
    release_data = requests.get(query_url).json()
    return release_data['downloads']['server']['url']

def download_server(url, backup=False):
    '''Downloads Minecraft Server at <url> to ./server.jar.  Overwrites existing server unless <backup> is True.'''
    download_request = requests.get(url)

    if os.path.exists('server.jar'):
        if backup:
            date_string = datetime.datetime.now().isoformat()
            date_string = date_string.replace(':', '.')
            os.rename('server.jar', f'{date_string}-server.jar')
        else:
            os.remove('server.jar')
    
    with open('server.jar', 'wb') as target:
        target.write(download_request.content)

def update_server(version='latest', backup=False):
    '''Convenience function for updating/installing the server.'''
    download_server(get_server_download_url(version=version), backup=backup)
