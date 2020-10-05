from rest_framework import serializers
from .models import BookSelf,BookNumber

class BookNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookNumber
        fields = '__all__'

class BookSerializers(serializers.ModelSerializer):
    number = BookNumberSerializer(many=False)
    
    class Meta:
        model = BookSelf
        fields = ['id','title','description','price','publication_name','number']