from django.urls import path
from .views import member_create_view, member_login_view

urlpatterns = [
    path(
        "create/",
        member_create_view.create_member,
        name="create_member",
    ),
    path(
        "login/",
        member_login_view.login_member,
        name="login_member"
    )
]
