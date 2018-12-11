from django.db import models
from django.contrib.auth.models import User
import numpy as np


class Bourbon(models.Model):

    BourbonID = models.CharField(max_length=200)
    Bourbon = models.CharField(max_length=200)
    Aged = models.IntegerField()
    Proof = models.IntegerField()
    Corn = models.IntegerField()
    Rye = models.IntegerField()
    Barley = models.IntegerField()
    Wheat = models.IntegerField()
    Type = models.CharField(max_length=200)
    Style = models.CharField(max_length=200)
    Price_Range = models.IntegerField()
    Distillery = models.CharField(max_length=200)
    Location = models.CharField(max_length=200)
    Website = models.URLField()
    Description = models.CharField(max_length=2000)

    def average_rating(self):
        all_ratings = list(map(lambda x: x.Rating, self.review_set.all()))
        return np.mean(all_ratings)

    def __unicode__(self):
        return self.Bourbon


class Review(models.Model):

    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    RatingID = models.IntegerField(null=True, blank=True)
    Bourbon = models.ForeignKey(Bourbon)
    Pub_Date = models.DateTimeField('date published')
    User_Name = models.CharField(max_length=100)
    Comment = models.CharField(max_length=200)
    Rating = models.IntegerField(choices=RATING_CHOICES)


class SimilarBourbons(models.Model):

    BourbonID = models.CharField(max_length=200)
    Bourbon = models.CharField(max_length=200)


class SimilarReviews(models.Model):

    BourbonID = models.CharField(max_length=200)
    Bourbon = models.CharField(max_length=200)
    AvgRating = models.DecimalField(null=True, blank=True, max_digits=200, decimal_places=2)
    PredRating = models.DecimalField(null=True, blank=True, max_digits=200, decimal_places=2)