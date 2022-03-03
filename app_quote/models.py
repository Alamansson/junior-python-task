from django.db import models
from picklefield.fields import PickledObjectField


class Quote(models.Model):
    quote = models.TextField(null=True)
    character = models.IntegerField(null=True, blank=True)
    consonant = models.IntegerField(null=True, blank=True)
    vowel = models.IntegerField(null=True, blank=True)
    average_lens = models.FloatField(null=True, blank=True)
    longest_word = models.CharField(max_length=100, null=True, blank=True)
    repeated_char = models.TextField(null=True, blank=True)
    objects = models.Manager()

