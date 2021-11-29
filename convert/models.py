from django.db import models


class number(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class words(models.Model):
    number = models.ForeignKey(number, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=124)
    number = models.ForeignKey(number, on_delete=models.SET_NULL, blank=True, null=True)
    words = models.ForeignKey(words, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name
