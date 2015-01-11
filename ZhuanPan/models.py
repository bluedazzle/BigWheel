from django.db import models

# Create your models here.
class Reward(models.Model):
    phone = models.CharField(max_length=15)
    content = models.CharField(max_length=50, blank=True, null=True)
    time = models.DateTimeField(max_length=30)
    if_exchange = models.BooleanField(default=True)
    fail_message = models.TextField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.phone

class Consume(models.Model):
    c_id = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    consume_time = models.DateTimeField(max_length=25)
    total = models.FloatField(max_length=10)
    if_play = models.BooleanField(default=False)

    def __unicode__(self):
        return self.phone