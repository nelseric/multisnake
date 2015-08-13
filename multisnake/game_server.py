''' Contains server logic '''

class MultisnakeServer(object):
    """docstring for MultisnakeServer"""
    def __init__(self):
        super(MultisnakeServer, self).__init__()
        self._next_id = 0
        self.players = {}

    def next_id(self):
        self._next_id += 1
        return self._next_id

    def add_player(self, player_id):
        """A player has joined the game"""
        if not self.players.has_key(player_id):
            self.players[player_id] = Player(player_id)
        else:
            print "Extra player! {}".format(player_id)

    def remove_player(self, player_id):
        """ The player leaves the game """
        del self.players[player_id]
    
    def update(self):
        """ Do Game Logic """
        print "There are {} players connected.".format(len(self.players))
        # print(self.players)


class Player(object):
    """ Player info """
    def __init__(self, player_id):
        super(Player, self).__init__()
        self.player_id = player_id
        