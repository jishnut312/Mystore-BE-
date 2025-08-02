from django.urls import path
from .views import (
    create_checkout_session,
    save_user_address,
    has_saved_address,
    get_user_address
)

urlpatterns = [
    path('create-checkout-session/', create_checkout_session, name='create_checkout_session'),
    path('user/address/', get_user_address, name='get_user_address'),
    path('user/save-address/', save_user_address, name='save_user_address'),
    path('user/has-address/', has_saved_address, name='has_saved_address'),]
