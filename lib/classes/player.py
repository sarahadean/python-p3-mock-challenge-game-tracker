class Player:

    all = []

    def __init__(self, username):
        self.username = username
        self._results = []
        self._games_played = []
        Player.all.append(username)

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username
        else:
            raise Exception("Username must be between 2 and 16 characters")

    # Adds new results to instance attribute player._results if new_result exists.
    # Returns a list of Result instances associated with the Player instance.
    # You will need to call this method in `Result.init()`.
    
    def results(self, new_result=None):
        from classes.result import Result
        if isinstance(new_result, Result):
            self._results.append(new_result)
        return [result for result in Result.all if result.player == self]
    
    #Returns a list of Game instances played by the Player instance:
    #taking in new game, appending to _games_played list and returning list of this player(self)'s
    #games played
    def games_played(self, new_game=None):
        from classes.game import Game
        from classes.result import Result
        if isinstance(new_game, Game):
            self._games_played.append(new_game)
        return [result.game for result in Result.all if result.player == self]

    def played_game(self, game):
        # return game in self._games_played
        from classes.result import Result
        return len([result.game for result in Result.all if result.player == self and result.game == game]) > 0
    
    #Returns the number of times the Player instance has played (Result instance created) 
    # the Game instance
    def num_times_played(self, game):
        from classes.result import Result
        #go thru self._games_played and count number of times game appears
        # return self._games_played.count(game)
        return len([result.game for result in Result.all if result.player == self and result.game == game])
    
    @classmethod
    def highest_scored(cls, game):
        pass
        
#-----testing-----

# user_one = Player("Mamahellcat")
# user_two = Player("a")
# print(user_two.username)