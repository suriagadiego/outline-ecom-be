from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..models import Product
from ..serializers import (
    ProductSerializer,
)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_product_by_uuid(request, product_uuid):
    product = get_object_or_404(Product, uuid=product_uuid)
    result = ProductSerializer(product, many=False).data
    return Response({"data": result})

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_product_by_id(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    result = ProductSerializer(product, many=False).data
    return Response({"data": result})
