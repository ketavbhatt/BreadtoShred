# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings



# Create your models here.

class Food(models.Model):
	name = models.CharField(max_length=100)
	calorie = models.CharField(max_length=100)
	

	def __str__(self):
		return self.name



class Exercise(models.Model):
	name = models.CharField(max_length=100)
	calorie = models.CharField(max_length=100)


	def __str__(self):
		return self.name

class user_calorie(models.Model):

	user = models.ForeignKey(User)
	food_cal = models.IntegerField()
	exe_cal = models.IntegerField()
	rem_cal = models.IntegerField()
	goal_cal = models.IntegerField()

	

