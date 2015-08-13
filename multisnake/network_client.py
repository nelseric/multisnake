'''
  Multisnake Client
'''
from __future__ import print_function

from twisted.internet import protocol, reactor, endpoints, task

# from multisnake.game_client_gui import GameWindow

class PrintClient(protocol.Protocol, object):
    """Multisnake debug client"""
    def __init__(self):
        super(PrintClient, self).__init__()

    def dataReceived(self, data):
        print(data)

    def connectioNMade(self, add):
        print("I've connected to {}".format(addr))

    def connectionLost(self, reason):
        print(reason.value)

class PrintClientFactory(protocol.Factory, object):
    """docstring for PrintClientFactory"""

    def __init__(self):
        super(PrintClientFactory, self).__init__()

    def buildProtocol(self, addr):
        return PrintClient()

def start():
    ''' Client Entrypoint '''
    endpoints.clientFromString(reactor, "tcp:localhost:1234").connect(PrintClientFactory())

    # gui = GameWindow()

    # gui_loop = task.LoopingCall(gui.update)
    # gui_loop.start(1.0)

    
    reactor.run()

