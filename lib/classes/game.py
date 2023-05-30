class Game:
    all = []

    def __init__(self, title):
        self.title = title
        self._results = []
        self._players = []
        Game.all.append(self)


    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title) > 0:
            self._title = title
        else:
            raise Exception("Title must have more than 0 characters")
        
    def results(self, new_result=None):
        from classes.result import Result
        if isinstance(new_result, Result):
            self._results.append(new_result)
        return [result for result in Result.all if result.game == self]
    
    
    def players(self, new_player=None):
        from classes.player import Player
        if isinstance(new_player, Player):
            self._players.append(new_player)
        return [result.player for result in self.results()]
       
    # Returns the average of all the player's scores for the Game instance
    def average_score(self, player):
        player_scores = [result.score for result in self._results if result.player == player]
        # score_sum = []
        # for result in self._results:
        #     if result.player == player:
        #         score_sum.append(result.score)
        # total = sum(score_sum)
        avg_score = sum(player_scores)/len(player_scores)
        # avg = total / len(score_sum)
        return avg_score
        # return sum(score_sum)/len(score_sum)
        
        # sum(self._results)/len(self._results)

        


# ------- testing --------
# pokemon = Game("Pokemon")
# print(pokemon.title)