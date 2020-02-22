from django.db import models
import graphene

# Create your models here.
class UserModel(models.Model):
    first_name =  models.CharField(max_length=100)
    last_name =  models.CharField(max_length=100)


class Breaks(models.Model):
    number_of_breaks = models.IntegerField()
    break_type = models.CharField(max_length=5,choices = [('short', 'SHORT'), ('long', 'LONG')])

class Session(models.Model):
    name = models.CharField(max_length=100)
    completed = models.BooleanField()
    owner =  models.ForeignKey(UserModel, on_delete=models.PROTECT)
    break_id = models.ForeignKey(Breaks, on_delete=models.CASCADE)
