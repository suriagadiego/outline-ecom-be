from django.urls import path
from .views import product_detail_view

urlpatterns = [
    path(
        "/<uuid:product_uuid>/",
        product_detail_view.get_product_by_uuid,
        name="product_detail_view",
    ),
]
# path('part/<int:pk>/', rest_part_no.part_no_detail_view,  name='part_no-detail'),
# path('part/create/', rest_part_no.part_no_create_view, name='part_no_create'),
# path('part/update/<int:pk>/', rest_part_no.part_no_update_view, name='part_no_update'),
# path('part/search/', rest_part_no.part_no_search_view, name='part_no_search'),
# path('part/batch_delete/', rest_part_no.part_delete_apiview, name='part_no_delete'),
# path('part/bulk/create/', rest_part_no.bulk_create_parts , name='part_bulk_create'),
