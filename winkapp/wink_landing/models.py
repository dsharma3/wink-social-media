from django.db import models

# Create your models here.
class UserFeed(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    feed_text = models.TextField()
    createddate=models.DateTimeField()

class Like(models.Model):
    feed =  models.ForeignKey(UserFeed, on_delete=models.CASCADE)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    createddate=models.DateTimeField()

class Comment(models.Model):
    feed =  models.ForeignKey(UserFeed,related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    comment = models.TextField()
    replied_comment = models.ForeignKey("self",related_name="replies",on_delete=models.CASCADE, blank=True, null=True)
    createddate=models.DateTimeField()

class Friend(models.Model):
    user = models.ForeignKey(UserFeed, related_name="requesteduser",on_delete=models.CASCADE)
    friend = models.ForeignKey(UserFeed, related_name="requestinguser", on_delete=models.CASCADE)
    createddate=models.DateTimeField()

class FriendRequest(models.Model):
    requesting_user =  models.ForeignKey("auth.User",related_name="requesteduser", on_delete=models.CASCADE)
    requested_user = models.ForeignKey("auth.User", related_name="requestinguser",on_delete=models.CASCADE)
    createddate=models.DateTimeField()
