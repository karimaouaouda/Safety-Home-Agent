import asyncio
import os
from multiprocessing import Process, Queue
import websockets

class BaseProcess:
    def __init__(self, name:str):
        self.name = name

        self.process:Process|None = None

        self.connected_clients = set()

        self.setup()

    def setup(self):
        try:
            self.create_process()
        except ChildProcessError as e:
            print("failed to create process")

    def create_process(self):
        self.process = Process(target=self.function)

    def get_pid(self):
        return self.process.pid

    def start(self):
        self.process.start()

    def stop(self):
        self.process.terminate()

    def join(self):
        self.process.join()

    async def target(self):
        await self.run_websocket_server('0.0.0.0', 8765)
    def function(self):
        asyncio.run(self.target())

    async def run_websocket_server(self, host:str = '0.0.0.0', port:int=8765):
        async with websockets.serve(self.handle_client, "0.0.0.0", 8765):
            print("✅ WebSocket server is running at ws://0.0.0.0:8765")
            await asyncio.Future()  # Keep running forever

    async def handle_client(self, websocket):
        # Add clientfolder to the set
        self.connected_clients.add(websocket)
        print(f"[+] New connection: {websocket.remote_address}")

        try:
            async for message in websocket:
                print(f"[{websocket.remote_address}] {message}")
                # Broadcast to all other connected clients
                for client in self.connected_clients:
                    if client != websocket:
                        await client.send(f"{websocket.remote_address} says: {message}")
        except websockets.exceptions.ConnectionClosed:
            print(f"[-] Disconnected: {websocket.remote_address}")
        finally:
            self.connected_clients.remove(websocket)
