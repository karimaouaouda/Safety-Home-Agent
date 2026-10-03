import asyncio

clients = set()

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"[+] New connection from {addr}")
    clients.add(writer)

    try:
        while True:
            data = await reader.readuntil(b'\n')
            # flush reader
            if not data:
                print('no data')
                break
            message = data.decode().strip()
            print(f"[{addr}] {message}")

            # Broadcast to all connected clients
            for client in clients:
                print('loop')
                if client != writer:
                    client.write(f"[{addr}] {message}\n".encode())
                    print('before drain')
                    await client.drain()
                    print('drain')
            print('out of loop')
    except asyncio.CancelledError:
        pass
    finally:
        print(f"[-] Disconnected: {addr}")
        clients.remove(writer)
        writer.close()
        await writer.wait_closed()

async def main():
    server = await asyncio.start_server(handle_client, '0.0.0.0', 8765)
    print("Server running on port 8765...")
    async with server:
        await server.serve_forever()

asyncio.run(main())
