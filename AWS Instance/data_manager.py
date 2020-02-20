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

