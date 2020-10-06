from django.shortcuts import render
from django.views import View
from rest_framework import viewsets
from .serializers import BookSerializers, BookMiniSerializer, BookAuthorSerializer
from .models import BookSelf, Author
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Create your views here.
# class Home(View):

#     def get(self,  request):
#         return render(request, 'home.html', {"title":"Home"})


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializers
    queryset = BookSelf.objects.all()
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = BookSerializers(instance)
        return Response(serializer.data)

class BookViewMiniSet(viewsets.ModelViewSet):
    serializer_class = BookMiniSerializer
    queryset = BookSelf.objects.all()
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = BookMiniSerializer(instance)
        return Response(serializer.data)

# class AuthorSet(viewsets.ModelViewSet):
#     serializer_class = Author
#     queryset = Author.objects.all()
#     authentication_classes = (TokenAuthentication,)

#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = BookAuthorSerializer(instance)
#         return Response(serializer.data)