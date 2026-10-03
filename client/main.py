from client.camera import Camera
import asyncio


camera1 = Camera('karim')

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(camera1.start())