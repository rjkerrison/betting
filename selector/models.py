from django.db import models

class Line(models.Model):
  line_description = models.CharField(max_length=200)
  odds_numerator = models.IntegerField(default = 1)
  odds_denominator = models.IntegerField(default = 1)

class Bet(models.Model):
  line = models.ForeignKey(Line, on_delete=models.CASCADE)
  stake = models.FloatField(default=0.0)
