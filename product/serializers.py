from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "uuid",
            "product_name",
            "description",
            "price",
            "image_url",
            "created_at",
            "updated_at",
        )
