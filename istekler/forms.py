from django import forms
from django.forms import ModelForm
from .models import Istek, Hastane



# Create a venue form
class HastaneForm(ModelForm):
	class Meta:
		model = Hastane
		fields = ('name', 
            'address', 
            'zip_code', 
            'phone', 
            'web', 
            'email_address')
		labels = {
			'name': '',
			'address': '',
			'zip_code': '',
			'phone': '',
			'web': '',
			'email_address': '',		
		}
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hastane Adı'}),
			'address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Adres'}),
			'zip_code': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zip Kodu'}),
			'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Telefon'}),
			'web': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Web Adresi'}),
			'email_address': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
		}



class IstekForm(ModelForm):
	class Meta:
		model = Istek
		fields = ('tibbi_malzeme_ilac_asi', 
            'kisisel_gereksinimler', 
            'hastane_adi',
            'hastanenin_altyapi_gereksinimleri_sorunlari', 
            'hastanede_saglik_calisani_gereksinimi', 
            'temel_gereksinimler',
            'ailevi_gereksinimler', 
            'diger_gereksinimler', 
            'mesaj_kutusu')
		labels = {
			'tibbi_malzeme_ilac_asi': '',
			'kisisel_gereksinimler':  '',
			'hastane_adi': '',
			'hastanenin_altyapi_gereksinimleri_sorunlari': '',
			'hastanede_saglik_calisani_gereksinimi': '',
			'temel_gereksinimler': '',
			'ailevi_gereksinimler': '',			
			'diger_gereksinimler': '',			
			'mesaj_kutusu': '',			
		}
		widgets = {
			'tibbi_malzeme_ilac_asi': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tıbbi malzeme / İlaç / Aşı'}),
			'kisisel_gereksinimler':  forms.TextInput(attrs={'class':'form-control', 'placeholder':'Kişisel Gereksinimler'}),
			'hastane_adi':  forms.Select(attrs={'class':'form-select', 'placeholder':'Hastane'}),
			'hastanenin_altyapi_gereksinimleri_sorunlari': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hastanenin Altyapı Gereksinimleri / Sorunları'}),
			'hastanede_saglik_calisani_gereksinimi': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hastanede Sağlık Çalışanı Gereksinimi'}),
			'temel_gereksinimler': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Temel Gereksinimler'}),
			'ailevi_gereksinimler': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ailevi Gereksinimler'}),			
			'diger_gereksinimler': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Diğer Gereksinimler'}),		
			'mesaj_kutusu': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Mesaj Kutusu'}),		
		}
