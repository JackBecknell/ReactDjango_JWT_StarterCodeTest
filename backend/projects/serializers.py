from rest_framework import serializers
from authentication.models import User
from .models import Project

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username']


class ProjectSerializer(serializers.ModelSerializer):
    # project_author_id = UserSerializer(read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'date_created', 'team', 'project_author', 'project_author_id']

    project_author_id = serializers.IntegerField(write_only=True)