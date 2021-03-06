from django.db import models
from datetime import datetime

# Create your models here.

class Artist(models.Model):
	"""
	Table for Artist
	"""
	GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
	name = models.CharField(max_length=72)
	dob = models.DateField()
	gender =  models.CharField(max_length=1, choices=GENDER_CHOICES)

	def __str__(self):
		"""
		String representation for the class on DB
		"""
		return self.name


class Award(models.Model):
	name = models.CharField(max_length=40)
	date = models.DateField()

	def __str__(self):
		"""
		String representation for the class on DB
		"""
		return self.name



class Movie(models.Model):
	"""
	Table for Movies to be entered
	MTM relation to Artist and awards
	"""
	name = models.CharField(max_length=80)
	genre = models.CharField(max_length=80)
	release_date = models.DateField(max_length=80)
	avg_rating = models.DecimalField(max_digits=4, decimal_places=2)
	language = models.CharField(max_length=20)
	artist = models.ManyToManyField(Artist)
	duration = models.DecimalField(max_digits=3, decimal_places=2)
	award = models.ManyToManyField(Award)


	def __str__(self):
		"""
		String representation for the class on DB
		"""
		return self.name

	# def rating_avg(self):
	# 	return self.R


class Rating(models.Model):
	"""
	Model to save movie and Its ratings
	"""

	RATINGS =[('0','0'),
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
    ('7','7'),
    ('8','8'),
    ('9','9'),
    ('10','10')
    ]
	movie_rating = models.CharField(max_length=20,choices=RATINGS,default='0')
	movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
	votes = models.IntegerField(default='0')
	def __str__(self):
		return self.movie.name + str(self.movie_rating) 