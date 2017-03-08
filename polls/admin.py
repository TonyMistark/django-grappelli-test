from django.contrib import admin

from polls import models


class GameAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ("id", "name", "code", "coef")

admin.site.register(models.Game, GameAdmin)

