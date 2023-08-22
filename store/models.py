from django.db import models
from django.db.models.signals import post_save
from datetime import datetime
from django.contrib.auth.models import User

from .signals import save_area_volume


class Box(models.Model):
    length = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    area = models.IntegerField(default=0)
    volume = models.IntegerField(default=0)
    created_by = models.ForeignKey(User,related_name="created_by",on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(default=datetime.now)


    def find_area(self):

        return 2*( (self.length * self.width) + (self.length * self.height) + (self.width * self.height) )

    def find_volume(self):

        return (self.length * self.width * self.height)
    
    def save(self, *args, **kwargs):
        self.area = self.find_area()
        self.volume = self.find_volume()
        self.last_updated = datetime.now()
        super(Box, self).save(*args, **kwargs)

post_save.connect(save_area_volume,sender=Box)


    




