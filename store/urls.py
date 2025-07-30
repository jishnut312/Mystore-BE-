from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('products/category/<slug:slug>/', ProductsByCategoryView.as_view(), name='products-by-category'),

]
