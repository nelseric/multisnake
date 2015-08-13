'''
  Multisnake Client
'''
from __future__ import print_function

from twisted.internet import protocol, reactor, endpoints

class PrintClient(protocol.Protocol, object):
    """Multisnake debug client"""
    def __init__(self):
        super(PrintClient, self).__init__()

    def dataReceived(self, data):
        print(data)

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
    reactor.run()

