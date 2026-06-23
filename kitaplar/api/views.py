from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework import permissions

from kitaplar.api.permissions import IsAdminUserOrReadOnly
from kitaplar.api.serializers import KitapSerializer, YorumSerializer
from kitaplar.models import Kitap, Yorum

# Concrete view
class KitapListCreateAPIView(generics.ListCreateAPIView):
    queryset = Kitap.objects.all()
    serializer_class = KitapSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class KitapDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kitap.objects.all()
    serializer_class = KitapSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class YorumCreateAPIView(generics.CreateAPIView):
    queryset = Yorum.objects.all()
    serializer_class = YorumSerializer
    permission_classes = [IsAdminUserOrReadOnly]


    def perform_create(self, serializer):
        kitap_pk = self.kwargs.get('kitap_pk')
        kitap = get_object_or_404(Kitap, pk=kitap_pk)
        serializer.save(kitap=kitap)

class YorumDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Yorum.objects.all()
    serializer_class = YorumSerializer
    permission_classes = [IsAdminUserOrReadOnly]









# # GenericAPIView
# class KitapListCreateAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
#     queryset = Kitap.objects.all()
#     serializer_class = KitapSerializer

#     # Listelemek
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)        

#     #Yaratabilmek
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)











