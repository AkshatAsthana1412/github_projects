import socket
import logging

logger = logging.getLogger('Server')
logging.basicConfig(level=logging.DEBUG)

host = ''
port = 8989 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
logger.debug('binding socket to address...')
server_socket.bind((host, port))
logger.debug('listening for connections...')
server_socket.listen(2)

filename = input('enter the filename')
conn, addr = server_socket.accept()
logger.debug(f'connected with {addr}')
logger.debug('Receiving test message..')
logger.info(f'Test message {conn.recv(1024).decode("ascii")}')
with open(filename, 'rb') as file:
    logger.debug('sending file to client..')
    data = file.read(1024)
    while data:
        conn.send(data)
        data = file.read(1024)
    logger.debug('file sent!')
server_socket.close()
    