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

class Advocate(models.Model):
    aname=models.TextField()
    aphone=models.TextField()
    aemail=models.TextField()
    apassword=models.TextField()
    aaddress=models.TextField()
    aprofile=models.FileField(null=True)
    agender=models.TextField(null=True)
    bcr_no=models.TextField(null=True)
    aheighest_qual=models.TextField(null=True)
    start_time=models.TimeField(null=True)
    end_time=models.TimeField(null=True)
    off_day=models.TextField(null=True)
    idproof=models.FileField(null=True)
    bc_certificate=models.FileField(null=True)
    exp_certificate=models.FileField(null=True)

    def __str__(self):
        return self.aname

class Langauges(models.Model):
    language=models.TextField(null=True)

    def __str__(self):
        return self.language
class Selected_lang(models.Model):
    aname=models.ForeignKey(Advocate,on_delete=models.CASCADE)
    alang=models.ForeignKey(Langauges,on_delete=models.CASCADE)
    def __str__(self) :
        return self.aname.aname


class Practice_areas(models.Model):
    p_area=models.TextField(null=True)

    def __str__(self) :
        return self.p_area

class Selected_parea(models.Model):
    p_area_name=models.ForeignKey(Practice_areas,on_delete=models.CASCADE)
    aname=models.ForeignKey(Advocate,on_delete=models.CASCADE)

    def __str__(self) :
        return self.aname.aname
    



