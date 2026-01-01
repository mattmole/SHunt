from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail
from django.conf import settings
import uuid

def generateUuid():
    return uuid.uuid4()

class ScavengerHunt(models.Model):
    scavengerHuntName = models.CharField(max_length=200, verbose_name="Scavenger hunt name", help_text="Enter a name for the ScavengerHunt")
    scavengerHuntDateAndTime = models.DateTimeField(verbose_name="Date and time", help_text="Enter when the ScavengerHunt will take place")
    identifier = models.UUIDField(default = generateUuid, editable = False, verbose_name="Unique identifier used for the Scavenger Hunt", help_text="The identier used, essentially, as a password", unique=True)

    def __str__(self):
        return self.scavengerHuntName

    class Meta:
        verbose_name="Scavenger Hunt"
        verbose_name_plural = "Scavenger Hunts"

class Teams(models.Model):
    scavengerHunt = models.ForeignKey(ScavengerHunt, on_delete=models.CASCADE, verbose_name="ScavengerHunt", help_text="Select which ScavengerHunt should the team be registered to")
    teamName = models.CharField(max_length=200, verbose_name="Team name", help_text="Enter a name for the team")
    identifier = models.UUIDField(editable = False, verbose_name="Unique identifier used for the team", help_text="The identier used, essentially, as a password")
    
    def __str__(self):
        return self.teamName

    class Meta:
        verbose_name="Team"
        verbose_name_plural = "Teams"

    def save(self, *args, **kwargs):

        if not self.id:
            self.identifier = generateUuid()
       
        return super(Teams, self).save(*args, **kwargs)

class Players(models.Model):
    team = models.ForeignKey(Teams, on_delete=models.CASCADE, verbose_name="Team", help_text="Select which team the player should be registered to")
    playerName = models.CharField(max_length=200, verbose_name="Player Name", help_text="The player's name")
    identifier = models.UUIDField(editable = False, verbose_name="Unique identifier used for the player", help_text="The identier used, essentially, as a password", unique=True)
    emailAddress = models.EmailField(max_length=100, verbose_name="Email address", help_text="Enter the player's email address", blank=True)
    emailAddressChanged = models.BooleanField(default=False, editable=False)
    emailSent = models.BooleanField(default=False, editable=False)
    def __str__(self):
        return self.playerName

    class Meta:
        verbose_name="Player"
        verbose_name_plural = "Players"

    def save(self, *args, **kwargs):

        if not self.id:
            self.identifier = generateUuid()
       
        return super(Players, self).save(*args, **kwargs)

class Items(models.Model):
    scavengerHunt = models.ForeignKey(ScavengerHunt, on_delete=models.CASCADE, verbose_name="ScavengerHunt", help_text="Select which ScavengerHunt this item should be added to")
    itemName = models.CharField(max_length=200, verbose_name="Item name", help_text="Enter an item")
    identifier = models.UUIDField(editable = False, verbose_name="Unique identifier used for the item", help_text="The identier used", unique=True)

    def __str__(self):
        return self.itemName

    class Meta:
        verbose_name="Item"
        verbose_name_plural = "Items"

    def save(self, *args, **kwargs):

        if not self.id:
            self.identifier = generateUuid()
       
        return super(Items, self).save(*args, **kwargs)

class Evidence(models.Model):

    item = models.ForeignKey(Items, on_delete=models.CASCADE, verbose_name="Item", help_text="Select which item the evidence is linked to")
    player = models.ForeignKey(Players, on_delete=models.CASCADE, verbose_name="Player", help_text="Select the player")
    team = models.ForeignKey(Teams, on_delete=models.CASCADE, verbose_name="Team", help_text="Select the team")
    image = models.ImageField(upload_to="SHunt/static/uploads" ,max_length=100, verbose_name="Image", help_text="Select a file to upload")

    imageShrunk  = ImageSpecField(source='image',
                                      processors=[Thumbnail(width=300)],
                                      format='JPEG',
                                      options={'quality': 60})

    imageThumbnail  = ImageSpecField(source='image',
                                      processors=[Thumbnail(width=150)],
                                      format='JPEG',
                                      options={'quality': 60})

    def __str__(self):
        return f"{self.item.itemName}-{self.player.playerName}-{self.image}"

    class Meta:
        verbose_name="Evidence"
        verbose_name_plural = "Evidence"

class Score(models.Model):
    item = models.ForeignKey(Items, on_delete=models.CASCADE, verbose_name="ScavengerHunt", help_text="Select which ScavengerHunt the score is linked to")
    player = models.ForeignKey(Players, on_delete=models.CASCADE, verbose_name="Player", help_text="Select the player", null=True)
    score = models.IntegerField(default=0, verbose_name="Score", help_text="Enter the score")

    def __str__(self):
        return f"{self.item.itemName}-{self.player.playerName}-{self.score}"

    class Meta:
        verbose_name="Score"
        verbose_name_plural = "Scores"