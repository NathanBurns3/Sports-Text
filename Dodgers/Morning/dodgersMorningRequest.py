import sys
sys.path.append(f'/home/nathan-burns/Projects/Sports-Text')
sys.path.append(f'/home/nathan-burns/Projects/Sports-Text/Dodgers')
sys.path.append(f'/Users/nathanburns/Projects/Sports-Text')
sys.path.append(f'/Users/nathanburns/Projects/Sports-Text/Dodgers')

import requests
import datetime
from twilio.rest import Client
import keys

from dodgersMorningModel import DodgersMorningModel
from dodgersMorningText import dodgersMorningText
from MLBTeams import MLBTeams

currentDate = datetime.date.today().strftime('%Y-%m-%d')
yesterdayDate = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')

espnUrl = "http://site.api.espn.com/apis/site/v2/sports/baseball/mlb/teams/" + str(MLBTeams.LosAngelesDodgers.value)
espn = requests.get(espnUrl)
espnData = espn.json()

message = ""

client = Client(keys.account_sid, keys.auth_token)

if espn.status_code == 200:
    try:
        comparisonDate = (espnData["team"]["nextEvent"][0]["date"]).split("T")[0]
        if (currentDate != yesterdayDate):
            raise Exception("different date")

        awayTeam = espnData["team"]["nextEvent"][0]["competitions"][0]["competitors"][1]["team"]["displayName"]
        homeTeam = espnData["team"]["nextEvent"][0]["competitions"][0]["competitors"][0]["team"]["displayName"]
        if (awayTeam == "Los Angeles Dodgers"):
            win = espnData["team"]["nextEvent"][0]["competitions"][0]["competitors"][1]["winner"]
            dodgersScore = espnData["team"]["nextEvent"][0]["competitions"][0]["competitors"][1]["score"]["displayValue"]
            oponentScore = espnData["team"]["nextEvent"][0]["competitions"][0]["competitors"][0]["score"]["displayValue"]
        else:
            win = espnData["team"]["nextEvent"][0]["competitions"][0]["competitors"][0]["winner"]
            dodgersScore = espnData["team"]["nextEvent"][0]["competitions"][0]["competitors"][0]["score"]["displayValue"]
            oponentScore = espnData["team"]["nextEvent"][0]["competitions"][0]["competitors"][1]["score"]["displayValue"]
        boxScoreLink = espnData["team"]["nextEvent"][0]["links"][4]["href"]
        place = espnData["team"]["standingSummary"]
        record = espnData["team"]["record"]["items"][0]["summary"]
        
        morningModel = DodgersMorningModel(awayTeam, homeTeam, win, dodgersScore, oponentScore, boxScoreLink, place, record)
        morningText = dodgersMorningText(morningModel)
        message = morningText.MorningText()
        print(morningText.message)
    except:
        morningText = dodgersMorningText()
        message = morningText.MorningTextNoGame()
        print(morningText.message)


message = client.messages.create(
    body=message,
    to=keys.target_number,
    from_=keys.twilio_number,
)

print(message.body)