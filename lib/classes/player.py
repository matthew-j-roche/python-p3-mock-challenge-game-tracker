class Player:

    all = []

    def __init__(self, username):
        self.username = username
        self._results = []
        self._games_played = []
        
    def results(self):
        from classes.result import Result
        return [r for r in Result.all if r.player == self ]
 
    
    def games_played(self):
        from classes.game import Game
        return list(set([r.game for r in self.results()]))
    
    def played_game(self, game):
        if game in self.games_played():
            return True
        else:
            return False
        
    def num_times_played(self, game):
        return len([r for r in self.results() if r.game == game])
        
    
    @classmethod
    def highest_scored(cls, game):
        pass
        
