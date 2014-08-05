from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Bird(models.Model):

	FAMILY_CHOICES = (
		("waterbirds_and_nearshore_birds", "Waterbirds & Nearshore Birds"),
		("doves_woodpeckers_etc", "Doves, Woodpeckers, Etc."),
		("birds_of_prey", "Birds of Prey"),
		("perching_birds", "Perching Birds"),
	)

	family = models.CharField(max_length=35, choices=FAMILY_CHOICES, default="perching_birds")
	name = models.CharField(max_length=50)
	scientific_name = models.CharField(max_length=50)
	slug = models.CharField(max_length=50)
	size = models.CharField(max_length=50)
	info = models.TextField(blank=True, null=True)
	pic = models.ImageField(upload_to="media")
	thumb = models.ImageField(upload_to="media")

	def __str__(self):
		return self.name

class Sighting(models.Model):

	birder = models.ForeignKey(User)
	bird = models.ForeignKey(Bird)
	notes = models.TextField(blank=True, null=True)
	sighted = models.BooleanField()

	def __str__(self):
		return str(self.bird) + " sighted by " + str(self.birder.username)