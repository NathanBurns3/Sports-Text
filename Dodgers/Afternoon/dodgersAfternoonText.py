class dodgersAfternoonText:
    message = "\n"

    def __init__(self, dodgersAfternoonModel=None):
        self.dodgersAfternoonModel = dodgersAfternoonModel

    def AfternoonText(self):
        if self.dodgersAfternoonModel is None:
            return ""
        
        self.message += "The Dodgers (" + self.dodgersAfternoonModel.dodgersRecord + ") play the " + self.dodgersAfternoonModel.otherTeam + " (" + self.dodgersAfternoonModel.otherTeamRecord + ") today at " + self.dodgersAfternoonModel.time
        
        if self.dodgersAfternoonModel.homeTeam == "Los Angeles Dodgers":
            self.message += " at home\n\n"
            self.message += self.dodgersAfternoonModel.homePitcher + " (" + self.dodgersAfternoonModel.homePitcherWins + " - " + self.dodgersAfternoonModel.homePitcherLosses + " | " + self.dodgersAfternoonModel.homePitcherERA + ") is pitching for the Dodgers\n\n"
            self.message += self.dodgersAfternoonModel.awayPitcher + " (" + self.dodgersAfternoonModel.awayPitcherWins + " - " + self.dodgersAfternoonModel.awayPitcherLosses + " | " + self.dodgersAfternoonModel.awayPitcherERA + ") is pitching for the " + self.dodgersAfternoonModel.otherTeam + "\n\n"
        else:
            self.message += " away\n\n"
            self.message += self.dodgersAfternoonModel.awayPitcher + " (" + self.dodgersAfternoonModel.awayPitcherWins + " - " + self.dodgersAfternoonModel.awayPitcherLosses + " | " + self.dodgersAfternoonModel.awayPitcherERA + ") is pitching for the Dodgers\n\n"
            self.message += self.dodgersAfternoonModel.homePitcher + " (" + self.dodgersAfternoonModel.homePitcherWins + " - " + self.dodgersAfternoonModel.homePitcherLosses + " | " + self.dodgersAfternoonModel.homePitcherERA + ") is pitching for the " + self.dodgersAfternoonModel.otherTeam + "\n\n"
        
        return self.message
    
    def AfternoonTextNoGame(self):
        self.message = "\nThe Dodgers do not play today" + "\n\n"
        return self.message