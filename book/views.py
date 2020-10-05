from django.shortcuts import render
from django.views import View
from rest_framework import viewsets
from .serializers import BookSerializers
from .models import BookSelf
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.
# class Home(View):

#     def get(self,  request):
#         return render(request, 'home.html', {"title":"Home"})


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializers
    queryset = BookSelf.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)