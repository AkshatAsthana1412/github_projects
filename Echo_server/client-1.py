import socket
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('Client-1')

logger.info('instantiating client socket')  
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

logger.info('get current machine name')
host = socket.gethostname()
port = 9999 #port on which to connect with the server

logger.info('connect to the server')

# try:
client_socket.connect((host, port))
try:
    while True:
        logger.info('send data to server')
        client_socket.send(input().encode('ascii'))

        logger.info('receive data from server')
        data = client_socket.recv(1024).decode('ascii')

        logger.debug(f'received: <{data}> (from server)')
    # except Exception as e:
    #     print(e)
except ConnectionAbortedError:
    logger.error('connection closed')
    logger.info('closing socket')
    client_socket.close()
