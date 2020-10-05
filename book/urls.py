# from django.conf.urls import url
from django.urls import path,include

from . import views
from rest_framework import routers
from .views import BookViewSet

router = routers.DefaultRouter()
router.register('books', BookViewSet)

urlpatterns = [
    # path('', views.Home.as_view(), name="Home"),
    path('', include(router.urls))
]