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
            'status',
            'from_branch',
            'to_branch'   
        ]
        read_only = ['id']
    
    author = AuthorSerializer()

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        author_serializer = AuthorSerializer(data=author_data)

        if not author_serializer.is_valid():
            raise Exception(
                f'Could not create author for PR {validated_data.get("title", None)}')

        author = author_serializer.save()
        validated_data.update(dict(author=author))
        return PullRequest.objects.create(**validated_data)
        

        