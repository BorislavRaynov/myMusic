from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.

class Album(models.Model):
    CHOISES = (
        ("Pop Music", "Pop Music"),
        ("Jazz Music", "Jazz Music"),
        ("R&B Music", "R&B Music"),
        ("Rock Music", "Rock Music"),
        ("Country Music", "Country Music"),
        ("Dance Music", "Dance Music"),
        ("Hip Hop Music", "Hip Hop Music"),
        ("Other", "Other")
    )


    name = models.CharField(max_length=30, unique=True)
    artist = models.CharField(max_length=30)
    genre = models.CharField(max_length=30, choices=CHOISES)
    description = models.TextField(blank=False, null=False)
    image = models.URLField()
    price = models.FloatField(validators=[MinValueValidator(0.0)])
