from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
	adi = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
	soyadi = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
	dogum_tarihi = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
	diploma_tescil_no = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
	mezun_oldugu_universite = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
	mezuniyet_yili = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
	uzmanlik_dali = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
	calistigi_bolge_hastane = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
	gsm_no = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
	adres = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))


	class Meta:
		model = User
		fields = ('username', 'adi', 'soyadi', 'dogum_tarihi' ,'email', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(RegisterUserForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'
