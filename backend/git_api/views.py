from rest_framework.viewsets import ModelViewSet, ViewSet
from django.apps import apps
from git_api import serializers

Author = apps.get_model('git_api', 'Author')
PullRequest = apps.get_model('git_api', 'PullRequest')


class AuthorsViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = serializers.AuthorSerializer


class PullRequestsViewSet(ModelViewSet):
    queryset = PullRequest.objects.all()
    serializer_class = serializers.PullRequestSerializer
