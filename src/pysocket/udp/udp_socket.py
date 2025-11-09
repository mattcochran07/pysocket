import socket
from socket import PySocket

class UdpSocket(PySocket):
    """Udp Socket class for sending/receiving packets

    Example Use:
        Sending:
            udp_sender = UdpSocket('localhost', 7777)
            udp_sender.send("Hello World")
        Receiving:
            udp_listener = UdpSocket('localhost', 7777)
            recv_str: str = udp_listener.listen_thread()

    Args:
        PySocket (_type_): inherits from base abstract class Socket
    """

    def __init__(self,
                 ip: str,
                 port: int,
                 maxbuffer: int = 1024) -> None:
        """ Constructor for UdpSocket class

        Args:
            ip (str): ip address to send/recv on
            port (int): port to send/recv on
        """
        super.__init__(ip, port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def recv(self) -> str:
        """Listen on the ip:port from constructor and decode if we have anything

        Returns:
            str: decoded stream received
        """
        self.socket.bind((self.ip, self.port))
        recv_bytes: bytes = self.socket.recv(self.maxbuffer)
        self.socket.close()
        
        return recv_bytes.decode()

    def send(self, stream: str) -> None:
        """Send the contents of stream on the ip:port from constructor

        Args:
            stream (str): stream we want to send
        """
        self.socket.sendto(stream.encode(), (self.ip, self.port))
