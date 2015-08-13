'''
  Multisnake Server
'''
from twisted.internet import protocol, reactor, endpoints, task

from multisnake.game_server import MultisnakeServer

class PlayerConnection(protocol.Protocol, object):
    ''' represents a player's network session '''
    def __init__(self, game, addr):
        super(PlayerConnection, self).__init__()
        self.addr = addr
        self.game = game
        self.player_id = game.next_id()

    def connectionMade(self):
        print "Hello from {}".format(self.addr)
        self.game.add_player(self.player_id)
        self.transport.write("Hello\n")

    def connectionLost(self, reason):
        print "Lost {} because {}".format(self.addr, reason.value)
        self.game.remove_player(self.player_id)

    def dataReceived(self, data):
        print data
        self.transport.write(data)

class PlayerConnectionFactory(protocol.Factory, object):
    ''' PlayerConnection Factory'''
    def __init__(self, game):
        super(PlayerConnectionFactory, self).__init__()
        self.game = game

    def buildProtocol(self, addr):
        return PlayerConnection(self.game, addr)

def start():
    game = MultisnakeServer()

    server_update = task.LoopingCall(game.update)
    server_update.start(1.0)

    endpoints.serverFromString(reactor, "tcp:1234").listen(PlayerConnectionFactory(game))

    reactor.run()
