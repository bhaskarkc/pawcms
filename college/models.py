from django.db import models


class Application(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone_no = models.CharField(max_length=255)
    email = models.EmailField()
    details = models.TextField()
    photo = models.ImageField()
    attachment = models.FileField()

    def __str__(self):
        return self.name
