from django.contrib import admin
from .models import ScavengerHunt, Teams, Players, Score, Evidence, Items
from django.utils.html import format_html
from imagekit.admin import AdminThumbnail

class TeamsInline(admin.TabularInline):
    model = Teams
    extra = 5
    fields = ["teamName", "identifier"]
    readonly_fields = ["identifier"]

class ItemsInline(admin.TabularInline):
    model = Items
    extra = 5
    fields = ["itemName"]

class PlayersInline(admin.TabularInline):
    model = Players
    extra = 3
    fields = ["playerName", "identifier"]
    readonly_fields = ["identifier"]

class ScavengerHuntAdmin(admin.ModelAdmin):
    list_display = ["scavengerHuntName", "scavengerHuntDateAndTime", "identifier"]
    inlines=[TeamsInline, ItemsInline]

class TeamsAdmin(admin.ModelAdmin):
    list_display = ["scavengerHunt", "teamName", "identifier"]
    inlines=[PlayersInline]

class PlayersAdmin(admin.ModelAdmin):
    list_display = ["team", "playerName", "identifier"]

class ScoreAdmin(admin.ModelAdmin):
    list_display = ["item", "player", "score"]

class EvidenceAdmin(admin.ModelAdmin):

    imageShrunk = AdminThumbnail(image_field="imageShrunk")
    imageShrunk.short_description = 'Image Preview'

    imageThumbnail = AdminThumbnail(image_field="imageThumbnail")
    imageThumbnail.short_description = 'Thumbnail'

    readonly_fields = ['imageShrunk']

    #fields = ['image_tag']
    #readonly_fields = ['image_tag']
    list_display = ["item", "player", "image", "imageThumbnail"]


class ItemsAdmin(admin.ModelAdmin):
    list_display = ["scavengerHunt", "itemName"]

# Register your models here.
admin.site.register(ScavengerHunt, ScavengerHuntAdmin)
admin.site.register(Teams, TeamsAdmin)
admin.site.register(Players, PlayersAdmin)
admin.site.register(Score, ScoreAdmin)
admin.site.register(Evidence, EvidenceAdmin)
#admin.site.register(Items, ItemsAdmin)