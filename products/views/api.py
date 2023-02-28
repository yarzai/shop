from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from products.serializers.test import TestSerializer


@api_view(["GET"])
def products(request):
    return Response({"message": "Welcome to Django rest framework"})


class Products(APIView):
    pass


@api_view(["POST"])
def test(request):
    print(request.data)
    ser = TestSerializer(data=request.data)
    if ser.is_valid():
        return Response(ser.validated_data)
    else:
        return Response(ser.errors)
