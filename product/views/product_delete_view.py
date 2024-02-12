from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from ..models import Product
from ..serializers import (
    ProductSerializer,
)

def custom_permission_classes(permissions):
    def decorator(view_func):
        def wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                # If the user is not authenticated, return a custom error response
                return Response({"error": True, "detail": "Authentication credentials were not provided."}, status=401)
            elif not request.user.is_superuser:
                # If the user is not an admin user, return a custom error response
                return Response({"error": True, "detail": "You do not have permission to perform this action."}, status=403)
            return view_func(request, *args, **kwargs)
        return wrapped_view
    return decorator





@api_view(["DELETE"])
@custom_permission_classes([IsAuthenticated, IsAdminUser])
def delete_product(request, product_uuid):
    product = Product.objects.filter(uuid=product_uuid).first()
    
    if product is None:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        product.delete()
        return Response({"message": "Product deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
