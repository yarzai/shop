from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from products.models import Product
from rest_framework.viewsets import ModelViewSet
from products.serializers.products_serializers import TestSerializer, ProductListSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import status


@api_view(["GET", 'POST'])
def products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serilizer = ProductListSerializer(products, many=True)
        print(serilizer.data)
        return Response(serilizer.data, status=status.HTTP_404_NOT_FOUND)
    elif request.method == "POST":
        serilizer = ProductListSerializer(data=request.data)
        if serilizer.is_valid():
            res = serilizer.save()
            return Response(ProductListSerializer(res).data)
        else:
            return Response(serilizer.errors)


class Products(APIView):
    def get(self, request):
        products = Product.objects.all()
        serilizer = ProductListSerializer(products, many=True)
        print(serilizer.data)
        return Response(serilizer.data)

    def post(self, request):
        serilizer = ProductListSerializer(data=request.data)
        if serilizer.is_valid():
            res = serilizer.save()
            return Response(ProductListSerializer(res).data)
        else:
            return Response(serilizer.errors)


@api_view(["POST"])
def test(request):
    print(request.data)
    ser = TestSerializer(data=request.data)
    if ser.is_valid():
        return Response(ser.validated_data)
    else:
        return Response(ser.errors)


class ProductModalViewSet(ModelViewSet):
    queryset = Product.objects.filter(price__gt=4000)
    serializer_class = ProductListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
