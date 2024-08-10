from django.urls import path
from . import views

app_name = "licores"
urlpatterns = [
    path("", views.index, name="index"),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path("sale", views.sale, name="sale"),
    path("sale/<int:sale_id>/", views.sale, name="display_sale"),
    path("add_sale/", views.add_sale, name="add_sale"),
    path("edit_sale/<int:id>/", views.edit_sale, name="edit_sale"),
    path("delete_sale/<int:id>/", views.delete_sale, name="delete_sale"),
]