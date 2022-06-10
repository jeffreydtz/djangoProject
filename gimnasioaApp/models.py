from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    UserAge = models.IntegerField()
    UserWeight = models.FloatField()
    UserHeight = models.FloatField()
    UserGender = models.CharField(max_length=1)


class Excercise(models.Model):
    ExcerciseId = models.AutoField(primary_key=True)
    ExcerciseName = models.CharField(max_length=50)
    ExcercisePhoto = models.ImageField()
    ExcerciseDescription = models.TextField()
    ExcerciseMuscle = models.CharField(max_length=50)


class Routine(models.Model):
    RoutineId = models.AutoField(primary_key=True)
    RoutineName = models.CharField(max_length=50)
    RoutineExcercises = models.ManyToManyField(Excercise)


class History(models.Model):
    HistoryUserId = models.ForeignKey(User, on_delete=models.CASCADE)
    HistoryRoutineId = models.ForeignKey(Routine, on_delete=models.CASCADE)
    HistoryWeight = models.FloatField()
    HistoryDate = models.DateField()
