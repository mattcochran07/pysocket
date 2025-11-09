from tcp_socket import TcpSocket, TcpSocketTypes

tcp_client = TcpSocket('localhost', 7777, TcpSocketTypes.TCP_CLIENT)
tcp_server = TcpSocket('localhost', 7777, TcpSocketTypes.TCP_SERVER)

tcp_client.send('Hello World')
print(tcp_server.recv())
