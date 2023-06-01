class Player:
    
    def __init__(self, username):
        self.username = username
        self._results = []
        self._games = []

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username
        else:
            raise Exception('Usernames must be strings between 2 and 16 characters')


    # Adds new results from each player instance - creating list of results for 
    #   single player. 
    #Self = player instance
    #Passing in new_result for this player
    def results(self, new_result=None):
        from classes.result import Result
        if new_result and isinstance(new_result, Result):
            self._results.append(new_result)
        return self._results
    
    #Returns a list of Game instances played by the Player instance.
    def games_played(self, new_game=None):
        from classes.game import Game
        if new_game and isinstance(new_game, Game):
            self._games.append(new_game)
        return self._games

    def played_game(self):
        pass