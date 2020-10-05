from django.shortcuts import render
from django.views import View
from rest_framework import viewsets
from .serializers import BookSerializers
from .models import BookSelf
# Create your views here.
# class Home(View):

#     def get(self,  request):
#         return render(request, 'home.html', {"title":"Home"})


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializers
    queryset = BookSelf.objects.all()
