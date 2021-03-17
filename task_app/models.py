from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Organisation(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'tbl_organisation'


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    org = models.ForeignKey(Organisation, on_delete=models.DO_NOTHING)
    mobile_number = models.CharField(max_length=13)
    address = models.TextField()
    add_longitude = models.CharField(max_length=25)
    add_latitude = models.CharField(max_length=25)

    class Meta:
        db_table = 'tbl_user_profile'


class Task(models.Model):

    org = models.ForeignKey(Organisation, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)
    assigned_to = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING, related_name="assigned_to")
    assigned_by = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING, related_name="assigned_by")
    status = models.IntegerField(default=1)


    class Meta:
        db_table = 'tbl_task'
