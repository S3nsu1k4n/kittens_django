from django.db import models
from django.urls import reverse

# Create your models here.

class Kitten(models.Model):
    '''
    Representing a kitten

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

    created_at = models.DateTimeField(auto_now_add=True, help_text='When the entry was created')
    updated_at = models.DateTimeField(auto_now=True, help_text='When the entry was last updated')

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('kitten-detail', args=[str(self.id)])
    