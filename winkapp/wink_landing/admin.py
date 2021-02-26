from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.UserFeed)
admin.site.register(models.Like)
admin.site.register(models.Comment)
admin.site.register(models.Friend)
admin.site.register(models.FriendRequest)


