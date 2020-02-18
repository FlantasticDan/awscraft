import asyncio
import websockets

class MinecraftServer:
    '''Asynchronous Subprocess Minecraft Server Controller'''

    def __init__(self):
        self.running = asyncio.Event()
        self.players = 0

    async def runServer(self):
        self.process = await asyncio.create_subprocess_shell('java -jar server.jar', stdout=asyncio.subprocess.PIPE, stdin=asyncio.subprocess.PIPE)
        await self.logReader()

    async def logReader(self):
        while True:
            output = await self.process.stdout.readline()

            if output == b'':
                break

            self.parseLog(str(output))

    def parseLog(self, logOutput):
        log = logOutput.split(']: ')[1]

        if log.find('Done') != -1 and not self.running.is_set():
            self.running.set()
        elif log.find('There are') != -1 and log.find('of a max') != -1 and not self.listRequest.is_set():
            self.players = [int(i) for i in log.split() if i.isdigit()][0]
            self.listRequest.set()

    def sendCommand(self, cmd: str):
        command = bytes('{cmd}\n')
        self.process.stdin.write(command)
        self.process.stdin.flush()

    async def updatePlayers(self):
        self.listRequest = asyncio.Event()
        self.sendCommand('list')
        await self.listRequest.wait()
        return self.players

class WebsocketServer:
    '''Websocket Server Manager'''

    def __init__(self, minecraftServer: MinecraftServer):
        self.clients = set()
        self.minecraft = minecraftServer

    async def runServer(self):
        self.server = await websockets.server.serve(self.handler, 'localhost', 35351)
        await self.server.wait_closed()
        print('Server Closed')

    async def onClientConnect(self, websocket):
        self.clients.add(websocket)
        await self.responseManager(websocket)

    async def onClientDisconnect(self, websocket):
        self.clients.remove(websocket)

    async def responseManager(self, websocket):
        try:
            async for message in websocket:
                pass
        finally:
            self.onClientDisconnect(websocket)

    async def handler(self, websocket, path):
        await self.onClientConnect(websocket)
        await self.minecraft.running.wait()

async def main(minecraft, websocket):
    await asyncio.gather(minecraft.runServer(),
                         websocket.runServer())


if __name__ == '__main__':
    minecraft = MinecraftServer()
    websocket = WebsocketServer(minecraft)

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(minecraft, websocket))
        loop.run_until_complete(loop.shutdown_asyncgens())
    finally:
        loop.close()

