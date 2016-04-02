from django.db import models
from django.contrib.auth.models import User

class Scheme(models.Model):
	name=models.CharField(max_length=20,blank=True,null=True)
	content=models.CharField(max_length=10000,blank=True,null=True)
	number=models.IntegerField(primary_key=True)
	state=models.PositiveSmallIntegerField(default=1,blank=True,null=True)
	duration=models.IntegerField(blank=True,null=True)
	qualification=models.PositiveSmallIntegerField(blank=True,null=True)
	income_per_annum=models.PositiveSmallIntegerField(default=1,blank=True,null=True)
	caste=models.PositiveSmallIntegerField(default=1,blank=True,null=True)
	physically_handicapped=models.PositiveSmallIntegerField(default=1,blank=True,null=True)
	gender=models.PositiveSmallIntegerField(default=1,blank=True,null=True)
	age=models.CharField(max_length=50,blank=True,null=True)
	occupation=models.PositiveSmallIntegerField(default=1,blank=True,null=True)
	categories=models.CharField(max_length=100,blank=True,null=True)
	def __unicode__(self):
		return self.name