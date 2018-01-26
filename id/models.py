from django.db import models

# Create your models here.
class Provinces(models.Model):
    '''省ID号'''
    provinceid = models.CharField(max_length=50)
    province = models.CharField(max_length=50)

    def __str__(self):
        return self.province

class Cities(models.Model):
    '''市ID号'''
    cityid = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    provinceid = models.CharField(max_length=50)

    def __str__(self):
        return self.city


class Areas(models.Model):
    '''区域ID号'''
    areaid = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    cityid = models.CharField(max_length=50)

    def __str__(self):
        return self.area

class Id_number(models.Model):
    '''身份证号'''
    id_numbers = models.CharField(max_length=18)

    def __str__(self):
        return self.id_numbers