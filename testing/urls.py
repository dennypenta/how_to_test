from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers

from app import views as app_views

router = routers.DefaultRouter()
router.register(r'products', app_views.ProductViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

urlpatterns = router.urls
