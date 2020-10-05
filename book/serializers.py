from rest_framework import serializers
from .models import BookSelf

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = BookSelf
        fields = ['id','title','description','price','publication_name']