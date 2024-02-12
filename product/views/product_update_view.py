from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from ..models import Product
from ..serializers import (
    ProductSerializer,
)

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_product(request, product_uuid):
    product = Product.objects.filter(uuid=product_uuid).first()
    
    if product is None:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
