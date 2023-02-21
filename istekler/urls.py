from django.urls import path
from . import views

urlpatterns = [
	# Path Converters
	# int: numbers
	# str: strings
	# path: whole urls /
	# slug: hyphen-and_underscores_stuff
	# UUID: universally unique identifier

    path('', views.home, name="home"),
	path('<int:year>/<str:month>/', views.home, name="home"),
	path('istek_ekle', views.istek_ekle, name='istek-ekle'),
	path('hastane_ekle', views.hastane_ekle, name='hastane-ekle'),
    # path('show_istek', views.show_istek, name='show-istek'),
    path('show_istek/<istek_id>', views.show_istek, name='show-istek'),
    path('HastaneIstekleri/<hastane_id>', views.HastaneIstekleri, name='HastaneIstekleri'),
    path('isteklerim', views.isteklerim, name='isteklerim'),
    path('istek_ekle', views.istek_ekle, name='istek-ekle'),
    path('istek_guncelle/<istek_id>', views.istek_guncelle, name='istek-guncelle'),
    # path('hastane_guncelle', views.hastane_guncelle, name='hastane-guncelle'),
    path('hastane_guncelle/<hastane_id>', views.hastane_guncelle, name='hastane-guncelle'),
    path('hastane_ara', views.hastane_ara, name='hastane-ara'),
    path('istek_ara', views.istek_ara, name='istek-ara'),
    path('show_hastane', views.show_hastane, name='show-hastane'),
    path('list_hastane', views.list_hastane, name='list-hastane'),
    path('hastane_ekle', views.hastane_ekle, name='hastane-ekle'),
    path('butun_istekler', views.butun_istekler, name='butun-istekler'),

	# path('hastane_text', views.hastane_text, name='hastane_text'),
	# path('hastane_csv', views.hastane_csv, name='hastane_csv'),
	# path('hastane_pdf', views.hastane_pdf, name='hastane_pdf'),

]