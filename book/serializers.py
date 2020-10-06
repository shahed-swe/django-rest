from rest_framework import serializers
from .models import BookSelf,BookNumber,Character,Author

class BookNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookNumber
        fields = '__all__'

class BookCharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'

class BookAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializers(serializers.ModelSerializer):
    number = BookNumberSerializer(many=False)
    characters = BookCharacterSerializer(many=True)
    author = BookAuthorSerializer(many=True)

    class Meta:
        model = BookSelf
        fields = ['id','title','description','price','publication_name','number','characters','author']


class BookMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookSelf
        fields = ['id','title']