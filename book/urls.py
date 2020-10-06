# from django.conf.urls import url
from django.urls import path,include

from . import views
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'booksmini', views.BookViewMiniSet)
router.register(r'books', views.BookViewSet)


urlpatterns = [
    # path('', views.Home.as_view(), name="Home"),
    path('', include(router.urls))
    
]