'''
  Multisnake Server
'''
from twisted.internet import protocol, reactor, endpoints


class Echo(protocol.Protocol, object):
    ''' echo '''
    def __init__(self, addr):
        super(Echo, self).__init__()
        self.addr = addr

    def connectionMade(self):
        print "Hello from {}".format(self.addr)
        self.transport.write("Hello\n")

    def connectionLost(self, reason):
        print "Lost {} because {}".format(self.addr, reason.value)

    def dataReceived(self, data):
        print data
        self.transport.write(data)

class EchoFactory(protocol.Factory, object):
    ''' Echo Factory'''
    def __init__(self):
        super(EchoFactory, self).__init__()

    def buildProtocol(self, addr):
        return Echo(addr)

def start():
    endpoints.serverFromString(reactor, "tcp:1234").listen(EchoFactory())
    reactor.run()
