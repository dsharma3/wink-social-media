from django.db import models

# Create your models here.
class UserFeed(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    feed_text = models.TextField()

class Like(models.Model):
    feed =  models.ForeignKey(UserFeed, on_delete=models.CASCADE)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)

class Comment(models.Model):
    feed =  models.ForeignKey(UserFeed, on_delete=models.CASCADE)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    comment = models.TextField()
    replied_comment = models.ForeignKey("self",related_name="replies",on_delete=models.CASCADE, blank=True, null=True)

class Friend(models.Model):
    user = models.ForeignKey(UserFeed, related_name="requesteduser",on_delete=models.CASCADE)
    friend = models.ForeignKey(UserFeed, related_name="requestinguser", on_delete=models.CASCADE)

class FriendRequest(models.Model):
    requesting_user =  models.ForeignKey("auth.User",related_name="requesteduser", on_delete=models.CASCADE)
    requested_user = models.ForeignKey("auth.User", related_name="requestinguser",on_delete=models.CASCADE)