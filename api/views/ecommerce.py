from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ecommerce.models import Product
from api.serializers.ecommerce import ProductSerializer

class ProductListView(APIView):
    def get (self,request):
        product= Product.objects.all()
        serializer = ProductSerializer(product,many=True)
        return Response(serializer.data)

