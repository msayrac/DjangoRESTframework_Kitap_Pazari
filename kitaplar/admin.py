from django.contrib import admin
from kitaplar.models import Kitap, Yorum

# Register your models here.

class KitapAdmin(admin.ModelAdmin):
    list_display = ('isim','yazar','yaratilma_tarihi','yayin_tarih')
    list_filter = ('isim','yazar','yaratilma_tarihi','yayin_tarih')
    search_fields = ('isim','yazar','yaratilma_tarihi','yayin_tarih')


class YorumAdmin(admin.ModelAdmin):
    list_display = ('kitap','yorum_sahibi','yaratilma_tarihi','degerlendirme')
    list_filter = ('kitap','yorum_sahibi','yaratilma_tarihi','degerlendirme')
    search_fields = ('kitap','yorum_sahibi','yaratilma_tarihi','degerlendirme')


admin.site.register(Kitap, KitapAdmin)
admin.site.register(Yorum, YorumAdmin)