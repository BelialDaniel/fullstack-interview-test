from rest_framework import serializers
from django.apps import apps

Author = apps.get_model('git_api', 'Author')
PullRequest = apps.get_model('git_api', 'PullRequest')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            'id',
            'name',
            'last_name',
            'email'
        ]
        read_only = ['id']


class PullRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PullRequest
        fields = [
            'id',
            'author',
            'title',
            'description',
            'status'
        ]
        read_only = ['id']
    
    author = AuthorSerializer()

        