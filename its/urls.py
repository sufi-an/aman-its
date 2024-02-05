from django.contrib import admin
from django.urls import path, re_path, include
from django.urls import reverse_lazy
from rest_framework.routers import DefaultRouter
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import Route, DynamicRoute, SimpleRouter

router = DefaultRouter()
router.register(r'v1/auth-token', auth_token_list_view)

urlpatterns = [

    path('', include(router.urls)),
    # path('', include(custom_router.urls))

    # routes
    # path('v1/get-next-leaf/', views.get_leatest_leaft_by_book, name='get_leatest_leaft_by_book'),
    # path('v1/bulk-update-checque-leaf/', views.bulk_update_checque_leaf, name='bulk_update_checque_leaf'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)