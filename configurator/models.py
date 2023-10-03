from django.db import models


class ButtonBody(models.Model):
    code = models.CharField(max_length=5)
    body = models.CharField(max_length=50)

    def __str__(self):
        return self.body


class PresselType(models.Model):
    code = models.CharField(max_length=5)
    pressel = models.CharField(max_length=50)

    def __str__(self):
        return self.pressel
