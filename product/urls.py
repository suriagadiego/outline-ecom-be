from django.urls import path
from .views import product_detail_view, product_create_view, product_update_view, product_delete_view, product_list_view

urlpatterns = [
    path(
        "list/",
        product_list_view.list_all_products,
        name="product_list_view"
    ),
    path(
        "<uuid:product_uuid>/",
        product_detail_view.get_product_by_uuid,
        name="product_detail_view",
    ),
    path(
        "id/<int:product_id>/",
        product_detail_view.get_product_by_id,
        name="product_detail_view_id",
    ),
    path(
        "create/",
        product_create_view.create_product,
        name="create_product",
    ),
    path(
        "update/<uuid:product_uuid>/",
        product_update_view.update_product,
        name="update_product"
    ),
    path(
        "delete/<uuid:product_uuid>/",
        product_delete_view.delete_product,
        name="delete_product"
    )
]
# path('part/<int:pk>/', rest_part_no.part_no_detail_view,  name='part_no-detail'),
# path('part/create/', rest_part_no.part_no_create_view, name='part_no_create'),
# path('part/update/<int:pk>/', rest_part_no.part_no_update_view, name='part_no_update'),
# path('part/search/', rest_part_no.part_no_search_view, name='part_no_search'),
# path('part/batch_delete/', rest_part_no.part_delete_apiview, name='part_no_delete'),
# path('part/bulk/create/', rest_part_no.bulk_create_parts , name='part_bulk_create'),
