from turtle import Turtle
import json
from datetime import datetime

scores = "./highscores.json" # A json for all of the scores

class Scoreboard(Turtle):
    """The Scoreboard Object using the Turtle Module"""
    def __init__(self, lives):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.lives = lives
        self.score = 0

        self.highscores = self.load_hisghscore()
        self.update_scoreboard()


    def load_hisghscore(self):
        """The function to load our highscore.json"""
        try:
            with open(scores, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return [] # Returns our empty list
        
    
    def save_highscore(self):
        """Save a highscore to a json file"""
        with open(scores, "w") as f:
            json.dump(self.highscores, f)


    def update_high_scores(self):
        """The function to place a new entry into the .json file"""
        score_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Gets the current date and time and formats it nicely
        self.highscores.append({"Score": self.score, "date": score_date})
        self.highscores.sort(key=lambda x: x["Score"], reverse=True) # Sorts it in descending order!
        self.save_highscore()


    def give_points(self):
        """A simple function to give points upon breakling a brick"""
        self.score += 1


    def update_scoreboard(self):
        """The function to update the scoreboard based on each score of points"""
        self.clear()
        self.goto(-250, 270)
        if not self.highscores:
            self.write(f"Score: {self.score} | Highscore: None", align="left", font=("Courier", 20, "normal")) # Incase the file is lost or doesnt exist
        else:
            self.write(f"Score: {self.score} | Highscore: {self.highscores[0]["Score"]}", align="left", font=("Courier", 20, "normal")) # Normal text
        self.goto(-250, 240)
        self.write(f"Lives: {self.lives}", align="left", font=("Courier", 15, "normal"))