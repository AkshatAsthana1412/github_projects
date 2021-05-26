import socket
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('server')

logger.debug('Instantiating the sever socket')
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

logger.debug('Get local machine name')
host = socket.gethostname()
port = 9999

address = (host, port)
logger.debug('binding the socket to address')
server_socket.bind(address)

logger.debug('Queue upto 5 connections')
server_socket.listen(5)

while True:
    logger.debug('accepting connection...')
    conn, addr = server_socket.accept()
    logger.debug(f'connected to {addr}')

    data = None
    while data not in ['bye', 'BYE', 'Bye']:
        logger.debug('receive data')
        data = conn.recv(1024).decode('ascii')
        logger.info(f'received: <{data}> from client')

        logger.debug('sending data to client')
        conn.send(data.encode('ascii'))

    logger.debug('Closing the connection')
    conn.close()
