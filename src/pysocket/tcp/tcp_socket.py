from socket import PySocket

from enum import auto, Enum

class TcpSocket(PySocket):
    """Tcp Socket class for send/recv on ip:port

    Args:
        PySocket (_type_): inherits from abstract base class 
    """

    class TcpSocketTypes(Enum):
        TCP_SERVER = auto()
        TCP_CLIENT = auto()

    def __init__(self,
                 ip: str,
                 port: int,
                 tcp_type: TcpSocketTypes) -> None:
        """Constructor for TCP Server AND Client

        Args:
            ip (str): _description_
            port (int): _description_
        """
        super.__init__(ip, port)
        if tcp_type == TcpSocket.TcpSocketTypes.TCP_SERVER:
            pass
        elif tcp_type == TcpSocket.TcpSocketTypes.TCP_CLIENT:
            pass

    def connect(self):
        """Connect method to be called when base class send_message
        """