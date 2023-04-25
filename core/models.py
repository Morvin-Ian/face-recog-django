from django.db import models

class Screenshot(models.Model):
    image = models.ImageField(upload_to="screenshots")


    