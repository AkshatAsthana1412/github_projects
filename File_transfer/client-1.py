import socket
import logging

logger = logging.getLogger('Client_A')
logging.basicConfig(level=logging.DEBUG)

client_socket = socket.socket()

host = socket.gethostname()
port = 8989

logger.debug(f'connecting to the server at port {port}...')
client_socket.connect((host, port))
logger.debug('Sending test message..')
client_socket.send(bytes('Hi server', 'ascii'))

with open('file_from_server.txt', 'wb') as outfile:
    logger.debug('Receiving file from server...')
    data = client_socket.recv(1024)
    while data:
        outfile.write(data)
        data = client_socket.recv(1024)
    logger.debug('File received successfully!')

logger.debug('closing client socket..')
client_socket.close()

