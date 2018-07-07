from django.db import models
from utils.main import disable_for_loaddata


class FaceToFace(models.Model):
    name = models.CharField(max_length=128,default='name')
    phone_number = models.CharField(max_length=12,default='number')
    place = models.CharField(max_length=128,default='place')

    def __str__(self):
        return "Подписчик %s %s" % (self.name, self.phone_number)

    class Meta:
        verbose_name = 'Subscriber of FaceToFace'
        verbose_name_plural = 'Subscribers of FaceToFace'

class Group(models.Model):
    name = models.CharField(max_length=128,default='name')
    phone_number = models.CharField(max_length=12,default='number')
    level = models.CharField(max_length=128,default='level')

    def __str__(self):
        return "Подписчик %s %s" % (self.name, self.phone_number)

    class Meta:
        verbose_name = 'Subscriber of Group'
        verbose_name_plural = 'Subscribers of Group'




