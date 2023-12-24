from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login, logout, authenticate
from .models import *
from .form import *
from django.contrib import messages
import datetime
from django.core.serializers import serialize
from django.core import serializers
from twilio.rest import Client
from django.utils import timezone
import os
from dotenv import load_dotenv



def twilio(request):
    load_dotenv()
    
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)
    
    telnolar = iptalInfo.objects.all()
    telnoTarih=iptalInfo.objects.first()
    tarih=telnoTarih.Tarih
    liste = []
    for i in telnolar:
        liste.append("+"+str(i.user.tel.country_code)+str(i.user.tel.national_number))
        i.delete() 
    for i in liste:
        print(liste)

        phone_number = i
        messages = client.messages.create(
        body = "{} tarihindeki randevunuz tatil nedeniyle iptal olmuştur. Lütfen yeni randevu oluşturun. Berber Ahmet".format(tarih),
        from_="+12058431980", 
        to=phone_number )
           
    return redirect("tatil")


def index(request):
    context = {}
    hours = RandevuSaatleri.objects.all()
    randevular = Randevu.objects.all()
    serialized_data = serialize('json', randevular, fields=('Müsteri', 'Tarih'))
    context["randevular"] = serialized_data
    
    tatiller = Tatil.objects.all()
    serialized_data1 = serialize('json', tatiller, fields=( 'tatil'))
    context["tatilveri"] = serialized_data1
    
    haftaTatilGun = haftaTatil.objects.first()
    haftaTatilGun1 = [haftaTatilGun]
    serialized_data2 = serializers.serialize("json", haftaTatilGun1, fields=("gün"))
    context["tatilGunu"] = serialized_data2
    
    
    context["hours"] = hours
    hizmetler = Hizmetler.objects.all()
    context["hizmetler"] = hizmetler

    simdiki_tarih = timezone.now()
    gecmisRandevular = Randevu.objects.filter(Tarih__lt=simdiki_tarih)
    gecmisRandevular.delete()
    
    gecmisTatiller = Tatil.objects.filter(tatil__lt=simdiki_tarih)
    gecmisTatiller.delete()
   
   
    return render(request, "index.html", context)  

def error(request):
    return render(request, "404.html")

def tatilIptal(request, tatilId):
    tatil = Tatil.objects.filter(id=tatilId).first()
    tatil.delete()
    return redirect("tatil")

def haftalıkTatil(request, gunId):
    if request.method == "POST":
        gun = haftaTatil.objects.filter(id = gunId).first()
        form = haftaTatilForm(request.POST, instance=gun)
        if form.is_valid():
            form.save()
            return redirect("tatil")

        

def tatil(request):
    context={}
    if not request.user.is_superuser:
        return redirect("404")
    
    if request.method=="POST":
        form=TatilForm(request.POST) 
        if form.is_valid():
            tatil_value = form.cleaned_data['tatil']
            iptalRandevu = Randevu.objects.filter(Tarih__date = tatil_value)
            if iptalRandevu:
                for r in iptalRandevu:
                    iptalInfo.objects.create(
                        user=r.Müsteri,
                        Tarih=r.Tarih
                    )
                    r.delete()
                form.save()
                return redirect("twilio")
            else:
                form.save()
                return redirect("tatil")
                
                
            
    else:
        haftaTatilGun = haftaTatil.objects.first()
        context["tatilGunu"] = haftaTatilGun
        context["form"] = TatilForm()
        tatiller = Tatil.objects.all().order_by("-tatil")
        context["tatiller"] = tatiller
        context["form1"] = haftaTatilForm(instance=haftaTatilGun)

        return render(request, "tatil.html", context)


def randevu(request, count, clock):
   if not request.user.is_authenticated:
        messages.add_message(request, messages.INFO, "Bu sayfaya erişemezsin")
        return redirect("404")
   if request.method == "POST":
        müsteri = request.POST.get("müsteri")
        user = AppUser.objects.filter(username=müsteri).first()
        is_randevu = Randevu.objects.filter(Müsteri=user)
        if not request.user.is_superuser:
             if is_randevu:
                return redirect("home")
        tarih = request.POST.get("tarih")     
        form = RandevuForm(request.POST)
        if form.is_valid:
            randevu_obj = form.save(commit=False)  # Veritabanına kaydetme işlemi için formu kullan, ancak commit etme
            randevu_obj.Müsteri = user
            randevu_obj.Tarih = tarih
            randevu_obj.save()  # Şimdi veritabanına kaydet
            messages.add_message(request, messages.INFO, "Randevunuz kaydedildi")

            return redirect("home")
        else:
            return redirect("login") 
   
   else:
      sayi = Count.objects.filter(counts=count).first()
      saat = Hours.objects.filter(saatler=clock).first()
      tarih = datetime.date.today() + datetime.timedelta(days=int(sayi.counts))
      xtam = str(tarih) + "T" + str(saat.saatler) + ":00.000"
      xyarim = str(tarih) + "T" + str(saat.saatler) + ":00.000"

      context = {
         "randevuSayi" : int(sayi.counts),
         "randevuSaat" : saat.saatler,
         "xtam" : xtam,
         "xyarim" : xyarim,

      }
      context["form"] = RandevuForm
   
   
      return render(request, "randevu.html", context)  
   

def login(request):
    if request.user.is_authenticated:
        return redirect("404")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username and password:
            user = authenticate(request, username = username ,password = password)
            if user:
                auth_login(request, user)

                return redirect("home")
            else:
                messages.add_message(request, messages.ERROR, "Böyle bir hesap bulunamadı")
                return redirect("login")
        else:
            messages.add_message(request, messages.ERROR, "Lütfen formu boş bırakmayın")

            return redirect("login")    
    else:    
        return render(request, "login.html")   

def register(request):
    context = {}
    if request.user.is_authenticated:
        return redirect("404")
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid:
            try:
                user = form.save(commit=False)
                username = form.cleaned_data["username"].lower()
                user.username=username
                user.set_password(form.cleaned_data["password"])

                user.save()
            except:
                messages.add_message(request, messages.ERROR, "Kullanıcı adını değiştirin veya numaranızı kontrol edin")
                return redirect("register")    
            return redirect("login")
        else:
            messages.add_message(request, messages.ERROR, "Kullanıcı adını değiştirin veya numaranızı kontrol edin")
            return redirect("register")

    else:
        context["form"] = RegisterForm
        return render(request, "register.html",context)
def log_out(request):
    if not request.user.is_authenticated:
        return redirect("404")    
    logout(request)
    messages.add_message(request, messages.INFO, "Hesaptan çıkış yapıldı")
    return redirect("home")


def profil(request, userId):
    if not request.user.is_authenticated:
        return redirect("404")    
    user = AppUser.objects.filter(id=userId).first()
    randevular = Randevu.objects.filter(Müsteri=user)
    context = {}
    
    if request.method == "POST":
        form = UpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "Hesap bilgileri güncellendi. Lütfen tekrar giriş yapınız")
            return redirect("login")
    else:
        form = UpdateForm(instance=user)

    context["form"] = form
    context["user"] = user
    context["randevular"] = randevular
    return render(request, "profil.html", context)

def allrandevu(request):
    if not request.user.is_superuser:
        return redirect("404")

    randevular = Randevu.objects.all().order_by('Tarih')
    context = {}
    context["randevular"] = randevular
    return render(request, "allrandevu.html",context)

def iptalRandevu(request, randevuId):

    randevu = Randevu.objects.filter(id = randevuId).first()
    if not request.user.is_authenticated:
        return redirect("404")        
    if request.user.id != randevu.Müsteri.id and request.user.is_superuser == False:
        return redirect("404")
    randevu.delete()
    referring_page = request.META.get('HTTP_REFERER')  # HTTP Referer başlığını al
    if referring_page:
        # Eğer HTTP Referer başlığı varsa, URL'yi parçalara ayırarak HTML dosyasının adını al
        referring_page_parts = referring_page.split('/')
        print(referring_page_parts)
        html_file_name = referring_page_parts[3] 
        """ html_file_name = html_file_name + ".html" """
    print(html_file_name)
    if html_file_name == "profil":
        return redirect(html_file_name, randevu.Müsteri.id)
    return redirect(html_file_name)
