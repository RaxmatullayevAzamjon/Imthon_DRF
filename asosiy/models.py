from django.db import models
from django.contrib.auth.models import User


class Suv(models.Model):
    brend = models.CharField(max_length=30)
    narx = models.CharField(max_length=30)
    litr = models.CharField(max_length=20)
    batafsil = models.CharField(max_length=30, blank=True,null=True)

    def __str__(self):
        return self.brend


class Mijoz(models.Model):
    ism = models.CharField(max_length=20)
    tel = models.CharField(max_length=20)
    manzil = models.CharField(max_length=30, null=True, blank=True)
    qarz = models.CharField(max_length=30, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ism



class Admin(models.Model):
    ism = models.CharField(max_length=20)
    yosh = models.CharField(max_length=20)
    ish_vaqt = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.ism


class Haydovchi(models.Model):
    ism = models.CharField(max_length=20)
    tel = models.CharField(max_length=20)
    Kiritilgan_sana = models.DateField()

    def __str__(self):
        return self.ism


class Buyurtma(models.Model):
    suv = models.ForeignKey(Suv, on_delete=models.CASCADE)
    sana = models.DateField()
    mijoz = models.ForeignKey(Mijoz, on_delete=models.CASCADE)
    miqdori = models.CharField(max_length=30)
    umumiy_narx = models.CharField(max_length=30)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    haydovchi = models.ForeignKey(Haydovchi, on_delete=models.CASCADE)
