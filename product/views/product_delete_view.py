from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import Product
from ..serializers import (
    ProductSerializer,
)

@api_view(["DELETE"])
def delete_product(request, product_uuid):
    product = Product.objects.filter(uuid=product_uuid).first()
    
    if product is None:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        product.delete()
        return Response({"message": "Product deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
