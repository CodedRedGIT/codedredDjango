from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="member", null=True, blank=True)
    time_created = models.DateTimeField(default=timezone.now)
    display_name = models.CharField(max_length=256)
    access_level = models.IntegerField(default=0)
    # Todo add Patreon id?

    def __str__(self):
        return "{} ({})".format(self.display_name, self.user.id)


class Article(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    publisher = models.ForeignKey(Member, on_delete=models.DO_NOTHING)
    level = models.IntegerField(default=1)
