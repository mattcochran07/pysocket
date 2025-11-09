import socket
from abc import ABC, abstractmethod

class PySocket(ABC):
	"""Abstract Class for Socket library use

	Args:
		ABC (_type_): inherits from abstract ABC
	"""
	def __init__(self,
			     ip: str,
				 port: int,
				 max_buffer_size: int = 1024):
		"""Constructor for Abstract Base Class Socket

		Args:
			ip (str): ip address to connect on
			port (int): port to connect on
		"""
		self.ip = ip
		self.port = port
		self.max_buffer_size = max_buffer_size
