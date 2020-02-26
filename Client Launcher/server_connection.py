import json
import asyncio
import websockets

def connect_to_server():
    '''Connect to AWS Lambda to request instance and returns IP address.'''
    # P L A C E H O L D E R  F U N C T I O N #
    return 'localhost'

class WebsocketHandler:
    def __init__(self, ip, display_name, ui, port='35351'):
        self.url = f"ws://{ip}:{port}"
        self.ip = ip
        establish = {'type': 'establish', 'display_name': display_name}
        self.establish_payload = json.dumps(establish)
        self.ui = ui

    async def connect(self):
        while True: 
            try:
                self.websocket = await websockets.connect(self.url)
                break
            except Exception:
                await asyncio.sleep(1)

        welcome = await self.websocket.recv()
        welcome = json.loads(welcome)

        if welcome['type'] == 'status' and welcome['status'] == 'connected':
            # Connected to Websocket and Minecraft Server is Running
            await self.websocket.send(self.establish_payload)
        elif welcome['type'] == 'status' and welcome['status'] == 'booting':
            # Connected to Websocket and Minecraft Server is Booting
            welcome = await self.websocket.recv()
            welcome = json.loads(welcome)
            if welcome['type'] == 'status' and welcome['status'] == 'connected':
                await self.websocket.send(self.establish_payload)

        self.ui.update_connect_button(3, self.ip)
        await self.listener()

    async def listener(self):
        async for message in self.websocket:
            pass