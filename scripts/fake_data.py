import os
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE','core.settings')

import django
django.setup()
# Modellerimize ve django içeriklerine erişmek için yukarıdaki gibi ayarlamaları yapmamız gerekiyor.
# Sıralama çok önemli
from django.contrib.auth.models import User
from faker import Faker

def set_user():
    fake = Faker(['en_US'])
    f_name = fake.first_name()
    l_name = fake.last_name()
    u_name = f'{f_name.lower()}_{l_name.lower()}'
    email = f'{u_name}@{fake.domain_name()}'
    print(f_name, l_name, email)

    user_check = User.objects.filter(username=u_name)
    while user_check.exists():
        u_name = u_name +str(random.rand(1,99))
        user_check = User.objects.filter(username=u_name)

    user = User(
        username = u_name,
        first_name = f_name,
        last_name = l_name,
        email =  email,
        is_staff =fake.boolean(chance_of_getting_true=50),
    )

    user.set_password('Admin1234.')
    user.save()
    print('Kullanıcı kaydedildi', u_name)


import requests
from pprint import pprint
from kitaplar.api.serializers import KitapSerializer

def kitap_ekle(konu):
    fake = Faker(['en_US'])
    url = 'https://openlibrary.org/dev/docs/api/search.json'
    payload = {'q':konu}
    response = requests.get(url, params=payload)

    if response.status_code != 200:
        print('Hatalı istek yapıldı', response.status_code)
        return
    jsn = response.json()
    kitaplar = jsn.get('docs', [])

    if not kitaplar:
        print(f'{konu} konusuyla ilgili kitap bulunamadı.')
        return
    i=0
    for kitap in kitaplar:
        kitap_adi = kitap.get('title')
        yazar_listesi = kitap.get('author_name')
        yazar_ismi = yazar_listesi[0] if yazar_listesi else 'Bilinmeyen Yazar'
        data =dict(
            isim = kitap_adi,
            yazar = yazar_ismi,
            aciklama ='-'.join(kitap.get('text')),
            yayin_tarihi = fake.date_time_between(start_date='-10y', end_date='now', tzinfo=None),
        )
        serializer = KitapSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print('kitap kaydedildi : ', kitap_adi)

        else:
            continue
        
        
