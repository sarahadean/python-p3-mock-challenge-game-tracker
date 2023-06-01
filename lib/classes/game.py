class Game:
    def __init__(self, title):
      self.title = title
      self._results = [] #list of results for each game instance
      self._players = []


    @property
    def title(self):
        return self._title
   
    @title.setter
    def title(self, title):
        if not hasattr(self, 'title') and isinstance(title, str) and len(title) > 0:
            self._title = title
        else:
            raise Exception('Title must be string greater than 0 characters')
        
    #Returns list of results for each game
    def results(self, new_result=None):
        from classes.result import Result
        if new_result and isinstance(new_result, Result):
            self._results.append(new_result)
        return self._results


    #Returns list of players for each game
    def players(self, new_player=None):
        from classes.player import Player
        if new_player and isinstance(new_player, Player):
            self._players.append(new_player)
        return self._players
   

