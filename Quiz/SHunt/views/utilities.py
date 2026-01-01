from django.shortcuts import render, HttpResponse
from django.core import exceptions
from ..models import ScavengerHunt, Teams, Players, Score, Evidence, Items

"""Check if the person exists"""
def playerExists(PlayerId):
    returnVal = None
    # First check if the player exists
    try:
        players = Players.objects.filter(identifier = PlayerId)
    except:
        returnVal = False
    else:
        numPlayers = len(players)
        if numPlayers > 0:
            returnVal = True
        else:
            returnVal = False
    finally:
        return returnVal

"""Check if the ScavengerHunt exists"""
def scavengerHuntExists(ScavengerHuntId):
    returnVal = None
    try:
        scavengerHunts = ScavengerHunt.objects.filter(identifier = ScavengerHuntId)
    except:
        returnVal = False
    else:
        numScavengerHunts = len(scavengerHunts)
        if numScavengerHunts > 0:
            returnVal = True
        else:
            returnVal = False
    finally:
        return returnVal
        