import sys
sys.path.append(f'/Users/nathanburns/Projects/Sports-Text')
sys.path.append(f'/Users/nathanburns/Projects/Sports-Text/Dodgers')

import requests
import datetime
from twilio.rest import Client
import keys

from dodgersAfternoonModel import DodgersAfternoonModel
from dodgersAfternoonText import dodgersAfternoonText
from MLBTeams import MLBTeams

currentDate = datetime.date.today().strftime('%Y-%m-%d')

espnUrl = "http://site.api.espn.com/apis/site/v2/sports/baseball/mlb/teams/" + str(MLBTeams.LosAngelesDodgers.value)
espn = requests.get(espnUrl)
espnData = espn.json()

message = ""

client = Client(keys.account_sid, keys.auth_token)

if espn.status_code == 200:
    try:
        awayTeam = espnData["team"]["nextEvent"][0]["competitions"][0]["competitors"][1]["team"]["displayName"]
        homeTeam = espnData["team"]["nextEvent"][0]["competitions"][0]["competitors"][0]["team"]["displayName"]
        if (awayTeam == "Los Angeles Dodgers"):
            otherTeam = homeTeam
            otherTeamID = espnData["team"]["nextEvent"][0]["competitions"][0]["competitors"][0]["id"]
        else:
            otherTeam = awayTeam
            otherTeamID = espnData["team"]["nextEvent"][0]["competitions"][0]["competitors"][1]["id"]

        dodgersRecord = espnData["team"]["record"]["items"][0]["summary"]

        try:
            awayPitcher = espnData["team"]["nextEvent"][0]["competitions"][0]["competitors"][1]["probables"][0]["athlete"]["displayName"]
            awayPitcherWins = espnData["team"]["nextEvent"][0]["competitions"][0]["competitors"][1]["probables"][0]["statistics"][0]["stats"][25]["displayValue"]
            awayPitcherLosses = espnData["team"]["nextEvent"][0]["competitions"][0]["competitors"][1]["probables"][0]["statistics"][0]["stats"][6]["displayValue"]
            awayPitcherERA = espnData["team"]["nextEvent"][0]["competitions"][0]["competitors"][1]["probables"][0]["statistics"][0]["stats"][52]["displayValue"]
        except:
            awayPitcher = "TBD"
            awayPitcherWins = "0"
            awayPitcherLosses = "0"
            awayPitcherERA = "0"

        try:
            homePitcher = espnData["team"]["nextEvent"][0]["competitions"][0]["competitors"][0]["probables"][0]["athlete"]["displayName"]
            homePitcherWins = espnData["team"]["nextEvent"][0]["competitions"][0]["competitors"][0]["probables"][0]["statistics"][0]["stats"][25]["displayValue"]
            homePitcherLosses = espnData["team"]["nextEvent"][0]["competitions"][0]["competitors"][0]["probables"][0]["statistics"][0]["stats"][6]["displayValue"]
            homePitcherERA = espnData["team"]["nextEvent"][0]["competitions"][0]["competitors"][0]["probables"][0]["statistics"][0]["stats"][52]["displayValue"]
        except:
            homePitcher = "TBD"
            homePitcherWins = "0"
            homePitcherLosses = "0"
            homePitcherERA = "0"


        fullTime = espnData["team"]["nextEvent"][0]["competitions"][0]["status"]["type"]["shortDetail"].split()
        time = fullTime[2] + " " + fullTime[3]
        
        # make api call to get other team's record
        OpponentEspnUrl = "http://site.api.espn.com/apis/site/v2/sports/baseball/mlb/teams/" + otherTeamID
        OpponentEspn = requests.get(espnUrl)
        OpponentEspnData = espn.json()
        otherTeamRecord = OpponentEspnData["team"]["record"]["items"][0]["summary"]

        afternoonModel = DodgersAfternoonModel(homeTeam, otherTeam, dodgersRecord, otherTeamRecord, awayPitcher, homePitcher, awayPitcherWins, awayPitcherLosses, awayPitcherERA, homePitcherWins, homePitcherLosses, homePitcherERA, time)
        afternoonText = dodgersAfternoonText(afternoonModel)
        message = afternoonText.AfternoonText()
        print(afternoonText.message)
  
    except:
        afternoonText = dodgersAfternoonText()
        message = afternoonText.AfternoonTextNoGame()
        print(afternoonText.message)

message = client.messages.create(
    body=message,
    to=keys.target_number,
    from_=keys.twilio_number,
)

print(message.body)
