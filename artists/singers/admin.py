from django.contrib import admin

from .models import Singer, Song, Album
# Register your models here.


admin.site.register(Singer)
admin.site.register(Song)
admin.site.register(Album)