from django.db import models


class Quote(models.Model):
    quote = models.TextField(null=True)
    character = models.IntegerField()
    consonant = models.IntegerField()
    vowel = models.IntegerField()
    average_lens = models.FloatField()
    longest_word = models.CharField(max_length=100)
    repeated_char = models.TextField()
    objects = models.Manager()


