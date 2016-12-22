from django.db import models


# going to hold the games location
class GameLocation(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name

# Model of a basketball game
class Game(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200, default='', blank=True)
    game_fk = models.ForeignKey(GameLocation, related_name='games', on_delete=models.CASCADE,)
    event_date = models.DateTimeField()
    game_description = models.CharField(max_length=500, default='', blank=True)
    score = models.IntegerField()
    away_team = models.CharField(max_length=100)
    home_team = models.CharField(max_length=100)
    completed = models.BooleanField(default=True)

    class Meta:
        ordering = ('name', )


# Model of a basketball player
class Player(models.Model):
    TEAM_CHOICES = (("ATL", "Atlanta Hawks",), ("BOS", "Boston Celtics",), ("BKN", "Brooklyn Nets",), ("CHA", "Charlotte Bobcats",), ("CHI", "Chicago Bulls",), ("CLE", "Cleveland Cavaliers",), ("DAL", "Dallas Mavericks",), ("DEN", "Denver Nuggets",), ("DET", "Detroit Pistons",), ("GSW", "Golden State Warriors",), ("HOU", "Houston Rockets",), ("IND", "Indiana Pacers",), ("LAC", "LA Clippers",), ("LAL", "LA Lakers",), ("MEM", "Memphis Grizzlies",), ("MIA", "Miami Heat",), ("MIL", "Milwaukee Bucks",), ("MIN", "Minnesota Timberwolves",), ("NO", "New Orleans Hornets",), ("NYK", "New York Knicks",), ("OKC", "Oklahoma City Thunder",), ("ORL", "Orlando Magic",), ("PHI", "Philadelphia Sixers",), ("PHO", "Phoenix Suns",), ("POR", "Portland Trail Blazers",), ("SAC", "Sacramento Kings",), ("SAS", "San Antonio Spurs",), ("TOR", "Toronto Raptors",), ("UTA", "Utah Jazz",), ("WAS", "Washington Wizards"))
    team = models.CharField(max_length=200, choices=TEAM_CHOICES, default="ATL")
    name = models.CharField(max_length=200)
    drafted_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name


class PlayerScores(models.Model):
    player_fk = models.ForeignKey(Player, related_name='scores', on_delete=models.CASCADE,)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, )
    points = models.IntegerField(default=0,)
    rebounds = models.IntegerField(default=0,)
    assists = models.IntegerField(default=0,)
    blocks = models.IntegerField(default=0,)
    steals = models.IntegerField(default=0,)
    date_of_game = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-points', )



