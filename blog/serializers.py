from django_grpc_framework import proto_serializers
from blog.models import Post
from blog_proto import post_pb2
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
# from django.contrib.auth.hashers import (
#     PBKDF2PasswordHasher, SHA1PasswordHasher,
# )

class PostProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Post
        proto_class = post_pb2.Post
        fields = ['id', 'title', 'content']

# class UserProtoSerializer(proto_serializers.ModelProtoSerializer):
#     class Meta:
#         model = User
#         proto_class = post_pb2.User
#         fields = ['id', 'username', 'password']

   
class UserProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = User
        proto_class = post_pb2.User
        fields = ['id', 'username', 'password']

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            password=make_password(validated_data['password'])
        )
        return user

