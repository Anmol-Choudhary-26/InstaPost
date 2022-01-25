from .models import Ipost, InstagramUser
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = InstagramUser
        fields = ['id', 'username', 'E_mail', 'bio', 'likedpost']

class PostSerializer(serializers.ModelSerializer):
    Likedby = UserSerializer(many=True, read_only=False)
    Likedby = serializers.StringRelatedField(many=True, read_only=False)
    class Meta:
        model = Ipost
        fields=['id','caption', 'location', 'can_comment', 'tags', 'image', 'Likedby']


