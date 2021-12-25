from django.db import models

class DataMqtt(models.Model):
    topic = models.CharField(max_length=100)
    payload = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)
    qos = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id}'

class DataImage(models.Model):
    image = models.ImageField()
    accuracy = models.DecimalField(max_digits=3, decimal_places=2,default=0)
    disease_name = models.CharField(max_length=20,null=True,blank=True)