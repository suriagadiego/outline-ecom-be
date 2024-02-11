from django.db import models
from django.utils import timezone
import uuid


class Image(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    image_url = models.CharField(null=False, blank=False, unique=True)
    title = models.CharField(blank=True, null=True)


class Product(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    product_name = models.CharField(
        null=False, blank=False, unique=True, default="PRODUCT_NAME"
    )
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField(blank=False, default=0, null=False)
    image_url = models.ForeignKey(
        "Image",
        to_field="image_url",
        db_column="image_url",
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
    )
    updated_at = models.DateTimeField(blank=False, default=timezone.now, null=False)
    created_at = models.DateTimeField(
        blank=False, default=timezone.now, null=False, editable=False
    )
