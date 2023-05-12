class Game:
    def __init__(self, title):
        if isinstance(title, str):
            self.title = title
            self._results = []
            self._players = []
        
    def results(self):
        from classes.result import Result
        return [r for r in Result.all if r.game == self ]
    
    def players(self):
        from classes.player import Player
        return list(set([r.player for r in self.results()]))
    
    def average_score(self, player):
        game_scores = [r.score for r in self.results() if r.player == player]
        return sum(game_scores) / len(game_scores)
        