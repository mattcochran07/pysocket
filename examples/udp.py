from udp_socket import UdpSocket

udp_conn = UdpSocket('localhost', 7777)

udp_conn.send('Hello World')
print(f'Udp Client received: {udp_conn.recv()}')
