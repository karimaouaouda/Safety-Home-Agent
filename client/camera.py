import cv2
import asyncio
import websockets
import base64


class Camera:
    def __init__(self, name='camera'):
        self.name = name

        self.ws = None

    async def connect_to_ws(self):
        return None
        # uri = "ws://localhost:8765"  # Replace with your WebSocket server URI
        # return await websockets.connect(uri)


    async def start(self):
        self.ws = await self.connect_to_ws()
        cap = cv2.VideoCapture(0)
        cv2.namedWindow(self.name)
        while True:
            ret, frame = cap.read()

            if not ret:
                continue

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.flip(frame, 1)

            await self.handle_frame(frame)

            # cancel when key q clicked
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()

    def draw_danger_zones(self, frame):
        return frame
    async def handle_frame(self, frame):

        frame = self.draw_danger_zones(frame)


        cv2.imshow(self.name, frame)



        img = base64.b64encode(frame)
        print(img)
        #await self.ws.send(img)
