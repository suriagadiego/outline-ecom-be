from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from ..models import Product
from ..serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def list_all_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response({"data": serializer.data})
