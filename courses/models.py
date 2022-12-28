from django.db import models
'from languages.fields import LanguageField'
from django.contrib.auth.models import User

# Create your models here.

class course(models.Model):
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=50)
    author = models.ForeignKey(User,related_name='author',on_delete=models.CASCADE)
    'language = LanguageField()'
    price= models.DecimalField(max_digits=10, decimal_places=2)
    introduction = models.TextField(max_length=100)
    whatUWillLearn = models.TextField(max_length=500)
    requierments = models.TextField(max_length=500)
    description = models.TextField(max_length=10000)
    reviews = models.TextField(max_length=500)
    image =models.ImageField(upload_to='Media/',default='default.png')
    date =models.DateField()

