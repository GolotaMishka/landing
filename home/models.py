from django.db import models
from utils.main import disable_for_loaddata


class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128,default='name')
    phone_number = models.CharField(max_length=12,default='number')
    level = models.CharField(max_length=128,default='level')

    def __str__(self):
        return "Подписчик %s %s" % (self.name, self.email,)

    class Meta:
        verbose_name = 'MySubscriber'
        verbose_name_plural = 'A lot of Subscribers'



