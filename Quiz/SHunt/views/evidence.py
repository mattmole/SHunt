from django.shortcuts import render, HttpResponse
from SHunt.models import ScavengerHunt, Teams, Players, Score, Evidence, Items
from SHunt.views import utilities

# Create your views here.
def uploadEvidence(request,ScavengerHuntId, PlayerId):

    # First check if the player and scavenger hunts exist
    playerExists = utilities.playerExists(PlayerId)
    scavengerHuntExists = utilities.scavengerHuntExists(ScavengerHuntId)

    # Carry on, but only if both exist. If they don't render an error page
    errorMessage = None
    if not playerExists and not scavengerHuntExists:
        errorMessage = "The player and scavenger hunt do not exist"
    if playerExists and not scavengerHuntExists:
        errorMessage = "The scavenger hunt does not exist, but the player does exist"
    if not playerExists and scavengerHuntExists:
        errorMessage = "The player does not exist, but the scavenger hunt does exist"

    if errorMessage != None:
        return render(request, "error.html", {"errorMessage": errorMessage})
    else:
        print("Carrying on...")

    print(scavengerHuntExists, playerExists)

    print(f"{ScavengerHuntId} {PlayerId}")