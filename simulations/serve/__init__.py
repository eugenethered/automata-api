import logging

from apiautomata.AutomataAPIServer import AutomataAPIServer

if __name__ == '__main__':

    options = {
        'REDIS_SERVER_ADDRESS': '192.168.1.90',
        'REDIS_SERVER_PORT': 6379
    }

    logging.basicConfig(level=logging.DEBUG)

    server = AutomataAPIServer(options)
    server.run()

    print('Automata API Server running...')
