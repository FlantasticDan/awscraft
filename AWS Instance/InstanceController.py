import asyncio
import json
from colorama import init as color_prep
from termcolor import cprint, colored
import websockets

class MinecraftServer:
    '''Asynchronous Subprocess Minecraft Server Controller'''

    def __init__(self):
        self.running = asyncio.Event()
        self.players = 0
        self.websocket = type(WebsocketServer)
        self.kickq = []

    def link_websocket_server(self, websocket):
        self.websocket = websocket

    async def runServer(self):
        self.process = await asyncio.create_subprocess_shell('java -jar server.jar', stdout=asyncio.subprocess.PIPE, stdin=asyncio.subprocess.PIPE)
        cprint('Minecraft Server Starting', 'yellow', None)
        await self.logReader()
        cprint('Minecraft Server Shutdown', 'red', None, attrs=['bold'])

    async def logReader(self):
        while True:
            output = await self.process.stdout.readline()

            if output == b'':
                break

            self.parseLog(str(output))

    def parseLog(self, logOutput):
        log = logOutput.split(']: ')[1]

        if log.find('Done') != -1 and not self.running.is_set():
            # Server has Started
            self.running.set()
            cprint('Minecraft Server Started', 'green', None, ['bold'])
        elif log.find('There are') != -1 and log.find('of a max') != -1 and not self.listRequest.is_set():
            # Updating the Player Count
            self.players = [int(i) for i in log.split() if i.isdigit()][0]
            self.listRequest.set()
        elif log.find(' joined the game') != 1:
            # Player Connection
            newPlayer = log.split(' joined the game')[0]
            self.websocket.confirm_player(newPlayer)

    def sendCommand(self, cmd: str):
        command = bytes('{cmd}\n')
        self.process.stdin.write(command)
        self.process.stdin.flush()

    async def updatePlayers(self):
        self.listRequest = asyncio.Event()
        self.sendCommand('list')
        await self.listRequest.wait()
        return self.players
    
    def kick_player(self, player, reason):
        '''Kick <player> from Minecraft Server for given <reason>.'''
        cmd = f'kick {player} {reason}'
        self.kickq.append(player)
        self.sendCommand(cmd)

class WebsocketServer:
    '''Websocket Server Manager'''

    def __init__(self, minecraftServer: MinecraftServer):
        self.clients = dict()
        self.minecraft = minecraftServer
        self.minecraft.link_websocket_server(self)

    async def runServer(self):
        self.server = await websockets.server.serve(self.handler, 'localhost', 35351)
        cprint('Websocket Server Started', 'green', None, ['bold'])
        await self.server.wait_closed()
        cprint('Websocket Server Closed', 'red', None, ['bold'])

    async def onClientConnect(self, websocket):

        # Notify Client of Minecraft Server Status
        if self.minecraft.running.is_set():
            welcome = {'type': 'status', 'status': 'connected'}
            await websocket.send(json.dumps(welcome))
        else:
            welcome = {'type': 'status', 'status': 'booting'}
            await websocket.send(json.dumps(welcome))

            await self.minecraft.running.wait()
            welcome = {'type': 'status', 'status': 'connected'}
            await websocket.send(json.dumps(welcome))

        # Register Client with Client Handler
        establish = await websocket.recv()
        establish = json.loads(establish)
        display_name = establish['display_name']
        self.clients[display_name] = ClientHandler(display_name, websocket)

        # Enter Client Response Manager
        await self.clients[display_name].responseManager()

    async def handler(self, websocket, path):
        await self.onClientConnect(websocket)
    
    def confirm_player(self, player):
        '''Check that given <player> has connected via the websocket.'''
        if player in self.clients.keys():
            print_player = colored(player, 'magenta', None, ['bold'])
            print(f'{print_player} has been authenticated and connected to the Minecraft Server.')
            return
        else:
            pass


class ClientHandler:
    def __init__(self, display_name, websocket):
        self.display_name = display_name
        self.websocket = websocket

        player = colored(display_name, 'magenta', None, ['bold'])
        print(f'{player} has connected to the Websocket Server')

    async def responseManager(self):
        try:
            async for message in self.websocket:
                pass
        finally:
            pass    

async def main(minecraft, websocket):
    await asyncio.gather(minecraft.runServer(),
                         websocket.runServer())


if __name__ == '__main__':
    color_prep()

    minecraft = MinecraftServer()
    websocket = WebsocketServer(minecraft)

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(minecraft, websocket))
        loop.run_until_complete(loop.shutdown_asyncgens())
    finally:
        loop.close()

