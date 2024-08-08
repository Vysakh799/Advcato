from django.db import models

# Create your models here.
class User(models.Model):
    uname=models.TextField()
    uphone=models.IntegerField()
    uemail=models.TextField()
    uaddress=models.TextField()
    upassword=models.TextField()

    def __str__(self):
        return self.uname
