import asyncio

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"Подключение от {addr}")

    try:
        while True:
            data = await reader.read(1024)  
            if not data:
                print(f"Отключение {addr}")
                break

            message = data.decode()
            print(f"Получено от {addr}: {message}")

            writer.write(data)
            await writer.drain()
    except asyncio.IncompleteReadError:
        print(f"Клиент {addr} принудительно закрыл соединение.")
    finally:
        writer.close()
        await writer.wait_closed()
        print(f"Соединение с {addr} закрыто.")

async def main():
    server = await asyncio.start_server(
        handle_client, '127.0.0.1', 8888
    )

    addr = server.sockets[0].getsockname()
    print(f"Сервер запущен на {addr}")

    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())
