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
    aname=models.ForeignKey(Advocate,on_delete=models.CASCADE)
    malayalam=models.BooleanField(default=False)
    english=models.BooleanField(default=False)
    hindi=models.BooleanField(default=False)

    def __str__(self):
        return self.aname.aname

class Practice_areas(models.Model):
    # aname=models.ForeignKey(Advocate,on_delete=models.CASCADE)
    # criminal_law=models.BooleanField(default=False)
    # civil_right_law=models.BooleanField(default=False)
    # family_law=models.BooleanField(default=False)
    # corporate_law=models.BooleanField(default=False)
    # intelectual_property_law=models.BooleanField(default=False)
    # employment_law=models.BooleanField(default=False)
    # personal_injury_law=models.BooleanField(default=False)
    # real_estate_law=models.BooleanField(default=False)
    # estate_planing_and_probate_law=models.BooleanField(default=False)
    # environmental_law=models.BooleanField(default=False)
    # bankruptcy_law=models.BooleanField(default=False)
    # immigration_law=models.BooleanField(default=False)
    # healthcare_law=models.BooleanField(default=False)   
    # tax_law=models.BooleanField(default=False)
    # admiralty_and_maritime_law=models.BooleanField(default=False)
    # entertainment_law=models.BooleanField(default=False)
    p_areas=models.ManyToManyField(Advocate,blank=False)


    



