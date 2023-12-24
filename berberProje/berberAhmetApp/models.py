from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser

# Create your models here.


class AppUser(AbstractUser):
    username = models.CharField(max_length=40, unique=True, blank=False, null=False)
    password = models.CharField(max_length=100,verbose_name="Şifre",  blank=False , null=False)
    first_name=models.CharField(("İsim"), max_length=50,  blank=False , null=False)
    last_name=models.CharField(("Soyisim"), max_length=50,  blank=False , null=False)
    avatar = models.FileField(("User Avatar"), upload_to="uploads", null=True, blank=True)
    tel = PhoneNumberField(null=True, region="TR",  blank=False)

    def __str__(self):
        return self.username    
    
class Hours(models.Model):
    saatler = models.CharField(("Saatler"), max_length=10)
    dolu_mu = models.BooleanField(("Dolu mu?"), default=False)

    def __str__(self):
        return self.saatler

class Days(models.Model):
    günler = models.CharField(("Günler"), max_length=10)

    def __str__(self):
        return self.günler
class haftaTatil(models.Model):
    gün = models.ForeignKey(Days, verbose_name=("Tatil günü"), on_delete=models.CASCADE, null=True, blank=True)

class Tatil(models.Model):
    tatil = models.DateField(("Tatil"), auto_now=False, auto_now_add=False,null=True, unique=True)
    
class Count(models.Model):
    counts = models.IntegerField(("Count"))
    
class RandevuSaatleri(models.Model):
    rs_sayi = models.ForeignKey(Count, verbose_name=("Count"), on_delete=models.CASCADE, null=True)
    rs_saat = models.ManyToManyField(Hours, verbose_name=("Saat"))

    
    
    
    
class Hizmetler(models.Model):
    avatar = models.FileField(("Hizmet Avatar"), upload_to="uploads", null=True, blank=True)
    hizmet = models.CharField(("Hizmet"), max_length=20)
    fiyat = models.CharField(("Fiyat"), max_length=10)
    createdAt = models.DateTimeField(auto_now=True, null=True)

 
   

    def __str__(self):
        return str(self.hizmet)    
    
class Randevu(models.Model):
    Müsteri = models.ForeignKey(AppUser, verbose_name=("Müşteri"), on_delete=models.CASCADE, null=True)
    Tarih = models.DateTimeField(verbose_name=("Tarih"), null=True)
    createdAt = models.DateTimeField(auto_now=True, null=True)
    hizmet = models.ForeignKey(Hizmetler, verbose_name=("Hizmet"), on_delete=models.CASCADE, null=True)
    description = models.CharField(("Açıklama"),blank=True, null=True, max_length=30,default=" ")
 
   

    def __str__(self):
        return str(self.Müsteri)      
    
class iptalInfo(models.Model):
    user = models.ForeignKey(AppUser, verbose_name=("User"), on_delete=models.CASCADE) 
    Tarih = models.DateTimeField(verbose_name=("Tarih"), null=True)
   