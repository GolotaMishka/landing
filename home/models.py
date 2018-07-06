from django.db import models
from utils.main import disable_for_loaddata


class Subscriber(models.Model):
    name = models.CharField(max_length=128,default='name',blank=False , null=True)
    phone_number = models.CharField(max_length=12,default='number',blank=False , null=True)
    level = models.CharField(max_length=128,default='level',blank=False , null=True)
    place = models.CharField(max_length=128,default='place',blank=False , null=True)

    def __str__(self):
        return "Подписчик %s %s" % (self.name, self.phone_number)

    class Meta:
        verbose_name = 'MySubscriber'
        verbose_name_plural = 'A lot of Subscribers'



