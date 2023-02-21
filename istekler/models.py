from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.

class Hastane(models.Model):
	name = models.CharField('Hastane Adı', max_length=120)
	address = models.CharField(max_length=300)
	zip_code = models.CharField('Zip Kodu', max_length=15)
	phone = models.CharField('Telefon', max_length=25, blank=True)
	web = models.URLField('Website', blank=True)
	email_address = models.EmailField('Email Adresi', blank=True)
	owner = models.IntegerField("Venue Owner", blank=False, default=1)
	venue_image = models.ImageField(null=True, blank=True, upload_to="images/")
	
	def __str__(self):
		return self.name

class Istek(models.Model):
	tibbi_malzeme_ilac_asi = models.CharField('Tibbi Malzeme / Ilac / Asi', max_length=120)
	kisisel_gereksinimler = models.CharField('Event Date',  max_length=120)
	#venue = models.CharField(max_length=120)
	kullanici_adi = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
	hastane_adi = models.ForeignKey(Hastane, blank=True, null=True, on_delete=models.CASCADE)
	hastanenin_altyapi_gereksinimleri_sorunlari = models.TextField(blank=True)
	hastanede_saglik_calisani_gereksinimi = models.TextField(blank=True)
	temel_gereksinimler = models.TextField(blank=True)
	ailevi_gereksinimler = models.TextField(blank=True)
	diger_gereksinimler = models.TextField(blank=True)
	mesaj_kutusu = models.TextField(blank=True)
	approved = models.BooleanField('Aprroved', default=False)

	def __str__(self):
		return self.tibbi_malzeme_ilac_asi



# ===============================================================
#   ? Bunun bizimle bir alakasi var mi ?
# ===============================================================

# class MyClubUser(models.Model):
# 	first_name = models.CharField(max_length=30)
# 	last_name = models.CharField(max_length=30)
# 	email = models.EmailField('User Email')

# 	def __str__(self):
# 		return self.first_name + ' ' + self.last_name

# ===============================================================