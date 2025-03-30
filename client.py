import asyncio

async def tcp_echo_client(message, host='127.0.0.1', port=8888):
    reader, writer = await asyncio.open_connection(host, port)
    print(f'Подключились к серверу {host}:{port}')

    print(f'Отправляем: {message!r}')
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(1024)
    print(f'Получено: {data.decode()!r}')

    print('Закрытие соединения')
    writer.close()
    await writer.wait_closed()

if __name__ == '__main__':
    message = "Привет, сервер!"
    asyncio.run(tcp_echo_client(message))
