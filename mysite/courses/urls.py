from django.urls import path
from .views import BaseView, ProductDetailView,create,ProductUpdateView,ProductDeleteView,SearchResultsView
urlpatterns = [
    path("",BaseView.as_view(),name = 'home'),
    path('course/<str:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path("create/",create, name = "create_new_product"),
    path('<str:slug>/update',ProductUpdateView.as_view(),name = 'product-update'),
    path('<str:slug>/delete',ProductDeleteView.as_view(),name = 'product-delete'),
    path('search/', SearchResultsView.as_view(), name='search_results')
]

