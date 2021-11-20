from django.db import models

# Create your models here.
class Finch(models.Model):
  name = models.CharField(max_length=100, default='Dorkus')
  species = models.CharField(max_length=100, default='House Finch')
  description = models.TextField(max_length=250, default='a real stinker')

  def __str__(self):
      return self.name
  