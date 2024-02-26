from django.db import models

# Create your models here.

class Kitten(models.Model):
    '''
    Kitten Model

    Attributes
    ----------
    - name : CharField
    - age : IntegerField
    - cuteness : IntegerField
    - softness : IntegerField
    '''
    name = models.CharField('Name', max_length=32, help_text='Name of the kitten')
    age = models.IntegerField('Age', help_text='Age of the kitten')
    cuteness = models.IntegerField('Cuteness', help_text='Cuteness of the kitten')
    softness = models.IntegerField('Softness', help_text='Softness of the kitten')