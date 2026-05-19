from django.db import models

# Create your models here.
class Movies(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    release_year = models.IntegerField()
    genre = models.CharField(max_length=50)
    sinopsis = models.TextField()
    picture = models.ImageField(upload_to="movies_pictures/", null=True, blank=True)


    def __str__(self):
        return self.title
    
    