class dodgersMorningText:
    message = "\n"

    def __init__(self, dodgersMorningModel=None):
        self.dodgersMorningModel = dodgersMorningModel
    
    def MorningText(self):

        if self.dodgersMorningModel is None:
            return ""
        
        if (self.dodgersMorningModel.awayTeam == "Los Angeles Dodgers"):
            self.message += "The Dodgers played the " + self.dodgersMorningModel.homeTeam + "\n\n"
        else:
            self.message += "The Dodgers played the " + self.dodgersMorningModel.awayTeam + "\n\n"
        
        if self.dodgersMorningModel.win:
            self.message += "They won "
        else:
            self.message += "They lost "

        self.message += str(self.dodgersMorningModel.dodgersScore) + " - " + str(self.dodgersMorningModel.opponentScore) + "\n\n"
        self.message += "Link to the box store: " + self.dodgersMorningModel.boxScoreLink + "\n\n"

        self.message += "The Dodgers are in " + self.dodgersMorningModel.place + " place in the NL West with a record of " + self.dodgersMorningModel.record + "\n\n"
        
        return self.message
    
    def MorningTextNoGame(self):
        self.message = "The Dodgers did not play yesterday"
        return self.message