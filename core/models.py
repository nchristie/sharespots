from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models




class Venue(models.Model):
    RATING_CHOICES = [(x, str(x)) for x in range(1, 6)]

    name = models.CharField(max_length=150)
    featured = models.BooleanField(default=False)
    address_1 = models.CharField(max_length=150)
    address_2 = models.CharField(max_length=150)
    post_code = models.CharField(max_length=10)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    wifi = models.IntegerField(choices=RATING_CHOICES)
    food = models.IntegerField(choices=RATING_CHOICES)
    atmosphere = models.IntegerField(choices=RATING_CHOICES)
    sockets = models.IntegerField(choices=RATING_CHOICES)
    coffee = models.IntegerField(choices=RATING_CHOICES)
    
    slogan = models.CharField(max_length=250, null=True)


    def __str__(self):
        return '{0} - created at: {1}'.format(self.name, self.created_at)
