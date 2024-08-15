from django.urls import path
from . import views

app_name = "licores"
urlpatterns = [
    path("", views.index, name="index"),
    
    path('login/', views.CustomLoginView.as_view(), name='login'),
    
    path("customer", views.customer, name="customer"),
    path("customer/<int:customer_id>/", views.info_customer, name="info_customer"),
    path("add_customer/", views.add_customer, name="add_customer"),
    path("edit_customer/<int:id>/", views.edit_customer, name="edit_customer"),
    path("delete_customer/<int:id>/", views.delete_customer, name="delete_customer"),
    
    path("category", views.category, name="category"),
    path("category/<int:category_id>/", views.info_category, name="info_category"),
    path("add_category/", views.add_category, name="add_category"),
    path("edit_category/<int:id>/", views.edit_category, name="edit_category"),
    path("delete_category/<int:id>/", views.delete_category, name="delete_category"),
    
    path("product", views.product, name="product"),
    path("product/<int:product_id>/", views.info_product, name="info_product"),
    path("add_product/", views.add_product, name="add_product"),
    path("edit_product/<int:id>/", views.edit_product, name="edit_product"),
    path("delete_product/<int:id>/", views.delete_product, name="delete_product"),
    path('add_saleproduct/<int:product_id>/', views.add_saleproduct, name='add_saleproduct'),
    
    path("sale", views.sale, name="sale"),
    path("sale/<int:sale_id>/", views.info_sale, name="info_sale"),
    path("add_sale/", views.add_sale, name="add_sale"),
]