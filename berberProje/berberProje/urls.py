from django.contrib import admin
from django.urls import path
from berberAhmetApp.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="home"),
    path("giris", login, name="login"),
    path("twilio", twilio, name="twilio"),
    path("404", error, name="404"),
    path("tatil", tatil, name="tatil"),
    path("kayıt", register, name="register"),
    path("cikis", log_out, name="log_out"),    
    path("allrandevu", allrandevu, name="allrandevu"),    
    path("haftalıkTatil/<gunId>", haftalıkTatil, name="haftalıkTatil"),    
    path("iptalRandevu/<randevuId>", iptalRandevu, name="iptalRandevu"), 
    path("tatilIptal/<tatilId>", tatilIptal, name="tatilIptal"), 
    path("profil/<userId>", profil, name="profil"),     
    path("randevu/<count>/<clock>", randevu, name="randevu"),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)