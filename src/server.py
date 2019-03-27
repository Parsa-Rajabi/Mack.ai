from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from wit import Wit
import personality as p
from socket import *

import sys                                  # In order to terminate the program
import getopt                               # for processsing of args from cmd

access_token = 'CDNAWIU4OA5JUBDQ3JESSC6AVZWRTDVR'

client = Wit(access_token=access_token)

def main(argv):

    serverPort = 6789

    # Get the port number at start up, but will default to 6789
    try:
        opts, args = getopt.getopt(argv,"hp:",["port="])
    except getopt.GetoptError:
        print ('webserver.py -p <port number>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print ('webserver.py -p <port number>')
            sys.exit()
        elif opt in ("-p", "--port"):
            serverPort = int(arg)

    print ('Server is running on port ', serverPort)

    # Create a TCP server socket
    # (AF_INET is used for IPv4 protocols)
    # (SOCK_STREAM is used for TCP)
    # This sets up a TCP sockect
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Bind the socket to server address and server port
    serverSocket.bind(("", serverPort))

    # Listen to at most 1 connection at a time
    serverSocket.listen(1)

    # Server should be up and running and listening to the incoming connections
    # keep looping forever
    while True:
        print('The server is ready to receive data....')


        connectionSocket, addr = serverSocket.accept()
        print(connectionSocket)


        try:

            message = connectionSocket.recv(1024).decode(encoding='UTF-8')
            resp = client.message(message)
            response = p.tree.navigate_tree(resp, "topic", p.tree.get_root())
            connectionSocket.send(response.encode(encoding='UTF-8'))
            print(response)

            while True:
                message = connectionSocket.recv(1024).decode(encoding='UTF-8')
                resp = client.message(message)
                response = p.tree.navigate_tree(resp, "topic", p.tree.get_root())
                connectionSocket.send(response.encode(encoding='UTF-8'))
                print(response)

        except IOError:

                connectionSocket.close()


    serverSocket.close()

    sys.exit()

if __name__ == "__main__":
    main(sys.argv[1:])
