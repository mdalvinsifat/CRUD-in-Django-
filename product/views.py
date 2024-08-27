
from rest_framework import generics
from .serializers import ProductSerializers
from .models import ProductModel 
# Create your views here.
class ProductListView(generics.ListCreateAPIView):
    queryset = ProductModel.objects.all( )
    serializer_class = ProductSerializers

class ProductDetelisView (generics.RetrieveUpdateDestroyAPIView):
       queryset = ProductModel.objects.all( )
       serializer_class = ProductSerializers
