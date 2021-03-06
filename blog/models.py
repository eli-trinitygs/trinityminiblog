from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

#definir objeto Post
class Post(models.Model):
    #definir propiedades
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    #metodo
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

